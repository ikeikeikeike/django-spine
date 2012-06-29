

Django Spine
=============
**Spine plugin for Django**


Installation
~~~~~~~~~~~~

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

    # set static directory for your app.
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


Run the below for generating spine's project. ::

    $ python manage.py generate spine:new your_app
    $ python manage.py generate spine:scaffold your_app example name content message


Or allows removing. ::

    $ python manage.py destroy spine:scaffold your_app example name content
    $ python manage.py destroy spine:new your_app


Examples
=========

**For more information, please see the** `Example. <https://github.com/ikeikeikeike/django-spine/tree/master/examples>`_


Setup
=====

::

    $ pip install django-spine


Documentation
==============

`django-spine.readthedocs.org <http://django-spine.readthedocs.org>`_


License
=======
MIT License
