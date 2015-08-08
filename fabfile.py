import sys

from fabric.api import run, env, cd, prefix, task


@task
def prod():
    env.prefix = 'source /home/webmaster/.virtualenvs/{{ project_name }}/bin/activate'
    env.user = 'webmaster'
    env.hosts = ['{{ project_name }}.com']
    env.path = '/home/webmaster/apps/{{ project_name }}'
    env.branch = 'master'
    env.db_name = '{{ project_name }}'
    env.app = '{{ project_name }}'


@task
def test():
    env.prefix = 'source /home/webmaster/.virtualenvs/{{ project_name }}/bin/activate'
    env.user = 'webmaster'
    env.hosts = ['test.{{ project_name }}.com']
    env.path = '/home/webmaster/apps/{{ project_name }}'
    env.branch = 'master'
    env.db_name = '{{ project_name }}'
    env.app = '{{ project_name }}'


if 'prod' not in sys.argv:
    test()


@task
def manage(command):
    with cd(env.path), prefix(env.prefix):
        run('python manage.py {}'.format(command))


@task
def update():
    pull()
    clean()
    requirements()
    collectstatic()
    migrate()
    restart()


@task
def pull():
    with cd(env.path):
        run('git pull origin {}'.format(env.branch))


@task
def clean():
    with cd(env.path):
        run('find . -name "*.pyc" -exec rm -f {} \;')


@task
def requirements():
    with cd(env.path), prefix(env.prefix):
        run('pip install -r requirements.txt')


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
    manage('collectstatic --noinput')


@task
def restart():
    run('supervisorctl restart {0}:'.format(env.app))


@task
def start():
    run('supervisorctl start {0}:'.format(env.app))


@task
def stop():
    run('supervisorctl stop {0}:'.format(env.app))


@task
def status():
    run('supervisorctl status')
