import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()




BOT_TOKEN = os.getenv("TOKEN")

ROLE_NAME = os.getenv("ROLE")

intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен и готов к работе!")

@bot.event
async def on_member_join(member):
    guild = member.guild
    role = discord.utils.get(guild.roles, name=ROLE_NAME)

    if role:
        try:
            await member.add_roles(role)
            print(f"Роль '{ROLE_NAME}' выдана пользователю {member.name}.")
        except Exception as e:
            print(f"Не удалось выдать роль '{ROLE_NAME}' пользователю {member.name}: {e}")
    else:
        print(f"Роль '{ROLE_NAME}' не найдена на сервере {guild.name}.")

bot.run(BOT_TOKEN)
