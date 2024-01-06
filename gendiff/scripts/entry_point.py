#!/usr/bin/env python3
import argparse
from gendiff.gendiff import gendiff


def main():
    args = parse_arg()
    file_path_1 = get_item(args)
    file_path_2 = get_item(args)
    gendiff(file_path_1, file_path_2)


def parse_arg():
    parser = argparse.ArgumentParser(description='Compares two '
                                     + 'configuration files and '
                                     + 'shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    return [args.first_file, args.second_file]


def get_arg(args):
    return iterable.pop(0)


if __name__ == '__main__':
    main()
