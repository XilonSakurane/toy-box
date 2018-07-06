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
            randNum = random.randrange(100)
            if randNum <= 5:
                m = "は？"
            elif randNum == 6:
                m = "何を言ってるのだ？"
            elif randNum == 7:
                m = "なんでも肯定するからといって調子乗らないほうがいいのだ"
            elif randNum == 8:
                m = "少しは自分の行いを見つめなおした方がいいのだ"
            elif randNum == 9:
                m = "ふざけるのも程々にしてほしいのだ"
            else:
                m = "そうなのだ！！！！！！！！！！！！！！！まったくもってその通りなのだ！！！！！！！！！！"

            print("randNum:" + str(randNum))
            print("Say:" + m)
            await client.send_message(msg.channel, m)
        if "ハム太郎" in msg.content and "ダイス" in msg.content:
            randNum = str(random.randrange(6) + 1)
            await client.send_message(msg.channel, randNum + "が出たのだ")

## コンフィグ情報の読み込み ##
inifile.read("../config.ini", "UTF-8")
print(inifile.get("hamutaro", "token"))
client.run(inifile.get("hamutaro", "token"))
