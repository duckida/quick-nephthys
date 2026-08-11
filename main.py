# Constants
TRANSCRIPT_DEFAULT =
'''
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
SLACK_SIGNING_SECRET="F_SLACK_SIGNING_TOKEN"
SLACK_HEARTBEAT_CHANNEL=""
SLACK_TICKET_CHANNEL="F_TICKET_CHANNEL"
SLACK_BTS_CHANNEL="F_TEAM_CHANNEL"
SLACK_HELP_CHANNEL="F_HELP_CHANNEL"
SLACK_MAINTAINER_ID="F_OWNER"
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/nephthys"
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

if shutil.which("uv") is None:
    print("uv is required to use Nephthys. Please install uv.")
    sys.exit()

nephthys_path = Path("nephthys")

if not nephthys_path.is_dir(): # nephthys not installed
    print("Downloading nephthys...")
    os.system("git clone https://github.com/hackclub/nephthys")
else:
    print("Using pre-installed nephthys folder")

print("Entering nephthys...")
os.chdir('nephthys')

# Env details
print("Nephthys will be setup on port 3000, this must be exposed to the internet. If using Nest, you can reverse proxy this to a URL.")
base_url = input("What is the base URL you will expose? Must start with https://")

# Slack details
program_codename = input("What is your program ID? Examples: flavortown, hcai, stardance.\n")
program_name = input("What is your program display name? Examples: Flavortown, Hack Club AI, Outpost.\n")

owner = input("What is the program owner's Slack ID? (starts with U0...)?\n")

help_channel = input("What is your public-facing help channel ID? (starts with C0...)?\n")
help_channel = input("What is your private ticketing channel ID? (starts with C0...)?\n")
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
