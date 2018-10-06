from mastodon import Mastodon
import json
import string
import random

# Generate a random letter to select from the spells list
spell_initial = random.choice(string.ascii_letters).upper()

# Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

# Open JSON file to select spell to toot
with open('quotes.json') as json_file:
    data = json.load(json_file)

    # Get the amount of spells in the current section
    section_length = len(data['sections'][spell_initial])

    # Select random spell in section
    spell_index = random.randint(1, section_length)
    current_spell = data['sections'][spell_initial][spell_index]

    # Toot random spell
    mastodon.status_post(current_spell['key'] + ': ' + current_spell['val'])