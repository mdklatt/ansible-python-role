..  README for the python role.

======
python 
======
..  |travis.png| image:: https://travis-ci.org/mdklatt/ansible-python-role.png?branch=master
    :alt: Travis CI build status
    :target: `travis`_
..  _travis: https://travis-ci.org/mdklatt/ansible-python-role
..  _Ansible: http://docs.ansible.com/ansible

|travis.png|

`Ansible`_ role to install essential Python packages. Additional packages
should be deployed per-application in a `virtualenv` environment.


Requirements
============
The target machine must have Python 2.7 installed.


Dependencies
============
- tmpdir: https://github.com/mdklatt/ansible-tmpdir-role


Role Variables
==============
- ``python_local``: local binary directory; system-dependent


Example Playbook
================
..  code::

    - hosts: all
      
      roles:
        - name: python
