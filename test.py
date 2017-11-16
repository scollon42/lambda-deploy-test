from __future__ import print_function

import json

def lambda_handler(event, context):
    print(event['test'])
    return "hello"

lambda_handler({'test': 1}, True)