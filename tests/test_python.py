""" Test suite for the python role.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the package is actually
being tested. If the package is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from os.path import abspath
from os.path import dirname
from os.path import join
from shlex import split
from shutil import copytree
from subprocess import call
from subprocess import check_call

import pytest


@pytest.fixture
def install(tmpdir):
    """ Install the role in a temporary working directory.

    """
    # TODO: Install the role using ansible-galaxy.
    pathobj = tmpdir.join("python")
    dirs = "defaults", "handlers", "meta", "tasks", "tests", "vars"
    root = dirname(dirname(abspath(__file__)))
    for name in dirs:
        copytree(join(root, name), join(pathobj.strpath, name))
    return pathobj.strpath


@pytest.fixture
def galaxy(install):
    """ Install dependencies using ansible-galaxy.

    """
    # When a role is installed using ansible-galaxy, its dependencies (see
    # meta/main.yml) will automatically be installed, but for testing the
    # dependencies must be installed manually.
    reqs = join(dirname(abspath(__file__)), "requirements.yml")
    roles = join(install, "tests", "roles")
    galaxy = "ansible-galaxy install -r {:s} -p {:s}".format(reqs, roles)
    check_call(split(galaxy))
    return


@pytest.mark.usefixtures("galaxy")
def test_role(install):
    """ Test the role syntax.

    """
    ansible = "ansible-playbook --syntax-check playbook.yml"
    assert 0 == call(split(ansible), cwd=join(install, "tests"))
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))
