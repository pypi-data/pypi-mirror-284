Welcome to python-nessus-api's documentation!
==============================================

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
   :target: https://github.com/PyCQA/bandit
   :alt: Security Status

python-nessus-api is yet another Python package for latest Nessus Professional.

- Issue Tracker: https://gitlab.com/th1nks1mple/python-nessus/-/issues
- GitLab Repository: https://gitlab.com/th1nks1mple/python-nessus

Features
--------

- Implement the latest Nessus Professional api

Installation
------------

To install the most recent published version to pypi, its simply a matter of
installing via pip:

.. code-block:: bash

   pip install python-nessus-api

If you're looking for bleeding-edge, then feel free to install directly from the
github repository like so:

.. code-block:: bash

   pip install git+git://gitlab.com/th1nks1mple/python-nessus.git#egg=python-nessus-api

Getting Started
---------------

Lets assume that we want to get the list of scans that have been run on our
Nessus application.  Performing this action is as simple as the following:

.. code-block:: python

   from nessus import Nessus
   nessus = Nessus(url='https://localhost:8834',
                  access_key='access_key',
                  secret_key='secret_key')
   for scan in nessus.scans.list():
      print(scan)

License
-------

The project is licensed under the MIT license.
