import argparse
import configparser
from datetime import datetime

try:
    import grp,pwd
except ModuleNotFoundError:
    pass

from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(description = "NovaVCS - A content-addressable version control system")

argsubparsers = argparser.add_subparsers(title = "Commands", dest = "command")
argsubparsers.required = True

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    
    COMMANDS = {
        "init" : cmd_init,
        "add" : cmd_add,
        "commit": cmd_commit,
        "status": cmd_status,
        "log": cmd_log,
        "checkout": cmd_checkout,
        "branch": cmd_branch,
        "hash-object": cmd_hash_object,
        "ls-tree": cmd_ls_tree,
        "cat-file": cmd_cat_file,
        "write-tree": cmd_write_tree,
    }

    COMMANDS[args.command](args)


    class GitRepository(object):
        """A git repository"""

        worktree = None
        gitdir = None
        conf = None

        def __init__(self, path, force=False):
            self.worktree = path
            self.gitdir = os.path.join(path, ".git")

            if not(force or os.path.isdir(self.gitdir)):
                raise Exception(f"Not a git repository {path}")
            
            # Read configuration file in the .git/config
            self.conf = configparser.ConfigParser()
            cf = repo_file(self, "config")

            if cf and os.path.exists(cf):
                self.conf.read([cf])
            elif not forse:
                raise Exception("Configuration file missing")
            
            if not force:
                vers = int(self.conf.get("core", "repositoryformatversion"))
                if vers != 0:
                    raise Exception(f"Unsupported repositoryformatversion: {vers}")


def repo_path(repo, *path):
    """Compute path under repo's gitdir"""
    return os.path.join(repo.gitdir, *path)


def repo_file(repo, *path,mkdir = False):