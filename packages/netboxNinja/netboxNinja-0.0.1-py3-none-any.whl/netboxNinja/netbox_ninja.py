from __future__ import annotations

import os

from dotenv import load_dotenv

from netboxNinja.logic.csv_reader import CSVReader
from netboxNinja.netbox_api.device_manager import DeviceManager
from netboxNinja.netbox_api.interface_manager import InterfaceManager
from netboxNinja.netbox_api.token_manager import TokenManager
from netboxNinja.netbox_api.vlan_manager import VLANManager

load_dotenv()


class NetboxNinja:
    def __init__(self):
        self.base_url = os.getenv("NETBOX_BASE_URL") + "/api/"
        self.username = os.getenv("NETBOX_USERNAME")
        self.password = os.getenv("NETBOX_PASSWORD")

        self.token = TokenManager.get_token(
            netbox_url=self.base_url,
            username=self.username,
            password=self.password
        )

        self.device_manager = DeviceManager(
            netbox_url=self.base_url,
            token=self.token
        )

        self.vlan_manager = VLANManager(
            netbox_url=self.base_url,
            token=self.token
        )

        self.interface_manager = InterfaceManager(
            netbox_url=self.base_url,
            token=self.token,
            device_manager=self.device_manager,
            vlan_manager=self.vlan_manager
        )

    def start(self, csv):
        interfaces = CSVReader.read_csv_as_dict_with_semicolon(csv)
        self.post_interfaces_loop(interfaces)

    def post_interfaces_loop(self, interfaces):
        if not interfaces:
            return
        later_interfaces: list = []
        for interface in interfaces:
            error = self.interface_manager.post_interface(interface)
            if error == "error":
                later_interfaces.append(interface)
        self.post_interfaces_loop(later_interfaces)
