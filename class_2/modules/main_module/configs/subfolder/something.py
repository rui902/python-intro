#!/usr/bin/env python3
# coding: utf-8
"""Simple file importing first-level scripts"""


from configs import main_config
main_config.config()


def addm(*args):
    if len(args) == 0:
        return 0

    return args[0] + addm(*args[1:])


if __name__ == "__main__":
    print(addm(1, 2, 3, 4))
