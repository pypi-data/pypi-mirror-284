# -*- coding: utf-8 -*-
"""
File name: rex_language.py
Author: Bowen
Date created: 15/7/2024
Description: Rex language SDK, providing help information and expressions for Rex language

Copyright information: © 2024 QDX
"""

import argparse
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(script_dir, 'rex_expressions.json')
try:
    with open(json_path, 'r') as f:
        rex_expressions = json.load(f)
except FileNotFoundError:
    print(f"Warning：cannot find file '{json_path}'.")
    rex_expressions = {}


def get_rex_help():
    """
    Get the help information of Rex language
    :return: help information
    """
    return rex_expressions.get("help_info", "Cannot find the help information.")


def get_rex_expression(keyword):
    """
    Get the specific Rex expression for RUSH modules
    :param keyword: the module name of the Rex expression
    :return: the corresponding Rex expression
    """
    return rex_expressions.get(keyword, "Corresponding Rex expression not found, please use 'rex-help expression' to get the list of available expressions.")


def main():
    parser = argparse.ArgumentParser(description='chemllmhack: Rex Language SDK')
    parser.add_argument('--rex-help', choices=['language', 'expression'], help='Get help information')
    parser.add_argument('-rex', help='Get a specific Rex expression')

    args = parser.parse_args()

    if args.rex_help == 'language':
        print(get_rex_help())
    elif args.rex_help == 'expression' and args.rex:
        print(get_rex_expression(args.rex))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()