import discord
import asyncio
import pdb
import hamutaro
import configparser

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
        if "ハム太郎" in msg.content and "お前もそう思う" in msg.content:
            m = hamutaro.affirmation(msg, client)
            await client.send_message(msg.channel, m)

## コンフィグ情報の読み込み ##

inifile.read("../config.ini", "UTF-8")
print(inifile.get("account", "token"))
client.run(inifile.get("account", "token"))
