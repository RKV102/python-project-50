#!/usr/bin/env python3
import argparse
from gendiff.gendiff import gendiff


def main():
    parser = argparse.ArgumentParser(description='Compares two '
                                     + 'configuration files and '
                                     + 'shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    file_path_1 = args.first_file
    file_path_2 = args.second_file
    gendiff(file_path_1, file_path_2)


def get_arg(args):
    return args.pop(0)


if __name__ == '__main__':
    main()
