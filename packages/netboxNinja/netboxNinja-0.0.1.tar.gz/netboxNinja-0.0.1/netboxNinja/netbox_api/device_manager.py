from __future__ import annotations

import json

import requests


class DeviceManager:
    def __init__(self, netbox_url: str, token: str):
        self.netbox_url: str = netbox_url
        self.netbox_token: str = token

    def get_devices(self):
        response: requests.Response
        devices: json

        response = requests.get(self.netbox_url + 'dcim/devices/',
                                headers={'Content-Type': 'application/json',
                                         'Authorization': f'Token {self.netbox_token}'}
                                )
        try:
            devices = json.loads(response.content.decode('utf-8'))['results']
        except KeyError as error:
            print(error)
            return

        return devices

    def find_device_by_id(self, device_id: int):
        return self._finde_device(type="id", identifier=device_id)

    def find_device_by_name(self, device_name: str):
        return self._finde_device(type="name", identifier=device_name)

    def _finde_device(self, type: str, identifier: str | int):
        devices = self.get_devices()
        try:
            for device in devices:
                if device[type] == identifier:
                    return device
        except:
            print("Error: An error occurred while obtaining the devices.")
