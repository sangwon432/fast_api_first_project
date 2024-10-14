#!/bin/bash

# Change to the git repository directory
# Uncomment and modify the next line if you want to specify a particular directory
# cd /path/to/your/git/repository

# Fetch the latest changes from the remote repository
git fetch

# Check if there are any changes to pull
UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "$LOCAL"
    echo "Need to pull"
    git pull
    kill -HUP 3380
else
    echo "Diverged"
fi