import discord
from discord.ext.commands import Bot
import platform
from PIL import Image
import requests
import asyncio
import time

# Description is the description of the bot, command_prefix is... the command prefix and pm_help is whether the help
# message should be send to PMs or not
client = Bot(description="Spammy boi", command_prefix="commy!", pm_help=False)
client.remove_command('help')
# Version of the bot. Just used for little aesthetics
botVersion = "0.1.0"


# some top level vars
replacementActive = True
deletingNextMemer = False


# top level lists
propertyWords = [['property', 'property'], ['belongs', 'belonging'], ['belonging', 'belonging'], ['dominion', 'dominion'], ['ownership', 'ownership'], ['owns', 'ownership'],
                 ['possesion', 'possesion'], ['possess', 'possession']]
DankMemeRepellant = ['kill', 'takecareof', 'murder']

# just some general information printed to console on startup. Mainly the login ID, server count, discord package
# version and python version.
@client.event
async def on_ready():
    global botVersion

    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
            len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {} | Bot Version: {}'.format(discord.__version__,
                                                                                                 platform.python_version
                                                                                                 (), botVersion))
    print('--------')
    return await client.change_presence(
        game=discord.Game(name='with the communist manifesto'))


@client.event
async def on_message(message):
    global deletingNextMemer

    await client.process_commands(message)

    if deletingNextMemer and message.author.name == 'Dank Memer':
        deletingNextMemer = False
        await client.delete_message(message)
        await client.send_message(message.channel, "shut up Dank Memer, your words can't harm the communists you captialist scum!");

    elif replacementActive and str(message.author) != 'Our bot#1432':
        newMessage = message.content.lower()
        if 'pls' in message.content:
            for i in DankMemeRepellant:
                if i in message.content:
                    if message.mentions[0].name == 'Our bot':
                        deletingNextMemer = True
        else:
            for i in propertyWords:
                if i[0] not in newMessage:
                    newMessage = ' ' + newMessage + ' '
                    newMessage = newMessage.replace(' mine ', ' ours ')
                    newMessage = newMessage.replace(' your ', ' our ')
                    newMessage = newMessage.replace(' yours ', ' ours ')
                    newMessage = newMessage.replace(' you\'re ', ' we are ')
                    newMessage = newMessage.replace(' you ', ' we ')
                    newMessage = newMessage.replace(' im ', ' were ')
                    newMessage = newMessage.replace(' i\'m ', ' we\'re ')
                    newMessage = newMessage.replace(' i am ', ' we are ')
                    newMessage = newMessage.replace(' i will ', ' we will ')
                    newMessage = newMessage.replace(' imma ', ' we\'re gonna ')
                    newMessage = newMessage.replace(' i ', ' we ')
                    newMessage = newMessage.replace(' my ', ' our ')
                    newMessage = newMessage.replace(' ', '', 1)
                    newMessage = newMessage[:-1]

                    if newMessage != message.content.lower():
                        newMessage = "**We think {} meant to say**   ".format(message.author.name) + newMessage
                        await client.send_message(message.channel, newMessage)
                        break

                else:

                    await client.send_message(message.channel, 'Fuck you, its **our** {}.'.format(i[1]))
                    break



@client.command(pass_context = True)
async def CommyGrammar(ctx):
    global replacementActive

    if replacementActive:
        replacementActive = False
        await client.send_message(ctx.message.channel, "I will no longer correct you, capitalist scum!")
    else:
        replacementActive = True
        await client.send_message(ctx.message.channel, "I will correct you again comrade.")


@client.command(pass_context=True)
async def gulag(ctx):
    try:
        user = ctx.message.mentions[0]
        userPP = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        img_data = requests.get(userPP).content
        with open('Images/fromCommands/userPP.png', 'wb') as handler:
            handler.write(img_data)
        profilePic = Image.open('Images/fromCommands/userPP.png').convert('LA').convert('RGBA')
        gulagPic = Image.open('Images/gulag.jpg')

        profilePic.thumbnail([68, 68])
        gulagPic.paste(profilePic, [254, 150], mask=profilePic)
        gulagPic.save('Images/fromCommands/GulagCommand.jpg')

        await client.send_message(ctx.message.channel, 'To the gulag with you, {}!'.format(ctx.message.mentions[0].name))
        await client.send_file(ctx.message.channel, 'Images/fromCommands/GulagCommand.jpg')
    except IndexError:
        try:
            link = ctx.message.content.replace('commy!gulag ', '')
            img_data = requests.get(link).content
            with open('Images/fromCommands/userPP.png', 'wb') as handler:
                handler.write(img_data)
            profilePic = Image.open('Images/fromCommands/userPP.png').convert('LA').convert('RGBA')
            gulagPic = Image.open('Images/gulag.jpg')

            profilePic.thumbnail([68, 68])
            gulagPic.paste(profilePic, [254, 150], mask=profilePic)
            gulagPic.save('Images/fromCommands/GulagCommand.jpg')

            await client.send_message(ctx.message.channel, 'To the gulag with you!')
            await client.send_file(ctx.message.channel, 'Images/fromCommands/GulagCommand.jpg')
        except requests.exceptions.MissingSchema:
            await client.send_message(ctx.message.channel, 'Please specify a user or link comrade!')


@client.command(pass_context=True)
async def stalin(ctx):
    try:
        user = ctx.message.mentions[0]
        userPP = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        img_data = requests.get(userPP).content
        with open('Images/fromCommands/userPP.png', 'wb') as handler:
            handler.write(img_data)
        profilePic = Image.open('Images/fromCommands/userPP.png').convert('LA').convert('RGBA')
        stalinPic = Image.open('Images/stalin.jpg')

        profilePic.thumbnail([86, 86])
        stalinPic.paste(profilePic, [52, 55], mask=profilePic)
        stalinPic.save('Images/fromCommands/StalinCommand.jpg')

        if ctx.message.mentions[0].name == 'Thomas288':
            await client.send_message(ctx.message.channel, 'Look, it is great communist leader!')
        elif ctx.message.mentions[0].name == 'Our bot':
            await client.send_message(ctx.message.channel, 'Look who is great leader now... Hey its me!')
        else:
            await client.send_message(ctx.message.channel, 'Look who is great leader now... Fake!')
        await client.send_file(ctx.message.channel, 'Images/fromCommands/StalinCommand.jpg')
    except IndexError:
        try:
            link = ctx.message.content.replace('commy!stalin ', '')
            img_data = requests.get(link).content
            with open('Images/fromCommands/userPP.png', 'wb') as handler:
                handler.write(img_data)
            profilePic = Image.open('Images/fromCommands/userPP.png').convert('LA').convert('RGBA')
            stalinPic = Image.open('Images/stalin.jpg')

            profilePic.thumbnail([86, 86])
            stalinPic.paste(profilePic, [52, 55], mask=profilePic)
            stalinPic.save('Images/fromCommands/StalinCommand.jpg')

            await client.send_message(ctx.message.channel, 'Look who is great leader now... Fake!')
            await client.send_file(ctx.message.channel, 'Images/fromCommands/StalinCommand.jpg')
        except requests.exceptions.MissingSchema:
            await client.send_message(ctx.message.channel, 'Please specify a user or link comrade!')


@client.command(pass_context=True)
async def anthem(ctx):
    try:
        channel = ctx.message.author.voice.voice_channel
        voice = await client.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('Audio/anthem.mp3')
        player.volume = 0.3
        player.start()
        await asyncio.sleep(226)
        await voice.disconnect()
    except discord.errors.InvalidArgument:
        await client.send_message(ctx.message.channel, 'I need you to be in a channel comrade.')
    except discord.errors.ClientException:
        await client.send_message(ctx.message.channel, 'I only have one voice, capitalist pig!')


client.run('NDQxNzQwMTc3MzU1MDQ2OTIz.Dc0tgA.Vh3eVXDmjk6Zwwk2k1x0KaaVFbY')