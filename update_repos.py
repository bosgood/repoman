#!/usr/bin/python

import yaml
import os
from optparse import OptionParser

CONF_FILE = 'conf.yaml'
CUSTOM_CONF_FILE = 'custom_conf.yaml'


def do_update(options, config):
    dev_root = config['dev_root']
    excluded_repos = config['exclude_in_update_repo']
    update_groups = config['update_groups']

    # Group specified, update only those
    if options.group:
        paths = update_repo_group(
            dev_root=dev_root,
            group=update_groups[options.group]
        )

    # Just update non-excluded directories
    elif not options.all:
        paths = update_repos_basic(
            excluded_repos=excluded_repos,
            dev_root=dev_root
        )

    # Update all directories
    else:
        paths = update_all_repos(dev_root=dev_root)

    # Enter each directory separately and run the pull command
    for path in paths:
        pull_repo_updates(
            options=options,
            config=config,
            path=path
        )

    print '\033[92m\nFetched %s repos.\033[m' % (len(paths))


def update_repo_group(dev_root, group):
    '''
    Updates only the repos in the given group
    '''
    paths = [(path, '%s/%s' % (dev_root, path)) for path in group]
    return paths


def update_all_repos(dev_root):
    '''
    Updates all repos in `dev_root' whether or not they are excluded
    '''
    paths = [(path, '%s/%s' % \
                (dev_root, path)) for path in os.listdir(dev_root)]
    return paths


def update_repos_basic(excluded_repos, dev_root):
    '''
    Updates the repos in the directory `dev_root' except the ones in
    the setting `exclude_in_update_repo'
    '''
    print '\033[95mSkipping %s directories: %s\033[m' % \
            (len(excluded_repos), excluded_repos)
    paths = [(path, '%s/%s' % \
                (dev_root, path)) for path in os.listdir(dev_root) if path not in excluded_repos]
    return paths


def pull_repo_updates(options, config, path):
    '''
    Gets the latest updates from a git repo with the command specified
    in the config file
    '''
    if os.path.isdir(path[1]):
        os.chdir(path[1])
        dry_run_str = ''

        if options.dry_run:
            dry_run_str = '(NOT) '
        print '\033[92m%sGetting latest copy for repo: %s\033[m' % (dry_run_str, path[0])
        if not options.dry_run:
            os.system(config['git_pull_command'])


def get_config():
    '''
    Gets a dict representing the options configured in CONF_FILE,
    overridden by the options configured in CUSTOM_CONF_FILE
    '''
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
    parser.add_option('-a', '--all', action='store_true', help='Update all repositores in the directory, excluding none')
    parser.add_option('-d', '--dry_run', action='store_true', help='Only say what will happen if the command were to be run without this flag')
    parser.add_option('-g', '--group', dest='group', help='Update only a specific repo group')

    options, args = parser.parse_args()
    do_update(options=options, config=get_config())

if __name__ == '__main__':
    main()
