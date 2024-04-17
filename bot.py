import discord 
from .responses import handle_response

async def send_message(message):
    try:

        response = handle_response(message)
        await message.channel.send(response)

    except Exception as e:
        print(e)

def run_bot():
    TOKEN = 'MTIzMDA3NTQ1ODc4MDAwODQ5OQ.Gy3OIj.Byg2Ub1p1mYolqWO3vOY2OBh2EcR5FTB-ST7iM'

    intents = discord.Intents.all()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running!")

    @client.event
    async def on_message(message):

        if len(message.mentions) > 0 and message.mentions[0].id == 1230075458780008499:
        
            username = str(message.author)
            user_message = message.clean_content
            channel = str(message.channel)

            print(f"{username} said: '{user_message}' ({channel})")

            await send_message(message)

    client.run(TOKEN)