import discord
import asyncio
import pdb
import hamutaro
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
        if "なあハム太郎" in msg.content and "お前もそう思う" in msg.content:
            m = hamutaro.affirmation(msg, client)
            await client.send_message(msg.channel, m)

## トークン情報を入力 ##
client.run("## insert token here ##")
