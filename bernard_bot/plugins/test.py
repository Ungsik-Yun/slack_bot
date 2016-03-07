import re

from slackbot.bot import listen_to, respond_to


@respond_to("!test", re.IGNORECASE)
def test_func(msg):
    msg.reply("test successful!")
