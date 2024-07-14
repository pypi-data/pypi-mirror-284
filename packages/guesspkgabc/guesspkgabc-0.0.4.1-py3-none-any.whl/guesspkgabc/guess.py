from random import randint

from pyrogram import Client

from pyrogram.types import Message

async def guess(c: Client, m: Message):    
    n = randint(1,100)
    a = -1

    guesses = 0

    while a != n:
        a = await c.ask(m.chat.id, text="guess the number :")
        a = int(a.text)
        if(a>n):
            await m.reply("lower number please")
            guesses += 1

        elif(a<n):
            await m.reply("higher number please")
            guesses += 1

    await m.reply(f" you have guessed the number {n} correctly in {guesses} attempt")