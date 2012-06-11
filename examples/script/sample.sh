#!/bin/sh -x -e
python manage.py generate spine:new spineapp

python manage.py generate spine:scaffold spineapp example name content message
