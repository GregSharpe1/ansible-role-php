ansible-role-php
=========

Install and configure php-fpm and extensions.

Requirements
------------

None.

This role has been tested solely against Ubuntu Xenial (16.04 LTS). This role
may work against other distros, but it has not been tested.

Role Variables
--------------

| Name | Default | Description |
|------|---------|-------------|
| `php_extensions` | `[ php-mysql, php-curl, php-gd, php-mbstring, php-mcrypt, php-xml, php-xmlrpc`] | List variable of php extenion packages to be installed. Defaults are the typical requirements for a wordpress installation. |
| `php_ini_path` | `/etc/php/7.0/fpm/php.ini` | `Path for the php.ini configuration file` |

Dependencies
------------

None.

Testing
-------

This role has [molecule](http://molecule.readthedocs.io/en/latest/) (v2.0.0.0rc11) testing. The molcule configuration can be found under `molecule/`. Testing is done through the [testinfra](http://testinfra.readthedocs.io/en/latest) framework.

Tests are currently configured to use the `vagrant` provider against `ubuntu/xenial64`.

Usage
-----

    - hosts: servers
      become: yes
      become_user: root
      become_method: sudo
      vars:
        php_extensions:
          - php-curl
      roles:
         - { role: ansible-role-php }

License
-------

BSD

Author Information
------------------

Nathan Davies ~ [ndavies.io](https://ndavies.io) ~ [me@ndavies.io](mailto://me@ndavies.io)
