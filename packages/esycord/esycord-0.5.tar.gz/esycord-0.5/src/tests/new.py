import lola
import discord
import time

client=lola.Bot('!', discord.Intents.all())

client.run('MTE2NDg1MzkxMjQyNDE2OTU1Mw.GPkmZG.JLjuJHAHQo5GacrsBeQRC7X5u-koo_gs3yW9Ng')


time.sleep(1)
client.set_bot_presence(state=discord.Status.do_not_disturb)