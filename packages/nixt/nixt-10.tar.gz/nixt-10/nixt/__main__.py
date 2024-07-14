# This file is placed in the Public Domain.
# pylint: disable=C0413,W0212,E0401


"main"


import getpass
import os
import pwd
import sys


from .cfg   import Config
from .defer import errors
from .disk  import Persist, skel, pidfile
from .main  import cmnd, enable, init, scan
from .parse import parse
from .utils import forever, modnames


from . import modules
from . import user


Cfg         = Config()
Cfg.name    = "nixt"
Cfg.user    = getpass.getuser()
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


def daemon(verbose=False):
    "switch to background."
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")


def privileges(username):
    "drop privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def background():
    "main"
    daemon("-v" in sys.argv)
    skel()
    pidfile(Cfg.pidfile)
    privileges(Cfg.user)
    if "-v" in sys.argv:
        enable(print)
    Cfg.mod = ",".join(modnames(modules, user))
    scan(Cfg.mod, modules, user)
    init(Cfg.mod, modules, user)
    forever()


def main():
    "main"
    parse(Cfg, " ".join(sys.argv[1:]))
    enable(print)
    if "h" in Cfg.opts:
        return cmnd("hlp", print)
    Cfg.dis = Cfg.sets.dis
    Cfg.mod = ",".join(modnames(modules, user))
    scan(Cfg.mod, modules, user)
    return cmnd(Cfg.otxt, print)


if __name__ == "__main__":
    if "-d" in sys.argv:
        background()
    else:
        main()
    errors()
