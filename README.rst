``Spine plugin for Django``

Description
===========

Requirements
============
* django
* django-subcommand

Features
========


Setup
=====

.. highlight:: bash

::

    $ pip install django-spine


Installation
~~~~~~~~~~~~

.. highlight:: python

edit settings.py ::

    INSTALLED_APPS = (
        "subcommand",
        "spine",
        'compressor',
    )

Run the below for generating spine's project ::

    $ python manage.py generate spine:new app

    $ python manage.py generate spine:scaffold app appclass name message date


History
========
0.x (2012-xx-xx)
~~~~~~~~~~~~~~~~
* first release

License
=======
MIT License
