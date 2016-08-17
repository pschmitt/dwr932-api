#!/usr/bin/python
# coding: utf-8

from __future__ import print_function
import argparse
from api import Dwr932


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['connect', 'disconnect', 'usage', 'battery'])
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    d = Dwr932()
    r = ''
    if args.action == 'connect':
        r = d.connect()
    elif args.action == 'disconnect':
        r = d.disconnect()
    elif args.action == 'usage':
        r = d.get_data_usage()
    elif args.action == 'battery':
        r = d.get_battery_info()
    print(r)
