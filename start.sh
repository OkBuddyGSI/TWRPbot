#!/bin/bash

# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Authenticate using GH
gh auth login --with-token < token.txt

# Perform the git pull command
git pull origin main

# Parse command line argument
case $1 in
    --kill)
        echo "Stopping the bot..."
        tmux kill-session -t twrpbot
        echo "Bot stopped."
        ;;
    --restart)
            tmux kill-session -t twrpbot;
            tmux new-session -d -s twrpbot
            tmux send-keys -t twrpbot 'python3 main.py' Enter
            echo "Runner Restarted"
        ;;
    *)
        if tmux has-session -t twrpbot;
        then
            echo "Bot is already Running"
        else
            tmux new-session -d -s twrpbot
            tmux send-keys -t twrpbot 'python3 main.py' Enter
            echo "Runner Started"
        fi
        ;;
esac