import discord
from discord.ext import commands
from random import choice as randchoice

class girafffefacts:

    def __init__(self, bot):
        self.bot = bot

        self.facts = ["Giraffes are the tallest mammals on Earth. Their legs alone are taller than many humans—about 6 feet.", 
                "They can run as fast as 35 miles an hour over short distances, or cruise at 10 mph over longer distances.",
                "A giraffe's neck is too short to reach the ground. As a result, it has to awkwardly spread its front legs or kneel to reach the ground for a drink of water.", 
                "Giraffes only need to drink once every few days. Most of their water comes from all the plants they eat.",
                "Giraffes spend most of their lives standing up; they even sleep and give birth standing up.", 
                "The giraffe calf can stand up and walk after about an hour and within a week, it starts to sample vegetation.", 
                "Despite the females’ attempts to stand over their calves during attacks by lions, spotted hyenas, leopards and African wild dogs (4), many calves are killed in their first few months.", 
                "A giraffe’s spots are much like human fingerprints. No two individual giraffes have exactly the same pattern.",
                "Both male and female giraffes have two distinct, hair-covered horns called ossicones. Male giraffes use their horns to sometimes fight with other males.", 
                "Giraffes only need 5 to 30 minutes of sleep in a 24-hour period! They often achieve that in quick naps that may last only a minute or two at a time." ,
                "Whilst it was thought that giraffes did not make any sounds, this is now known to be untrue, as giraffes bellow, snort, hiss and make flute-like sounds, as well as low pitch noises beyond the range of human hearing.",
                "No one has ever seen a giraffe swimming.",
                "Giraffes only need 5 to 30 minutes of sleep in a 24-hour period.",
                "Giraffes only need to drink once every few days. Most of their water comes from all the plants they eat.",
                "A giraffe's spots are like human fingerprints: no two individual giraffes have exactly the same pattern."]

    @commands.command()
    async def giraffefact(self):
        await self.bot.say(randchoice(self.facts))


def setup(bot):
    bot.add_cog(giraffefacts(bot))