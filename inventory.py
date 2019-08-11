"""Script to create dynamic inventory file for ansible nodes
"""

import os
import sys
import json
import argparse


class AnsibleInventory(object):

    def __init__(self):
        # class level variable declarations
        self.all_nodes = list()
        self.uninstall_nodes = list()
        self.args = list()

        self.read_cli_arguments()
        self.parse_node_list()

        __inventory = self.write_resource_list()
        print json.dumps(__inventory)

    @staticmethod
    def return_list(delimited_string):
        return [str(x).strip() for x in str(delimited_string).split()]

    def parse_node_list(self):
        self.all_nodes = self.return_list(self.args.host)
        self.uninstall_nodes = self.return_list(self.args.uninstall)

    def write_resource_list(self):
        return {
            '_meta':{'hostvars':{}},
            'all': {
              'hosts': self.all_nodes
            },
            'validate_nodes': {
              'hosts': self.all_nodes
            },
            'uninstall_nodes': {
              'hosts': self.uninstall_nodes
            }
        }

    def read_cli_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store', dest='list')
        parser.add_argument('--hosts', action='store', dest='host')
        parser.add_argument('--uninstall', action='store', dest='uninstall')

        self.args = parser.parse_args()


AnsibleInventory()
