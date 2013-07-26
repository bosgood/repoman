#!/usr/bin/python

import os
import conf_object
from optparse import OptionParser


def update_repos(all=False, dry_run=False):
    if not all:
        print '\033[95mSkipping %s directories: %s\033[m' % (len(conf_object.EXCLUDE_IN_UPDATE_REPO), conf_object.EXCLUDE_IN_UPDATE_REPO)
        paths = [(path, '%s/%s' % (conf_object.DEV_ROOT, path)) for path in os.listdir(conf_object.DEV_ROOT) if path not in conf_object.EXCLUDE_IN_UPDATE_REPO]
    else:
        paths = [(path, '%s/%s' % (conf_object.DEV_ROOT, path)) for path in os.listdir(conf_object.DEV_ROOT)]
    for path in paths:
        if os.path.isdir(path[1]):
            os.chdir(path[1])
            dry_run_str = ''
            if dry_run:
                dry_run_str = '(NOT) '
            print '\033[92m%sGetting latest copy for repo: %s\033[m' % (dry_run_str, path[0])
            if not dry_run:
                os.system(conf_object.GIT_PULL_COMMAND)

    print '\033[92m\nFetched %s repos.\033[m' % (len(paths))


def main():
    parser = OptionParser()
    parser.add_option('-a', '--all', action='store_true')
    parser.add_option('-d', '--dry_run', action='store_true')

    options, args = parser.parse_args()

    update_repos(all=options.all, dry_run=options.dry_run)

if __name__ == '__main__':
    main()
