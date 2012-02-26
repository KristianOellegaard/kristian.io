from fabric.decorators import task

from dploi_fabric.db import pg # if project uses mysql, import "mysql" instead
from dploi_fabric import git, utils, south, django_utils, supervisor, project, nginx, virtualenv

from dploi_fabric.conf import load_settings

@task
def dev():
    load_settings('dev')

@task
def stage():
    load_settings('stage')

@task
def live():
    load_settings('live')

@task
def deploy():
    pg.dump.run()
    git.update()
    virtualenv.update()
    south.migrate.run()
    django_utils.collectstatic()
    supervisor.restart()
    supervisor.status()