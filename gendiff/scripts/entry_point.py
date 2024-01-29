#!/usr/bin/env python3
from gendiff.cli import run_argparse
from gendiff.diff_generator import generate_diff


def main():
    file_path_1, file_path_2, formatter = run_argparse()
    formatted_diff = generate_diff(file_path_1, file_path_2,
                                   formatter=formatter)
    print(formatted_diff)


if __name__ == '__main__':
    main()
