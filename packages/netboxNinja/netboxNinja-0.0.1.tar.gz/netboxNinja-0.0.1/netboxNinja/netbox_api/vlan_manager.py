import json
from pprint import pprint

import requests


class VLANManager:
    def __init__(self, netbox_url: str, token: str):
        self.netbox_url: str = netbox_url
        self.netbox_token: str = token

    def get_vlans(self):
        response: requests.Response
        vlans: json

        response = requests.get(self.netbox_url + 'ipam/vlans/',
                                headers={'Content-Type': 'application/json',
                                         'Authorization': f'Token {self.netbox_token}'}
                                )
        try:
            vlans = json.loads(response.content.decode('utf-8'))['results']
        except KeyError as error:
            print(error)
            return

        return vlans

    def post_vlan(self, vlan_id: str):
        response: requests.Response

        response = requests.post(self.netbox_url + 'ipam/vlans/',
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': f'Token {self.netbox_token}'},
                                 json={'name': vlan_id,
                                       'vid': int(vlan_id)}
                                 )
        pprint(response.json())
        return response.json()

    def get_or_create_vlan_id(self, vlan_id: str):
        vlans = self.get_vlans()
        for vlan in vlans:
            if vlan['vid'] == int(vlan_id):
                return vlan['id']
        return self.post_vlan(vlan_id=vlan_id)['vid']
