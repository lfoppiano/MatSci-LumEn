import json
import time
from typing import Union

import requests

from commons.grobid.client import ApiClient

'''
This client is a generic client for any Grobid application and sub-modules.
At the moment, it supports only single document processing.

Source: https://github.com/kermitt2/grobid-client-python 
'''


class MaterialParsersClient(ApiClient):

    def __init__(self, base_url="http://localhost:8090", ping=False):
        self.base_url = base_url
        super().__init__(self.base_url)

        if ping:
            result = self.ping()
            if not result:
                raise Exception("Material parsers server is down.")

    def ping(self):
        ping_url = f"{self.base_url}/version"

        r = requests.get(ping_url)
        status = r.status_code

        if status != 200:
            print('The server does not appear up and running ' + str(status))
            return False
        else:
            print("The server is up and running")
            return True

    def parse_materials(self,
                        input: Union[str, list],
                        params={},
                        headers={"Accept": "application/json"}):

        files = {
            'texts': input
        }

        the_url = f"{self.base_url}/process/material"

        res, status = self.post(
            url=the_url,
            files=files,
            data=params,
            headers=headers
        )

        if status == 503:
            time.sleep(5)
            return self.parse_materials(input, params, headers)
        elif status != 200:
            print('Processing failed with error ' + str(status))
            return status, None
        else:
            return status, json.loads(res.text)
