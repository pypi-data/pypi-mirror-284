import typer
import rich
import os
from typing_extensions import Annotated
from trc_cli.run import run_provision
from dotenv import load_dotenv

load_dotenv()


app = typer.Typer(rich_markup_mode='rich')


@app.command()
def main(provision: Annotated[bool, typer.Option("--provision", "-p",
                                                 help="Provisions the workspace and adds sample data.")] = False):
    """
    TRC CLI
    """

    if provision:

        if load_dotenv():
            API_TOKEN = os.getenv("APITOKEN")
            BASE_URL = os.getenv("HOST")

        else:
            BASE_URL = typer.prompt("Enter your host name e.g. demo-eu-2 ", hide_input=False,
                                    )
            API_TOKEN = typer.prompt(
                "Enter your API Token", hide_input=True)

    run_provision(base_url=BASE_URL, api_token=API_TOKEN)


if __name__ == "__main__":

    app()
