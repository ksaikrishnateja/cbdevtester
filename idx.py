#!/usr/bin/env python3

import time
import argparse
import requests
import logging

from config import GetIndexServer, GetUserName, GetPassword, GetAuth

#g_headers = {"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"}

def GetIndexStatus():
    index_url  = GetIndexServer() + "getIndexStatus"
    r = requests.get(index_url, auth=GetAuth())
    if r.status_code != 200:
        return None
    return r.text

if __name__=="__main__":
    def arg_parser():
        parser = argparse.ArgumentParser(description='GetIndexStatus Request.')

        parser.add_argument('-l', '--log', dest='log', default="status.log", type=str,
                            help='Log file Name')
        parser.add_argument('-c', '--count', dest='count', default=100, type=int,
                            help='Count to Invoke GetIndexStatus')

        args = parser.parse_args()
        return args

    args = arg_parser()
    logging.basicConfig(filename=args.log, level=logging.INFO)
    for _ in range(args.count):
        fiename = "out.json"
        text = GetIndexStatus()
        with open(filename, 'w') as fp:
            fp.write(text)
        time.sleep(2)

