repoman
=======

![repoman](https://raw.github.com/bosgood/repoman/master/repoman.jpg)

Do you have a project where you have to work with multiple git repos at the same time? Really? That kind of sucks.

But hey, we're here to help you keep all of them updated.

## Setup

* Clone this repo.

        git clone git@github.com:bosgood/repoman.git

* From the directory you cloned it to, install repoman's dependencies.

        python setup.py install

* Symlink `rpman.py` to somewhere in your `PATH` as `repoman`. (to find this: `echo $PATH`)

        ln -s /path/to/rpman.py /path/in/PATH/repoman
        chmod +x /path/to/rpman.py

* Create a `~/.repoman.yaml` file by copying `conf.yaml` in this project.

        cp /path/to/conf.yaml ~/.repoman.yaml

* (optional) Add a group name and underneath, the names of the repos you intend to pull by group.
* (optional) Add to `exclude_in_update_repo` to exclude particular repos from that global update function.

## Usage
* To update all repos in `dev_root` except those in `exclude_in_update_repo`:

         repoman

* To update all repos in `<group>`:

         repoman -g <group>

* To update one repo individually:

         repoman -i <repo_name>




