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

# Strings
resolve_ticket_button = input("What should the resolve button say? (default: i get it now!)") or "i get it now!"

new_user_msg = input("""What should the new user message say? (default: hi (user), it looks like this is your first time here, welcome!
someone should be along to help you soon.
if your question has been answered, please hit the button below to mark it as resolved)""") or """hi (user), it looks like this is your first time here, welcome!
someone should be along to help you soon.
if your question has been answered, please hit the button below to mark it as resolved"""

ticket_create_msg = input("What should the resolve button say? (default: i get it now!)") or "i get it now!"
ticket_resolve_msg = input("What should the resolve button say? (default: i get it now!)") or "i get it now!"

faq_macro = input("What should the FAQ macro (!faq) say? (default: ooh, it looks like that question's answered in our FAQ! Have a look at <{faq_link}|*the FAQ*>)") or "ooh, it looks like that question's answered in our FAQ! Have a look at <{faq_link}|*the FAQ*>"
