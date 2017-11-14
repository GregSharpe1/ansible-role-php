import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def defaults(Ansible):
    return Ansible("include_vars", "../../defaults/main.yml")["ansible_facts"]


def test_php_fpm_install(host):
    assert host.package("php-fpm").is_installed


def test_php_extensions_install(host, defaults):
    for package in defaults['php_extensions']:
        assert host.package(package).is_installed


def test_php_ini_security_fix(host):
    php_ini = host.file("/etc/php/7.0/fpm/php.ini")

    assert php_ini.contains("cgi.fix_pathinfo=0")
    assert not php_ini.contains(";cgi.fix_pathinfo")
