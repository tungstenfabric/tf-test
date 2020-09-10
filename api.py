"""
Non-init module for doing convenient * imports from.

Necessary because if we did this in __init__, one would be unable to import
anything else inside the package -- like, say, the version number used in
setup.py -- without triggering loads of most of the code. Which doesn't work so
well when you're using setup.py to install e.g. ssh!
"""

import string
from fabric.context_managers import (cd, hide, settings, show, path, prefix,
    lcd, quiet, warn_only, remote_tunnel, shell_env)
from fabric.decorators import (hosts, roles, runs_once, with_settings, task,
        serial, parallel)
from fabric.operations import (require, prompt, put, get, run, sudo, local,
    reboot, open_shell)
from fabric.state import env, output
from fabric.utils import abort, warn, puts, fastprint
from fabric.tasks import execute


@needs_host
def run(command, shell=True, pty=True, combine_stderr=None, quiet=False,
    warn_only=False, stdout=None, stderr=None, timeout=None, shell_escape=None,
    capture_buffer_size=None):

    return _run_command(
        command.replace("docker ", "podman "), shell, pty, combine_stderr, quiet=quiet,
        warn_only=warn_only, stdout=stdout, stderr=stderr, timeout=timeout,
        shell_escape=shell_escape, capture_buffer_size=capture_buffer_size,
    )
 

@needs_host
def sudo(command, shell=True, pty=True, combine_stderr=None, user=None,
    quiet=False, warn_only=False, stdout=None, stderr=None, group=None,
    timeout=None, shell_escape=None, capture_buffer_size=None):
    
    return _run_command(
        command.replace("docker ", "podman "), shell, pty, combine_stderr, sudo=True,
        user=user if user else env.sudo_user,
        group=group, quiet=quiet, warn_only=warn_only, stdout=stdout,
        stderr=stderr, timeout=timeout, shell_escape=shell_escape,
        capture_buffer_size=capture_buffer_size,
    )

