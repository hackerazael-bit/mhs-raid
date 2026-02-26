#!/usr/bin/env python3
# mhs raid bot v5.5 - termux 100% fix
# criado por azael @_azaelx64

import discord
from discord.ext import commands
import asyncio
from colorama import init, Fore, Style
init(autoreset=True)

print(Fore.CYAN + """
██╗  ██╗ █████╗ ███╗   ███╗██████╗  ██████╗ ██╗
██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔═══██╗██║
███████║███████║██╔████╔██║██║  ██║██║   ██║██║
██╔══██║██╔══██║██║╚██╔╝██║██║  ██║██║   ██║██║
██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝
    mhs raid v5.5 - termux fix - criado por azael @_azaelx64
""")

# ═══════════════════════════════════════════════════════════════
import os
from dotenv import load_dotenv

load_dotenv()
# ═══════════════════════════════════════════════════════════════

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class spamButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(label="mhs", style=discord.ButtonStyle.red)
    async def mhs_raid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        spam_msg = """# servidor purificado pela mhs
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
mhs purificou seu servidor
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# servidor purificado pela mhs
СИСТЕМА ВЗЛОМАНА
mhs purificou seu servidor
# servidor purificado pela mhs
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
mhs purificou seu servidor
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# servidor purificado pela mhs
СИСТЕМА ВЗЛОМАНА
mhs purificou seu servidor
# servidor purificado pela mhs
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
mhs purificou seu servidor
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# servidor purificado pela mhs
СИСТЕМА ВЗЛОМАНА
mhs purificou seu servidor
|| @everyone ||
https://cdn.discordapp.com/attachments/1475302058914742364/1476630742397222933/aac6fef82d3a6edbd86ea5ac96a33a30.jpg?ex=69a1d30b&is=69a0818b&hm=e33c1fdbe2c232558fe9ac9c20ded06d47c03cd8012700ff39e4f8b4052e13d0&

https://discord.gg/m8EzwdSZmy"""

        print(Fore.YELLOW + "🚀 raid iniciado - 30 mensagens")
        for i in range(30):
            try:
                await interaction.followup.send(spam_msg)
                print(f"[{i+1}/30] ✅ enviada!")
                await asyncio.sleep(1.0)
            except Exception as e:
                print(f"[{i+1}/30] ❌ erro: {e}")
                await asyncio.sleep(1.0)
        
        print(Fore.GREEN + "🎉 mhs raid concluída!")

@bot.command()
async def mhs(ctx):
    """ativa o raid mhs"""
    view = spamButton()
    await ctx.send("clique para mhs", view=view)

@bot.tree.command(name="mhs", description="mhs raid by azael")
async def slash_mhs(interaction: discord.Interaction):
    view = spamButton()
    await interaction.response.send_message("clique para mhs", view=view, ephemeral=True)

@bot.event
async def on_ready():
    print(Fore.GREEN + f"✅ {bot.user} online no termux!")
    print(Fore.BLUE + "📱 slash: /mhs | prefix: !mhs")
    
    try:
        synced = await bot.tree.sync()
        print(Fore.GREEN + f"✅ {len(synced)} slash comandos sync")
    except Exception as e:
        print(f"⚠️ sync erro: {e}")

print(Fore.GREEN + "🚀 iniciando mhs raid...")
bot.run(os.getenv("TOKEN"))
