Development
===========

The ``asr`` toolkit is developed by Martin Thoma. The development began in
November 2014.

It is developed on GitHub: https://github.com/MartinThoma/asr

You can file issues and feature requests there. Alternatively, you can send
me an email: info@martin-thoma.de

Tools
-----

* ``nosetests`` for unit testing
* ``pylint`` to find code smug
* GitHub for hosting the source code
* https://pythonhosted.org/asr for hosting the documentation


Code coverage can be tested with

.. code:: bash

    $ nosetests --with-coverage --cover-erase --cover-package asr --logging-level=INFO --cover-html

and uploaded to coveralls.io with

.. code:: bash

    $ coveralls


Documentation
-------------

The documentation is generated with `Sphinx <http://sphinx-doc.org/latest/index.html>`_.
On Debian derivates it can be installed with

.. code:: bash

    $ sudo apt-get install python-sphinx

Sphinx makes use of `reStructured Text <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_

The documentation can be built with ``make html``.



Project structure
-----------------

The project structure is

::

    .
    ├── asr
    ├── bin
    ├── docs
    └── tests


where the folder ``bin`` contains all scripts that can directly be used,
``asr`` contains all modules and ``tests`` contains unittests written with
nosetools.