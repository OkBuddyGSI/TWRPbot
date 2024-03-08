#!/bin/bash

# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

if ! command -v tmux &> /dev/null
then
    echo "tmux could not be found. Installing tmux..."
    sudo apt update
    sudo apt install tmux -y
    echo "tmux installed."
fi


# Authenticate using GH
gh auth login --with-token < token.txt

# Perform the git pull command
git pull origin main