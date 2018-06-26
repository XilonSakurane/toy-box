import discord
import asyncio

"""hamutaro say 'affirmative'."""
def affirmation(msg, client):
        print("HamutaroRecognition:" + msg.content)
        m = "そうなのだ！！！！！！！！！！！！！！！まったくもってその通りなのだ！！！！！！！！！！"
        print("Say:" + m)
        return m
