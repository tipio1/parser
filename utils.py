#!/usr/bin/env python3
# encoding: utf-8
"""_summary_
Work utilities
June 2023, tipio, SOC Analyst Intern
"""
import os
import sys


class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    BLUE = "\033[94m"
    END = '\033[0m'


class Directory:
    @staticmethod
    def createDirectory(directory):
        try:
            os.makedirs(directory)
            print(directory)
        except OSError:
            if not os.path.isdir(directory):
                raise
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)
