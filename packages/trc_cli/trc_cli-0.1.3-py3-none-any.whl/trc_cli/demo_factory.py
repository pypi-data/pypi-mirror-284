import json
import logging
from pathlib import Path
from typing import List
import requests
import os
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed, wait_random
from trc_cli.constants import TEMP_STORAGE
from trc_cli.authenticator import LeanIXAPIAuthenticator
from trc_cli.utils import get_random_sbom
from trc_cli.exceptions import LeanIXDemoFactoryException


logging.basicConfig(level=logging.WARN)

temp_storage = Path(TEMP_STORAGE)


class LeanIXTechDiscoveryDemoFactory:
    """Class to generate demo entries to a tech discovery provisioned Workspace"""

    _base_url: str
    _authenticator: LeanIXAPIAuthenticator
    _user_agent: str = "LeanIXTechDiscoveryDemoProvisioner"
    _request_timeout: int = 10
    session: requests.Session

    def __init__(
        self,
        base_url: str,
        api_token: str,
        session: requests.Session | None = None,
    ):
        self._base_url = base_url
        self.session = session or requests.Session()
        self._authenticator = LeanIXAPIAuthenticator(
            api_token=api_token,
            base_url=base_url,
            user_agent=self._user_agent,
            session=self.session,
        )

    def prepare_request(self):
        """Prepares the request details"""
        self.session.headers = {
            "User-Agent": self._user_agent,
            "Authorization": f"Bearer {self._authenticator.access_token}",
        }

    @retry(
        retry=retry_if_exception_type(requests.RequestException),
        stop=stop_after_attempt(3),
        wait=wait_fixed(3) + wait_random(0, 2),
    )
    def register_microservice(self, microservices: List[dict]) -> List[dict]:
        """Registeres a microservice with LeanIX creating the relevant fact sheet.

        Args:
            microservices (List[dict]): A list of dictionaries with the micro services information.
        """
        registered_microservices = list()
        micro_services_endpoint = f"https://{
            self._base_url}.leanix.net/services/technology-discovery/v1/microservices"
        self.prepare_request()
        for microservice in microservices:
            logging.info(f"Preparing to register microservice: {microservice}")
            try:
                response = self.session.post(
                    url=micro_services_endpoint, json=microservice, timeout=self._request_timeout)
                response.raise_for_status()
            except requests.RequestException as e:
                # Conflict just means that the microservice is already registered
                if response.status_code == 409:

                    logging.info(f"Microservice {
                                 microservice} is already registered")
                    continue
                else:
                    logging.error(f"Could not register microservice: {
                                  microservice}, reason: {e}")
                    raise LeanIXDemoFactoryException(f"Could not register microservice: {
                                                     microservice}, reason: {e}") from e
            else:
                registered_microservices.append({
                    "name": microservice.get("name"),
                    "externalId": microservice.get("externalId"),
                    "factSheetId": response.json().get("data", {}).get("factSheetId")
                })
                logging.info(f"Succesfully registered microservice: {
                             microservice}")
        return registered_microservices

    def store_microservices(self, microservices: List[dict], location: Path = temp_storage):
        """Writes the registered microservices into a file

        Returns:
            _type_: _description_
        """
        with location.open(mode="w") as file:
            file.write(json.dumps(microservices))
            logging.info(f"Stored microservices fact sheet ids: {
                         location.absolute()}")
            return True

    def attach_sboms(self, factsheet_ids: List[dict]):

        for factsheet_id in factsheet_ids:
            sbom_endpoint = f"https://{
                self._base_url}.leanix.net/services/technology-discovery/v1/microservices/{factsheet_id}/sboms"
            self.prepare_request()

            logging.info(f"Preparing to attach sbom for Factsheet ID: {
                         factsheet_id}")

            sbom_path = get_random_sbom()
            with sbom_path.open('rb') as f:
                sbom_contents = f.read()

            request_payload = {
                'sbom': (
                    'spdx.json',
                    sbom_contents,
                    'application/json'
                )
            }
            try:
                response = self.session.post(
                    url=sbom_endpoint, files=request_payload, timeout=self._request_timeout)
                response.raise_for_status()

            except requests.RequestException as e:

                if response.status_code == 201:
                    logging.info(
                        f"Attached SBOM to Factsheet: {factsheet_id}")
                    continue
                else:
                    logging.error(f"Could not attach SBOM to Factsheet {
                                  factsheet_id}: , reason: {e}")

    def delete_temp_files(location: Path = temp_storage):
        try:
            os.remove(str(location))
            logging.info(f" Deleted {str(location)}")

        except FileNotFoundError:
            logging.error(f"File {str(location)} not found.")

        except Exception as e:
            logging.error(f"Error occurred while deleting file {
                          str(location)}:", str(e))
