# Bot to send workflow requests

Step 1: Create token.txt with your github PAT and tele_token.txt with your Telegram Bot Token and grant them permissions with
```chmod +x start.sh setup.sh```

Step 2: Start the bot
```./start.sh```
To Kill existing sessions, `./start.sh --kill`

To Kill existing sessions and restart, `./start.sh --restart`

This uses tmux backend so you can view it for debugging
```tmux a -t twrpbot```

To detach, `press Ctrl B and then D`