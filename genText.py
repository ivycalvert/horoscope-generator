import json
import random
import os
import tracery
from random import randint
from tracery.modifiers import base_english

# put your grammar here as the value assigned to "rules"
# "origin" to have enough sentence options to create variance in the generated content
rules = {
    "about":["STAR SIGN: #star.capitalize#. #star# have very #adj# personalities, due to this you should aspire #to_do#."],
    "description": ["#[star:#sign#]about#"],
    "origin":
        ["#happening.capitalize# will occur in #setting# however, you should be open minded to new occurances and embrace the events happening around you.", 
        "You should be feeling #opt# about these events.", 
        "This month #objective.a# #character# will enter your life, bringing with them an omen fortelling #omen#.",
        "Don't be so #objective# when you meet #character.s#, but rather embrace the opportunity to grow.",
        "Too much stress from #event# could have you feeling #objective#, don't be afraid to relax.",
        "You have been dreaming of taking a trip away, #place# will offer the soulsearching you require.",
        "You're less likely to forget anything if you stay #objective#.",
        "Your current state of mind could result in #measure# love decisions this month.",
        "#quote#",
        "You have energy to spare this month, be #objective# and use your time wisely.",
        "Go for it."] ,
    "to_do": ["take chances" , "explore new things" , "venture outside your comfort zone" , "embrace the difference others have to offer" ],
    "set_sign": ["#[personality:#sign.capitalize#]#"],
    "adjective": ["mysterious", "noble", "enigmatic"] ,
    "origin2": "Your gemstone is #gemstone#." ,
    "origin3": "Your lucky colour is #colour#.",
    "measure": ["good", "bad", "questionable", "disasterous", "profitable", "drastic", "positive", "negative"],
    "month": ["Jan - Feb", "Feb - Mar", "Mar - Apr", "Apr - May", "May - Jun", "Jun - Jul", "Jul - Aug", "Aug - Sep", "Sep - Oct", "Oct - Nov", "Nov - Dec", "Dec - Jan"]
}

# load in the json data from files downloaded from corpora project
event_data = json.loads(open("event.json").read())
colour = json.loads(open("crayola.json").read())
stone = json.loads(open("gemstones.json").read())
opt = json.loads(open("encouraging_words.json").read())
star_sign = json.loads(open("wrestlers.json").read())
mood = json.loads(open("moods.json").read())
country = json.loads(open("countries.json").read())
quote = json.loads(open("oprahQuotes.json").read())
adj = json.loads(open("adjs.json").read())


# set values for the variables data from downloaded files
rules["happening"] = ["arrival", "departure", "giving", "recieving", "loss", "victory", "defeat", "ritual", "rebirth", "healing"]
rules["character"] = ["hero", "anti-hero", "caretaker", "coward" , "mentor", "fool", "trickster", "child", "wanderer", "hermit", "dreamer", "leader", "tyrant", "temptress"]
rules["setting"] = ["shop", "bridge", "office","road","crossroads","forest","garden"]
rules["colour"] = ["Aquamarine", "Black", "blush", "brown", "blue", "orange", "eggplant", "green", "gray", "yellow", "indigo", "lavender", "maroon", "melon", "peach", "plum", "tan", "tangerine"]
rules["gemstone"] = stone["gemstones"]
rules["opt"] = opt["encouraging_words"]
rules["omen"] = ["good will" , "misfortune" , "bad luck" , "love" , "prosperity" , "good fortune"]
rules["sign"] = star_sign["wrestlers"]
rules["objective"] = mood["moods"]
rules["event"] = ["work", "your love life", "family", "friends", "peer pressure", "talking to your boss", "seeing an ex", "pressing assignments", "not enough sleep", "eating poorly", "breaking out"]
rules["place"] = country["countries"]
rules["quote"] = quote["oprahQuotes"]
rules["adj"] = adj["adjs"]


grammar = tracery.Grammar(rules) # create a grammar object from the rules
grammar.add_modifiers(base_english) # add pre-programmed modifiers

#create fictional star sign details 
randNum = str(randint(19, 23)) + " - " + str(randint(19, 23))
print("MONTH: ", grammar.flatten("#month#"))
print("DATES: ", randNum)
print("STONE: ", grammar.flatten("#origin2#"))
print(grammar.flatten("#description#"))


# create the sentences for each month
for i in range(12):
    print("YOUR HOROSCOPE THIS MONTH:")
    for i in range(3):
        print(grammar.flatten("#origin#"))
    print("LUCKY COLOUR THIS MONTH IS:", grammar.flatten("#colour#"))
    print("YOUR LUCKY NUMBERS THIS MONTH ARE: ")
    for i in range(5):
        randLuck = str(randint(1,99))
        print(randLuck)