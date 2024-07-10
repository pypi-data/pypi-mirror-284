import logging
from argparse import ArgumentParser

from castor_extractor.visualization import mode  # type: ignore

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


def main():
    parser = ArgumentParser()

    parser.add_argument("-H", "--host", help="Mode Analytics host")
    parser.add_argument("-w", "--workspace", help="Mode Analytics workspace")
    parser.add_argument(
        "-t",
        "--token",
        help="The Token value from the API token",
    )
    parser.add_argument(
        "-s",
        "--secret",
        help="The Password value from the API token",
    )

    parser.add_argument("-o", "--output", help="Directory to write to")

    args = parser.parse_args()
    credentials = mode.Credentials(
        host=args.host,
        workspace=args.workspace,
        token=args.token,
        secret=args.secret,
    )

    mode.extract_all(
        credentials,
        output_directory=args.output,
    )
