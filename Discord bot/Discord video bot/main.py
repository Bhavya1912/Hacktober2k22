import os
from time import sleep

import discord
import pyperclip
from dotenv import load_dotenv
from pyautogui import hotkey, press
from youtubesearchpython import SearchVideos

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX')
USER_ID = os.getenv('DISCORD_USER_ID')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user \
            or len(message.content) < 2 \
            or PREFIX is not message.content[0]:
        return

    connected = message.author.voice

    if connected:
        channel = await client.fetch_channel(connected.channel.id)
        if int(USER_ID) in channel.voice_states:
            if not channel.voice_states[int(USER_ID)].self_stream:
                await message.channel.send('Player is not streaming')
                return
        else:
            await message.channel.send('Player is not connected to the voice channel')
            return
    else:
        await message.channel.send('You are not connected to any voice channel')
        return

    command = message.content[1]

    if command == 'p':
        if len(message.content) == 2:
            await pause_play(message.channel)
        elif len(message.content) < 4 or message.content[2] != ' ':
            return
        else:
            await search_video(message.channel, message.content[3:])
    elif command == 's':
        skip()
        await message.channel.send('Skipped')
    elif command == 'l' and len(message.content) > 3:
        play(message.content[3:])
    else:
        return


async def search_video(channel, search):
    search = SearchVideos(search, offset=1, mode="list", max_results=1)

    if len(search.result()) != 1:
        await channel.send('Unable to find any Video')
    else:
        await channel.send('Playing ' + search.result()[0][2])
        play(search.result()[0][2])


def play(url):
    pyperclip.copy(url)
    press('f')
    sleep(1)
    hotkey('ctrl', 'l')
    sleep(1)
    hotkey('ctrl', 'v')
    sleep(1)
    press('enter')
    sleep(15)
    press('f')


def skip():
    hotkey('shift', 'n')


async def pause_play(channel):
    press('space')
    await channel.send('Video Paused/Play')


client.run(TOKEN)
