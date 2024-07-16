import json
from pprint import pprint

import requests

from netboxNinja.netbox_api.device_manager import DeviceManager
from netboxNinja.netbox_api.vlan_manager import VLANManager


class InterfaceManager:
    def __init__(self, netbox_url: str, token: str, device_manager: DeviceManager, vlan_manager: VLANManager):
        self.netbox_url: str = netbox_url
        self.netbox_token: str = token
        self.device_manager: DeviceManager = device_manager
        self.vlan_manager: VLANManager = vlan_manager

    def get_interfaces_with_name_from_device(self, interface_name, device_name):
        for interface in self.get_interfaces():
            if interface['name'] == interface_name:
                if interface['device']['id'] == self.device_manager.find_device_by_name(device_name)['id']:
                    return interface

    def get_interfaces(self):
        response: requests.Response
        interfaces: json

        response = requests.get(self.netbox_url + 'dcim/interfaces/',
                                headers={'Content-Type': 'application/json',
                                         'Authorization': f'Token {self.netbox_token}'}
                                )

        try:
            interfaces = json.loads(response.content.decode('utf-8'))['results']
        except KeyError as error:
            print(error)
            return

        return interfaces

    def post_interface(self, interface):
        interface_copy = interface.copy()
        response: requests.Response
        device_id: int = self.device_manager.find_device_by_name(interface_copy['device'])['id']
        device_name: str = interface_copy['device']
        interface_copy['device'] = device_id

        tagged_vlans: list[int]
        tagged_vlan_ids: list[int] = []
        untagged_vlan: int

        if interface_copy['lag'] == '':
            del interface_copy['lag']
        else:
            try:
                interface_copy['lag'] = self.get_interfaces_with_name_from_device(
                    interface_name=interface_copy['lag'], device_name=device_name)['id']
            except:
                print("Lag interface not create at the moment. Try it again later.")
                return "error"
        if interface_copy['speed'] == '':
            del interface_copy['speed']

        tagged_vlans = interface_copy['tagged_vlans'].split(",")
        if tagged_vlans != ['']:
            for vlan in tagged_vlans:
                tagged_vlan_ids.append(self.vlan_manager.get_or_create_vlan_id(vlan_id=str(vlan)))
            interface_copy['tagged_vlans'] = tagged_vlan_ids
        else:
            del interface_copy['tagged_vlans']

        untagged_vlan = interface_copy['untagged_vlan']
        if untagged_vlan != '':
            untagged_vlan_id = self.vlan_manager.get_or_create_vlan_id(vlan_id=str(untagged_vlan))
            interface_copy['untagged_vlan'] = untagged_vlan_id
        else:
            del interface_copy['untagged_vlan']

        response = requests.post(self.netbox_url + 'dcim/interfaces/',
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': f'Token {self.netbox_token}'},
                                 json=interface_copy
                                 )

        pprint(response.json())
