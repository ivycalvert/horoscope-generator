import json
import random
import os
import tracery
from random import randint
from tracery.modifiers import base_english

with open('animals.json') as json_data:
    animals_data = json.load(json_data)

chosen_animal = random.choice(animals_data["animals"])

print("Using animal {}".format(chosen_animal))

# scrape flickr for images
URL="https://www.flickr.com/photos/tags/{}/page{}".format(chosen_animal, 1)
os.system("bash collect.sh {}".format(URL))

# signal downloads have been completed
print("DOWNLOAD DONE")
