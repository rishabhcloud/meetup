import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_consul_file(host):
    f = host.file('/etc/systemd/system/consul.service')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_consul_exists(host):
    f = host.file('/usr/local/bin/consul')

    assert f.exists
