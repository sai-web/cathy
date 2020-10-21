import discord
import aiml
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if message.content.startswith('!ugay'):
            await message.channel.send('i sassy {0.author.mention}'.format(message))
        if message.content.startswith('-'):
            await message.channel.send(a.respond(message))
client = MyClient()
client.run('Njk4MjQ3NDUwNzAzNTYwNzM0.XpMNkQ.21jWi8_QmvzF6Hfec0fy-WA4BHw')