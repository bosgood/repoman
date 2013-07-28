#!/usr/bin/python

import yaml
import os
from optparse import OptionParser

CONF_FILE = 'conf.yaml'
CUSTOM_CONF_FILE = 'custom_conf.yaml'


def do_update(options, config):
    dev_root = config['dev_root']
    excluded_repos = config['exclude_in_update_repo']

    # Just update non-excluded directories
    if not options.all:
        paths = update_repos_basic(
            excluded_repos=excluded_repos,
            dev_root=dev_root
        )

    # Update all directories
    else:
        paths = update_all_repos(dev_root=dev_root)

    # Enter each directory separately and run the pull command
    for path in paths:
        if os.path.isdir(path[1]):
            os.chdir(path[1])
            dry_run_str = ''

            if options.dry_run:
                dry_run_str = '(NOT) '
            print '\033[92m%sGetting latest copy for repo: %s\033[m' % (dry_run_str, path[0])
            if not options.dry_run:
                os.system(config['git_pull_command'])

    print '\033[92m\nFetched %s repos.\033[m' % (len(paths))


def update_all_repos(dev_root):
    paths = [(path, '%s/%s' % \
                (dev_root, path)) for path in os.listdir(dev_root)]
    return paths


def update_repos_basic(excluded_repos, dev_root):
    print '\033[95mSkipping %s directories: %s\033[m' % \
            (len(excluded_repos), excluded_repos)
    paths = [(path, '%s/%s' % \
                (dev_root, path)) for path in os.listdir(dev_root) if path not in excluded_repos]
    return paths


def get_config():
    config = {}
    config_paths = [CONF_FILE, CUSTOM_CONF_FILE]
    for config_path in config_paths:
        try:
            with open(config_path, 'r') as stream:
                file_data = yaml.load(stream)
                config.update(file_data)

        except Exception:
            if config_path == CONF_FILE:
                print 'Configuration file %s not found.' % CONF_FILE
                raise

    return config


def main():
    parser = OptionParser()
    parser.add_option('-a', '--all', action='store_true')
    parser.add_option('-d', '--dry_run', action='store_true')
    parser.add_option('-g', '--group', action='store_true')

    options, args = parser.parse_args()
    do_update(options=options, config=get_config())

if __name__ == '__main__':
    main()
