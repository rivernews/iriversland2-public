from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    # TODO: setup init-container for iriversland2-api

    # TODO: check database - if already have db, if have admin account, if data seems ok, then skip

    # TODO: pull latest json from s3

    # TODO: create postgres db

    # TODO: migrate db using Django's schema, trim tables
    '''./manage.py migrate && echo "delete from auth_permission; delete from django_content_type;" | python manage.py dbshell
    '''

    # TODO: load into postgres VIA DJANGO manage command
    '''./manage.py loaddata <json_path>
    '''
    pass