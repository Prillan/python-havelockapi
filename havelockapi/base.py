# -*- coding: utf-8 -*-

import json
import urllib2

from urllib import urlencode

DOC_URL = "https://www.havelockinvestments.com/apidoc.php"
BASE_URL = "https://www.havelockinvestments.com/r/{cmd}"

def command(cmd, **kwargs):
    data = urlencode(kwargs)
    response = urllib2.urlopen(BASE_URL.format(cmd=cmd), data)
    
    response_data = response.read()

    json_data = json.loads(response_data)

    return json_data
