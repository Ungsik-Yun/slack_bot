import re

from slackbot.bot import listen_to, respond_to


@respond_to("!test", re.IGNORECASE)
def roll_dice(msg):
    msg.reply("test successful!")
