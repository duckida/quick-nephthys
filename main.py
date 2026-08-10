import os
import shutil
import sys
from pathlib import Path

if shutil.which("uv") is not None:
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

# Slack details
program = input("What is your program ID? Examples: flavortown, hcai, stardance.")
program_name = input("What is your program display name? Examples: Flavortown, Hack Club AI, Outpost.")

owner = input("What is the program owner's Slack ID? (starts with U0...)?")

help_channel = input("What is your public-facing help channel ID? (starts with C0...)?")
help_channel = input("What is your private ticketing channel ID? (starts with C0...)?")
bts_channel = input("What is your private behind-the-scenes help channel ID? (starts with C0...)?")

faq_link = input("What is the link to your FAQ page?")

# Default strings
RESOLVE_BUTTON_DEFAULT = "i get it now!"
NEW_USER_DEFAULT = """hi (user), it looks like this is your first time here, welcome!
someone should be along to help you soon.
if your question has been answered, please hit the button below to mark it as resolved"""
TICKET_CREATE_DEFAULT = "if you haven't already, check out <{faq_link}|*the FAQ*> for commonly asked questions! otherwise, someone should be here to help you soon!"
TICKET_RESOLVE_DEFAULT = ":yay: this post has been marked as resolved by <@{{user_id}}>! if you have any more questions, please make a new post in <#{help_channel}> and we'll be happy to help you out!"
FAQ_MACRO_DEFAULT = "ooh, it looks like that question's answered in our FAQ! Have a look at <{faq_link}|*the FAQ*>"
NOT_ALLOWED_DEFAULT = "heya, it looks like you're not supposed to be in that channel, pls talk to <@{program_owner}> if that's wrong"

# Strings
resolve_ticket_button = input(f"What should the resolve button say? (default: {RESOLVE_BUTTON_DEFAULT})") or RESOLVE_BUTTON_DEFAULT

new_user_msg = input(f"What should the new user message say? (default: {NEW_USER_DEFAULT}") or NEW_USER_DEFAULT

ticket_create_msg = input(f"What should the ticket create message say? (default: {TICKET_CREATE_DEFAULT})") or TICKET_CREATE_DEFAULT
ticket_resolve_msg = input(f"What should the ticket resolved say? (default: {TICKET_RESOLVE_DEFAULT})") or TICKET_RESOLVE_DEFAULT

faq_macro = input(f"What should the FAQ macro (!faq) say? (default: {FAQ_MACRO_DEFAULT})") or FAQ_MACRO_DEFAULT

not_allowed_msg = input(f"What should the not allowed message say? (default: {NOT_ALLOWED_DEFAULT}") or NOT_ALLOWED_DEFAULT
