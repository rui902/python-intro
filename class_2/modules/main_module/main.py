#!/usr/bin/env python3
# coding: utf-8
"""Simple main file"""


from configs import main_config
from configs.subfolder import something


def main():
    print("Running main() from main.py")
    main_config.config()
    print(something.addm(1, 2, 3, 4))


if __name__ == "__main__":
    main()
