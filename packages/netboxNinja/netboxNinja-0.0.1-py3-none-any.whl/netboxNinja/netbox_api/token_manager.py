import json
import sys

import requests


class TokenManager:

    @staticmethod
    def get_token(netbox_url: str, username: str, password: str):
        netbox_token: str
        response: requests.Response
        json_response: json

        response = requests.post(netbox_url + 'users/tokens/provision/',
                                 headers={'Content-Type': 'application/json'},
                                 data=f'{{"username": "{username}", '
                                      f'"password": "{password}"}}'
                                 )

        try:
            json_response = json.loads(response.content.decode('utf-8'))
            netbox_token = json_response['key']
        except KeyError:
            print("Cannot obtain a token.\n"
                  "Please check the Netbox URL, username and password.")
            sys.exit(1)
        except:
            print("Error: Cannot obtain a token.\n")
            print(json_response)
            print(response)
            sys.exit(1)

        return netbox_token
