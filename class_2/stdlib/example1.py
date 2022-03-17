#!/usr/bin/env python3
# coding: utf-8
"""Shows how importing standard library modules work"""

import sys


def main(*args):
    print("System Args:", args)


if __name__ == "__main__":
    main(sys.argv[1:])
