from argparse import ArgumentParser, RawDescriptionHelpFormatter
from typing import List, Optional, TypedDict

from src.machine_learning.main import main


class ArgConfig(TypedDict, total=False):
    name: str
    shortname: str
    type: str
    required: bool
    nargs: str
    const: Optional[str]


def console_entry() -> None:
    description = (
        "You can execute this script using the following arguments:\n"
        "    - script (integer): the script to run\n"
        "Example: python -m machine_learning -s 1\n"
        "This example executes the first script in the package.\n"
    )
    arg_config: List[ArgConfig] = [
        {
            "name": "--script",
            "shortname": "-s",
            "type": "int",
            "required": False,
            "nargs": "?",  # "*" for optional
        },
    ]

    uds_parser = ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
    for arg in arg_config:
        uds_parser.add_argument(
            arg["name"],
            arg["shortname"],
            type=arg["type"],
            required=arg["required"],
            nargs=arg["nargs"],
            const=arg["const"],
        )
    args = uds_parser.parse_args()

    main(script=args.script)


if __name__ == "__main__":
    console_entry()
