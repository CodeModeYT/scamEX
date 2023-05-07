from dotenv import load_dotenv
import os
import discord
from discord import app_commands
import random

# Startup
load_dotenv()
token = os.getenv("TOKEN")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
report_channel = client.get_channel(1104404031713054730)


@tree.command(name = "checkserver", description = "Check if a Server is registered at scamEX by ID", guild=discord.Object(id=969274610275192882)) 
async def checkserver(interaction, server_id: int):
    print(f"Getting data for Server {server_id}")
    await interaction.channel.send(f"Checked the Server with the ID: {server_id}")


@tree.command(name="usercheck", description = "Check if a user is registered at scamEX by ID", guild=discord.Object(id=969274610275192882))
async def checkuser(interaction, server_id: int):
    print(f"Getting data for user {server_id}")
    await interaction.channel.send(f"Checked User with {server_id}")

@tree.command(name="serverreport", description="Report a user to scamEX", guild=discord.Object(id=969274610275192882))
async def serverreport(interaction, server_id: int, reason: str, invite: str):
    reported_server_id=server_id
    reported_reason=reason
    reported_server_invite=invite
    await interaction.channel.send(f"Thanks for your report, we will check it and get back to you! You can report again in 24h")
    embedVar = discord.Embed(title="Server Report - soon", description="Desc", color=0x00ff00)
    embedVar.add_field(name="User information", value=f"Username: \n User-ID:", inline=False)
    embedVar.add_field(name="Server information", value=f"Server-ID: {reported_server_id} \n Reason: {reported_reason} \n Server invie: {reported_server_invite}", inline=False)
    channel = client.get_channel(1104404031713054730)
    await channel.send(embed=embedVar)
    print("Got a new Report with report-ID = soon")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=969274610275192882))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="out for scams"))
    print("Logged in")

client.run(token)
