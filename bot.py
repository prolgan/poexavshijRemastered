import discord

class MyBot(discord.Client):
    async def on_ready(self):
        print("Мое уважение")
    
    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))

bot = MyBot()
bot.run()