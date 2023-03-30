import discord
import os
import openai
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.all()
#intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='>', description="bad to the bone", intents=intents)

@bot.command(name='chat', description='prompt chatGPT')
async def chat_prompt(ctx, *, arg):
  print(arg)
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": arg}
      ],
    temperature=0.9,
    max_tokens=150
  )

  print(completion['choices'][0]['message']['content'])
  await ctx.send(completion['choices'][0]['message']['content'])

bot.run(bot_token)