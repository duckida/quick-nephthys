# quick nephthys

A quick way to setup [Hack Club Nephthys](https://github.com/hackclub/nephthys), a Slack support bot for YSWSs and other programs!

Designed for Linux or macOS servers such as [Hack Club Nest](https://hackclub.app)! 

## how does this work?
quick nephthys is a python script which asks you questinos about your setup & program, and automatically configures Nephthys's transcripts, environment file, and installs everything!

## how can i use it?
### Prerequisites:
#### Docker (for database)
Nephthys requires a PostgreSQL database to store tickets. An easy way to run one is using Docker.

If Docker is isntalled (https://docs.docker.com/engine/install), quick-nephthys can easily setup your database!

#### Slack bot
A [video demo](https://user-cdn.hackclub-assets.com/019ff147-b57b-79d5-85f7-29e888509556/slack-api-setup-quick-nephthys.mp4) is available.

1. Go to https://api.slack.com/apps and click "Create New App".
2. quick-nephthys will create a Slack manifest for you to paste during the flow
2. Choose "From an app manifest" and select your workspace.
3. Paste the manifest
4. Review and create the app.
5. Under Settings→Install app, install the app in your workspace
6. Store the User OAuth Token and Bot User OAuth Token
7. From Settings→Basic Information, retrieve and store the Signing Secret.
8. Scroll to App-Level Tokens and create one called Nephthys, and store this too
9. Add your bot to your help channels
### Slack channels
Create a public-facing help channel, a private tickets channel, and a private behind-the-scenes channel.

Store the channel ID for each by right-clicking the channel, clicking details, and scrolling to the bottom to find it.

Add any help team members, and your Slack bot, to all of these channels.
### usage
1. Download the script: `wget https://raw.githubusercontent.com/duckida/quick-nephthys/refs/heads/main/main.py`
2. Run the script and follow the prompts! `python3 main.py`
