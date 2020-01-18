import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비완료!")
    game = discord.Game("!안녕")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
       await message.channel.send("안녕하십니까!")

    if message.content.startswith("!나"):
       await message.channel.send("당신은 나의 VVIP~")










client.run("NjY4MTYxNjc5NDM1MTA0MjU4.XiNQPg.dQnJI7-_Nlm_wfhpraluCiym6Ms")