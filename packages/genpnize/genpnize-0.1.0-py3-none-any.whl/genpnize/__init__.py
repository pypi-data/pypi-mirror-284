import argparse

from genpnize.producer import GenP

__version__ = "0.1.0"


def main():
    args = parse_args()

    input_text = args.input.read()
    for line in GenP().write_lines(input_text):
        print(line)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"))
    return parser.parse_args()
