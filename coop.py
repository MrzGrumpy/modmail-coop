@client.event
@bot.listen()
async def on_message(message):
   if message.author == client.user:
        return

   if message.content.startswith('!help'):
        await message.channel.send("{message.author.mention} needs help with {message.content}.")