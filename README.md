# quick nephthys

A quick way to setup [Hack Club Nephthys](https://github.com/hackclub/nephthys), a Slack support bot for YSWSs and other programs!

Designed for Linux or macOS servers such as [Hack Club Nest](https://hackclub.app)! 

## how does this work?
quick nephthys is a python script which asks you questinos about your setup & program, and automatically configures Nephthys's transcripts, environment file, and installs everything!

## how can i use it?
### Prerequisites:
#### PostgreSQL database
Nephthys requires a PostgreSQL database to store tickets. An easy way to run one is using Docker.
1. Install Docker: https://docs.docker.com/engine/install/
2. Run a database: `docker run --name hh-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres`
3. Create the table: `docker exec -it hh psql -U postgres -c "CREATE DATABASE nephthys;"`
### Slack channels
Create a public-facing help channel, a private tickets channel, and a private behind-the-scenes channel.
Store the channel ID for each by right-clicking the channel, clicking details, and scrolling to the bottom to find it.
#### Slack API setup
A [video demo](https://user-cdn.hackclub-assets.com/019ff147-b57b-79d5-85f7-29e888509556/slack-api-setup-quick-nephthys.mp4) is available.

1. Go to https://api.slack.com/apps and click "Create New App".
2. Choose "From an app manifest" and select your workspace.
3. Copy and paste the manifest in the [Nephthys manifest.yml](https://github.com/hackclub/nephthys/blob/main/manifest.yml)
4. Review and create the app.
5. In Settings→Basic Information, scroll to Display Information and rename your bot
6. In Settings→Socket Mode, enable Socket Mode
7. Under Settings→Install app, install the app in your workspace
8. Store the User OAuth Token and Bot User OAuth Token
8. From Settings→Basic Information, retrieve and store the Signing Secret.
9. Scroll to App-Level Tokens and create one called Nephthys, and store this too
10. Add your bot to your help channel 

### usage
1. Download the script: `wget https://raw.githubusercontent.com/duckida/quick-nephthys/refs/heads/main/main.py`
2. Run the script and follow the prompts! `python3 main.py`
