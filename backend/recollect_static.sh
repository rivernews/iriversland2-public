#!/bin/sh

rm -r -f www/static && ./manage.py collectstatic --noinput && echo "SUCCESS: static files recollected."