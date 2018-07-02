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
    print("Logged in as AllPositiveHamutaro")
    print(client.user.name)
    print(client.user.id)
    print("--------")


#メッセージを受け取り検査
@client.event
async def on_message(msg):
    if client.user != msg.author:
        if "ハム太郎" in msg.content and "お前もそう思う" in msg.content:
            print("HamutaroRecognition:" + msg.content)
            m = "そうなのだ！！！！！！！！！！！！！！！まったくもってその通りなのだ！！！！！！！！！！"
            print("Say:" + m)
            await client.send_message(msg.channel, m)

## コンフィグ情報の読み込み ##
inifile.read("../config.ini", "UTF-8")
print(inifile.get("hamutaro", "token"))
client.run(inifile.get("account", "token"))
