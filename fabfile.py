from fabric.api import (
    cd,
    env,
    prefix,
    require,
    run,
    sudo,
    task,
)
from fabric.contrib import console
from fabric.utils import abort

# globals
env.project = "eGazeciarz"
env.user = "egazeciarz"
env.work_user = None

env.path = "/home/%s" % env.user
env.env_path = "%s/venv" % env.path
env.repo_path = "%(path)s/%(project)s" % {
    "path": env.path,
    "project": env.project,
}
env.work_path = "%s/egazeciarz" % env.repo_path

env.prompt = True


@task
def production():
    """
    Select production environment
    """
    env.environment = "production"
    env.port = 1337
    env.hosts = [
        "%(user)s@beta.egazeciarz.pl:%(port)d" % {
            "user": env.work_user,
            "port": env.port,
        }
    ]
    env.branch = "master"
    env.work_path += "_%s" % env.environment
    env.venv_path += "_%s" % env.environment


@task
def staging():
    """
    Select staging environment
    """
    env.environment = "staging"
    env.port = 1337
    env.hosts = [
        "%(user)s@staging.egazeciarz.pl:%(port)d" % {
            "user": env.work_user,
            "port": env.port,
        }
    ]
    env.branch = "dev"
    env.work_path += "_%s" % env.environment
    env.venv_path += "_%s" % env.environment


@task
def noinput():
    """
    Answer affirmatively to all prompts
    """
    env.prompt = False


def pull_changes():
    """
    Switch to appropriate branch and pull changes from upstream
    """

    check_prompt = (
        not env.prompt or
        console.confirm(
            "Switch to appropriate branch and pull changes from upstream?",
            default=True,
        )
    )

    if check_prompt:
        with cd(env.repo_path):
            run("git checkout %s" % env.branch)
            run("git pull")


def update_requirements():
    """
    Update virtualenv requirements based on requirements.txt file
    """

    check_prompt = (
        not env.prompt or
        console.confirm(
            "Update virtualenv requirements based on requirements.txt file?",
            default=True,
        )
    )

    if check_prompt:
        with cd("%s" % env.repo_path):
            with prefix("source %s/bin/activate" % env.env_path):
                run(
                    "pip install"
                    "--requirement %s/requirements.txt" % env.repo_path
                )


def collect_static():
    """
    Collect static files and copy them to collect_static
    """

    check_promt = (
        not env.prompt or
        console.confirm(
            "Collect static files and copy them to collect_static?",
            default=True,
        )
    )

    if check_promt:
        with cd("%s" % env.work_path):
            with prefix("source %s/bin/activate" % env.env_path):
                run(
                    "./manage.py collectstatic"
                    "--noinput"
                )


def sync_db():
    """
    Create tables for models which have not yet been installed
    """

    check_prompt = (
        not env.prompt or
        console.confirm(
            "Create tables for models which have not yet been installed?",
            default=True,
        )
    )

    if check_prompt:
        with cd("%s" % env.work_path):
            with prefix("source %s/bin/activate" % env.env_path):
                run(
                    "./manage.py syncdb"
                    "--noinput"
                )


def cleanup_pyc():
    """
    Remove .pyc files
    """
    check_prompt = (
        not env.prompt
        or console.confirm(
            "Remove .pyc files?",
            default=True,
        )
    )

    if check_prompt:
        with cd("%s" % env.repo_path):
            run("find . -name \*.pyc -delete")


def restart_apache():
    """
    Restart Apache web server
    """
    check_prompt = (
        not env.prompt or
        console.confirm(
            "Restart Apache web server?",
            default=True,
        )
    )

    if check_prompt:
        sudo("service apache2 restart")


@task
def deploy():
    """
    Deploy code to remote host
    """
    require(
        "environment",
        provided_by=[
            production,
            staging
        ]
    )

    check_prompt = (
        env.prompt and
        env.environment == "production" and
        not console.confirm(
            "Are you sure you want to deploy production?",
            default=False,
        )
    )
    if check_prompt:
        abort("Production deployment aborted.")

    pull_changes()
    update_requirements()
    collect_static()
    sync_db()
    cleanup_pyc()
    restart_apache()


@task(default=True)
def usage():
    """
    Print usage examples
    """
    print(
        """
Usage examples:

Staging deployment:
       $ fab [noinput] staging deploy

Production deployment:
       $ fab [noinput] production deploy
""")
