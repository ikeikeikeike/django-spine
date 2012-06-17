

Django Spine
=============
``Spine plugin for Django``


Installation
~~~~~~~~~~~~

.. highlight:: python

edit settings.py ::

    # set (subcommand, spine, pipeline) package.
    INSTALLED_APPS = (
        # external
        "subcommand",
        "spine",
        'pipeline',

        # applications
        "your_app" #
    )

    # set static project directory for your app.
    PIPELINE_JS = {
        'application': {
            'source_filenames': (
                'js/*.js',
                'js/spine/*.js',
                'js/spine/**/*.js',
                'js/your_app/lib/*.coffee',
                'js/your_app/*.coffee',
                'js/your_app/models/*.coffee',
                'js/your_app/controllers/*.coffee',
                'js/your_app/views/**/*.eco',
            ),
            'output_filename': 'js/application.r?.js'
        }
    }

    # set Eco Compiler
    PIPELINE_COMPILERS = (
        'pipeline.compilers.coffee.CoffeeScriptCompiler',
        'spine.compiler.EcoCompiler',  # this compiler.
    )


Run the below for generating spine's project ::

    $ python manage.py generate spine:new app

    $ python manage.py generate spine:scaffold app appclass name message date


Examples
=========

**For more information, please see the** `Example. <https://github.com/ikeikeikeike/django-spine/tree/master/examples>`_


Setup
=====

.. highlight:: bash

::

    $ pip install django-spine


History
========
0.0.1 (2012-06-16)
~~~~~~~~~~~~~~~~~~~
* Alpha

0.0.2 (2012-06-17)
~~~~~~~~~~~~~~~~~~~
* Added the django-pipeline and eco package to requirements.txt
* modify examples
* modify README.rst

License
=======
MIT License
