import os
import pytest
import testinfra
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

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

