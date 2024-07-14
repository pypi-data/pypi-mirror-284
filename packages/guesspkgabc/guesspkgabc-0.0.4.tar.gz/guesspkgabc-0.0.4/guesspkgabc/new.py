from random import randint
n = randint(1,100)
a = -1

guesses = 0

while a != n:
    a = await client.ask(message.chat.id, text = "guss the number : ")
    a = int(a.text)
    if(a>n):
        await message.reply("lower number please")
        guesses += 1

    elif(a<n):
        await message.reply("higher number please")
        guesses += 1

print(f"you have guess the number {n} correctly in {guesses} attempt")