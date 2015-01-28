# Database commands
#
# MySQL:
#     create: mysql -uroot -e "drop database if exists db_name"
#     drop: mysql -uroot -e "drop database if exists db_name"
#
# PostgreSQL:
#     create: createdb db_name
#     drop: dropdb db_name

import sys
from fabric.api import run, env, cd, prefix, task

env.prefix = 'source /home/webmaster/.virtualenvs/{{ project_name }}/bin/activate'
env.user = 'webmaster'


@task
def test():
    env.hosts = ['test.{{ project_name }}.com']
    env.path = '/home/webmaster/apps/{{ project_name }}'
    env.branch = 'master'
    env.db_name = '{{ project_name }}'

if 'prod' not in sys.argv:
    test()


@task
def prod():
    env.hosts = ['{{ project_name }}.com']
    env.path = '/home/webmaster/apps/{{ project_name }}'
    env.branch = 'master'
    env.db_name = '{{ project_name }}'


@task
def manage(command):
    with cd(env.path), prefix(env.prefix):
        run('python manage.py {}'.format(command))


@task
def update():
    with cd(env.path):
        run('git pull origin {}'.format(env.branch))
        run('find . -name "*.pyc" -exec rm -f {} \;')
        requirements()
        collectstatic()
        restart()


@task
def requirements():
    with cd(env.path), prefix(env.prefix):
        run('pip install --exists-action=s -r requirements.txt')


@task
def db():
    stop()
    dropdb()
    createdb()
    migrate()
    loaddata()
    start()


@task
def dropdb():
    run('dropdb {0}'.format(env.db_name))


@task
def createdb():
    run('createdb {0}'.format(env.db_name))


@task
def migrate():
    manage('migrate')


@task
def loaddata():
    manage('filldb')


@task
def collectstatic():
    manage('bower_install')
    manage('collectstatic --noinput')


@task
def restart():
    run('supervisorctl restart {{ project_name }}:')


@task
def start():
    run('supervisorctl start {{ project_name }}:')


@task
def stop():
    run('supervisorctl stop {{ project_name }}:')


@task
def status():
    run('supervisorctl status')
