import os
import testinfra
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
  'wget',
  'emacs',
  'apache2',
  'unzip',
])
def test_package_installed(host, pkg):
    os = host.system_info.distribution

    if os == 'centos' and pkg == 'apache2':
        pkg = 'httpd'

    package = host.package(pkg)
    assert package.is_installed

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
