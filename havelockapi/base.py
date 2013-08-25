# -*- coding: utf-8 -*-

import json
import urllib2

from urllib import urlencode

DOC_URL = "https://www.havelockinvestments.com/apidoc.php"
BASE_URL = "https://www.havelockinvestments.com/r/{cmd}"

def command(cmd, **kwargs):
    data = urlencode(kwargs)
    url = BASE_URL.format(cmd=cmd)
    
    req = urllib2.Request(url, data=data, 
                          headers={'User-Agent': "Python api"}) 

    response = urllib2.urlopen(req)
    
    response_data = response.read()

    json_data = json.loads(response_data)

    return json_data
