# configuration module for my scripts run locally

# Root directory for all repos
DEV_ROOT = ''

# Repos to exclude from the global update script
EXCLUDE_IN_UPDATE_REPO = [

]

# Command to use to update a repo
GIT_PULL_COMMAND = 'git pull --rebase'

# Not working yet...
# GIT_PULL_COMMAND = 'git pull --rebase origin $(current_branch)'
