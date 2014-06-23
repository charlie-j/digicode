#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import os
from . import config

BASE_URL = 'http://localhost:8000/rpc'

CA = os.path.join(os.path.dirname(__file__), '../ssl/cacert.org_chain.pem')

def ask_code(code):
    req = requests.post('%s/code' % BASE_URL, {
      'id': config.pk_local,
      'shared_secret': config.shared_secret,
      'code': code,
      },
      verify=CA,  
     )

    if req.status_code != 200:
        raise Exception("Return code %d" % req.status_code)
    try:
        data = json.loads(req.text)
    except:
        raise Exception("Bad data")

    return data['open']

if __name__ == '__main__':
    if sys.argv[1:]:
        print("Ouverture %d" % ask_code(sys.argv[1]))
    else:
        print("Give me an arg !")
