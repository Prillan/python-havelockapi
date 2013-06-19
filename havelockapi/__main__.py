import argparse
import sys
import api
import base
import json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(usage="%(prog)s CMD",
                                     epilog="Full documentation at\n  {}"\
                                     .format(base.DOC_URL))

    subparsers = parser.add_subparsers(dest="CMD")
    for cmd in api.HavelockApi.commands:
        current_parser = subparsers.add_parser(cmd.name)
        for opt in cmd.optional:
            current_parser.add_argument("--{}".format(opt), type=str)
        for req in cmd.required:
            current_parser.add_argument(req, type=str)

    args = parser.parse_args()

    api = api.HavelockApi()

    kwargs = args._get_kwargs()[1:]

    data = api.__getattr__(args.CMD)(**dict(kwargs))
    print json.dumps(data, indent=2)
