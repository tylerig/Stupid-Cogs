import discord
from discord.ext import commands
from random import choice as randchoice

class goosefacts:

    def __init__(self, bot):
        self.bot = bot

        self.facts = ["Some geese migrate every year. Others stay in the same place year round.", 
                "Geese eat seeds, nuts, grass, plants and berries. They love blueberries.",
                "Geese can live almost anywhere. They like fields, parks and grassy areas near water.", 
                "Geese fly in a “V” formation. If one goose is injured, other geese will stay with it until it dies or can rejoin the flock.",
                "Geese are sometimes raised like chickens for their meat or eggs.", 
                "Male geese protect the nest while the female geese sit on the eggs.", 
                "Life spans of 15to 25 years!", 
                "21.7 inches to 43.3 inches in legnth!",
                "There are around 30 species of goose in the world.", 
                "Geese vocalise their messages in ten different ways, depending upon the situation. And in a threatening situation, geese stretch out their necks and make loud honks." ,
                "A day old gosling is capable of diving and swimming as much as 30 to 40 feet underwater. Attaining the age of three months, goslings begin to fly.",
                "Geese were probably the first type of poultry domesticated by humans, over 3000 years ago in Egypt.",
                "In another surprising historical use of geese, the first golf balls were stuffed with goose feathers. These balls were handmade and extremely expensive.",
                "Geese are excellent weeders and during the early days of commercial agriculture goose farmers would supplement their income by renting flocks out to cotton farms for a chemical-free weeding solution.",
                "In Victorian England geese were a regular companion of the chimney sweep. A goose would be sent down the chimney to collect the built up coal, coming out the other end black with soot."]

    @commands.command()
    async def goosefact(self):
        await self.bot.say(randchoice(self.facts))


def setup(bot):
    bot.add_cog(goosefacts(bot))