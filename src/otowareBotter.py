import discord
from discord.utils import get
import asyncio
import pdb
import configparser
import random
import time

inifile = configparser.ConfigParser()
client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as OtowareBotter")
    print(client.user.name)
    print(client.user.id)
    print("--------")

@client.event
async def on_message(msg):
    if client.user != msg.author:
        if "？？？？？" in msg.content or "?????" in msg.content:
            if not msg.author.voice_channel: # 発言者がVCチャンネルに存在していない
                await client.send_message(msg.channel, "？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？")
                return
            voice = await client.join_voice_channel(msg.author.voice_channel)
            player = voice.create_ffmpeg_player("../audio/otoware_potter.m4a")
            player.start()
            await client.send_message(msg.channel, "？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？")
            time.sleep(15)
            # 全VCチャンネルから切断？
            for x in client.voice_clients:
                await x.disconnect()


## コンフィグ情報の読み込み ##
inifile.read("../config.ini", "UTF-8")
print(inifile.get("otoware_botter", "token"))
client.run(inifile.get("otoware_botter", "token"))
