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
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")

#メッセージを受け取り検査
@client.event
async def on_message(msg):
    if client.user != msg.author:
        if "？？？？？" in msg.content or "?????" in msg.content:
            # 鯖独自の絵文字を使用してるため普通の鯖だと絶対例外すっとんでくる
            emoji1 = "smile" + str(random.randrange(4) + 1)
            emoji2 = "smile" + str(random.randrange(4) + 1)
            while emoji1 == emoji2:
                emoji2 = "smile" + str(random.randrange(4) + 1)

            e1 = get(client.get_all_emojis(), name = emoji1)
            e2 = get(client.get_all_emojis(), name = emoji2)
            await client.add_reaction(msg, e1)
            await client.add_reaction(msg, e2)
            print("AddReaction:" + emoji1 + ", " + emoji2)

## コンフィグ情報の読み込み ##
inifile.read("../config.ini", "UTF-8")
print(inifile.get("account", "token"))
client.run(inifile.get("account", "token"))
