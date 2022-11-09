import discord
import ugg

search_ugg = ugg.Ugg() # create an object for webscraping

no_result_message = 'Could not find what you are looking for. Try typing a champion\'s name'

def run_bot():
    TOKEN = 'INSERT-TOKEN-HERE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        # let it be known that the bot is online
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        # ignore message if it is sent by the bot
        if message.author == client.user:
            return
        message_content = message.content.lower() # lower case all user input

        if message_content.startswith(f'!help'):
            await message.channel.send('This bot lets you easily get champion guides, counters, and builds. Try it yourself! ex: !build twitch')

        if f'!build' in message_content: # if user types the !build command
            search_words = search_ugg.key_words(message_content) # call key_words
            result_links = search_ugg.search(search_words) # call search
            links = search_ugg.send_link(result_links, search_words) # call send_link

            if len(links) > 0: # if links are available, send them to the discord channel
                for link in links:
                    await message.channel.send(link)
            else: # else no result
                await message.channel.send(no_result_message)


    client.run(TOKEN) # run the bot with the token
