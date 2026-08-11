# Constants
TRANSCRIPT_DEFAULT = '''
from nephthys.transcripts.transcript import Transcript

class F_CLASSNAME(Transcript):
    """Transcript for F_DISPLAYNAME"""

    program_name: str = "F_DISPLAYNAME"
    program_owner: str = "F_OWNER"

    help_channel: str = "F_HELP_CHANNEL"
    ticket_channel: str = "F_TICKET_CHANNEL"
    team_channel: str = "F_TEAM_CHANNEL"

    faq_link: str = "F_FAQ_LINK"
    resolve_ticket_button: str = "F_RESOLVE_BTN"

    first_ticket_create: str = """
    F_FIRST_TICKET
    """
    ticket_create: str = f"F_TICKET_CREATE"
    ticket_resolve: str = f"F_TICKET_RESOLVE"

    not_allowed_channel: str = f"F_NOT_ALLOWED"
    faq_macro: str = f"F_FAQ_MACRO"
'''

ENV_DEFAULT = '''
ENVIRONMENT="production"
PORT=3000
SLACK_BOT_TOKEN="F_SLACK_BOT_TOKEN"
SLACK_USER_TOKEN="F_SLACK_USER_TOKEN"
SLACK_APP_TOKEN="F_SLACK_APP_TOKEN"
SLACK_SIGNING_SECRET="F_SLACK_SIGNING_TOKEN"
SLACK_HEARTBEAT_CHANNEL=""
SLACK_TICKET_CHANNEL="F_TICKET_CHANNEL"
SLACK_BTS_CHANNEL="F_TEAM_CHANNEL"
SLACK_HELP_CHANNEL="F_HELP_CHANNEL"
SLACK_MAINTAINER_ID="F_OWNER"
DATABASE_URL="F_DATABASE_URL"
PROGRAM="F_CODENAME"
BASE_URL="F_BASEURL"
APP_TITLE="F_BOTNAME"
HACK_CLUB_AI_API_KEY=""
'''

# Default strings
RESOLVE_BUTTON_DEFAULT = "i get it now!"
NEW_USER_DEFAULT = """hi (user), it looks like this is your first time here, welcome!
someone should be along to help you soon.
if your question has been answered, please hit the button below to mark it as resolved"""
TICKET_CREATE_DEFAULT = "if you haven't already, check out <{faq_link}|*the FAQ*> for commonly asked questions! otherwise, someone should be here to help you soon!"
TICKET_RESOLVE_DEFAULT = ":yay: this post has been marked as resolved by <@{{user_id}}>! if you have any more questions, please make a new post in <#{help_channel}> and we'll be happy to help you out!"
FAQ_MACRO_DEFAULT = "ooh, it looks like that question's answered in our FAQ! Have a look at <{faq_link}|*the FAQ*>"
NOT_ALLOWED_DEFAULT = "heya, it looks like you're not supposed to be in that channel, pls talk to <@{program_owner}> if that's wrong"

# Imports

import os
import shutil
import sys
from pathlib import Path

print(r"""
    _   __           __    __  __
   / | / /__  ____  / /_  / /_/ /_  __  _______
  /  |/ / _ \/ __ \/ __ \/ __/ __ \/ / / / ___/
 / /|  /  __/ /_/ / / / / /_/ / / / /_/ (__  )
/_/ |_/\___/ .___/_/ /_/\__/_/ /_/\__, /____/
          /_/                    /____/
          """)

# Checking uv and Nephthys installation
if shutil.which("uv") is None:
    print("uv is required to use Nephthys. Please install uv.")
    sys.exit()

nephthys_path = Path("nephthys")

if not nephthys_path.is_dir(): # nephthys not installed
    print("Downloading nephthys...")
    os.system("git clone https://github.com/hackclub/nephthys")
else:
    print("Using pre-installed nephthys folder")

os.chdir('nephthys')

# Prerequesites
print("""
Before starting Nephthys setup, you must have the following:
- A Slack API bot setup with a bot token, app token, user token, & signing secret
- A public-facing help channel, a private tickets channel, and a private behind-the-scenes channel
- Your Slack bot added to all those channels
- A PostgreSQL database to store tickets

To set these up, read the guide in the quick-nephthys repo.
""")

input("Press enter once you have set these up.")

# Question time

# Env details
print("\nNephthys will be setup on port 3000, this must be exposed to the internet. If using Nest, you can reverse proxy this to a URL.")
base_url = input("What is the base URL you will expose? Must start with https://\n")

database_url = input("What is your database URL? (example: postgresql://postgres:postgres@localhost:5432/nephthys)\n")

# Slack bot
signing_secret = input("What is your Slack Bot signing secret?\n")
app_token = input("What is your Slack Bot app token (starts with xapp-)?\n")
user_token = input("What is your Slack Bot user token (starts with xoxp-)?\n")
bot_token = input("What is your Slack Bot bot token (starts with xoxb-)?\n")


# Program details
program_codename = input("What is your one-word program ID? Examples: flavortown, hcai, stardance.\n")
program_name = input("What is your program display name? Examples: Flavortown, Hack Club AI, Outpost.\n")
helpbot_name = input("What is your help bot's name? Examples: Helper Heidi, orphAIus.\n")

owner = input("What is the program owner's Slack ID? (starts with U0...)?\n")

help_channel = input("What is your public-facing help channel ID? (starts with C0...)?\n")
ticket_channel = input("What is your private ticketing channel ID? (starts with C0...)?\n")
bts_channel = input("What is your private behind-the-scenes help channel ID? (starts with C0...)?\n")

faq_link = input("What is the link to your FAQ page?\n")

# Strings
resolve_ticket_button = input(f"What should the resolve button say? (default: {RESOLVE_BUTTON_DEFAULT})\n") or RESOLVE_BUTTON_DEFAULT

new_user_msg = input(f"What should the new user message say? (default: {NEW_USER_DEFAULT}\n") or NEW_USER_DEFAULT

ticket_create_msg = input(f"What should the ticket create message say? (default: {TICKET_CREATE_DEFAULT})\n") or TICKET_CREATE_DEFAULT
ticket_resolve_msg = input(f"What should the ticket resolved say? (default: {TICKET_RESOLVE_DEFAULT})\n") or TICKET_RESOLVE_DEFAULT

faq_macro = input(f"What should the FAQ macro (!faq) say? (default: {FAQ_MACRO_DEFAULT})\n") or FAQ_MACRO_DEFAULT

not_allowed_msg = input(f"What should the not allowed message say? (default: {NOT_ALLOWED_DEFAULT}\n") or NOT_ALLOWED_DEFAULT

## todo: write to transcript, write to transcript init, setup .env, postgres, uv stuff, venv, run, systemd

# write to .env
print("Writing .env")
env_content = (
    ENV_DEFAULT
    .replace("F_SLACK_BOT_TOKEN", bot_token)
    .replace("F_SLACK_APP_TOKEN", app_token)
    .replace("F_SLACK_USER_TOKEN", user_token)
    .replace("F_SLACK_SIGNING_TOKEN", signing_secret)
    .replace("F_TICKET_CHANNEL", ticket_channel)
    .replace("F_TEAM_CHANNEL", bts_channel)
    .replace("F_HELP_CHANNEL", help_channel)
    .replace("F_OWNER", owner)
    .replace("F_DATABASE_URL", database_url)
    .replace("F_CODENAME", program_codename)
    .replace("F_BASEURL", base_url)
    .replace("F_BOTNAME", helpbot_name)
)

with open(".env", "w", encoding="utf-8") as f:
    f.write(env_content)

# Write transcript
print("Writing transcript")
class_name = program_codename.capitalize()

transcripts_path = Path("nephthys/transcripts/transcripts")
transcript_file_path = transcripts_path / f"{program_codename}.py"

transcript_content = (
    TRANSCRIPT_DEFAULT
    .replace("F_CLASSNAME", class_name)
    .replace("F_DISPLAYNAME", program_name)
    .replace("F_OWNER", owner)
    .replace("F_HELP_CHANNEL", help_channel)
    .replace("F_TICKET_CHANNEL", ticket_channel)
    .replace("F_TEAM_CHANNEL", bts_channel)
    .replace("F_FAQ_LINK", faq_link)
    .replace("F_RESOLVE_BTN", resolve_ticket_button)
    .replace("F_FIRST_TICKET", new_user_msg.strip())
    .replace("F_TICKET_CREATE", ticket_create_msg)
    .replace("F_TICKET_RESOLVE", ticket_resolve_msg)
    .replace("F_NOT_ALLOWED", not_allowed_msg)
    .replace("F_FAQ_MACRO", faq_macro)
)

transcript_file_path.write_text(transcript_content, encoding="utf-8")

# write to transcripts __init__.py
print("Updatign transcript imports")
init_path = Path("nephthys/transcripts/__init__.py")
init_content = init_path.read_text()

import_line = f"from nephthys.transcripts.transcripts.{program_codename} import {class_name}"

init_content = init_content.replace(
"from nephthys.transcripts.transcript import Transcript",
f"from nephthys.transcripts.transcript import Transcript\n{import_line}"
)

init_content = init_content.replace(
"transcripts: List[Type[Transcript]] = [",
f"transcripts: List[Type[Transcript]] = [\n    {class_name},"
)

init_path.write_text(init_content, encoding="utf-8")

print("Configuration done!")

# uv stuff
print("Installing packages...")
os.system("uv sync")
print("Activating venv...")
os.system("source .venv/bin/activate")
os.system("uv run pre-commit install")

print("Running database migrations & setup...")
os.system(f'DATABASE_URL="{database_url}" piccolo migrations forwards nephthys'
)

print("Nephthys is now ready! To use it, run `nephthys`")
