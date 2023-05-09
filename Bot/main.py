from dotenv import load_dotenv
import os
import discord
from discord import app_commands
import datetime
import time

# Startup
load_dotenv()
token = os.getenv("TOKEN")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
report_channel = client.get_channel(1104404031713054730)


@tree.command(name = "checkserver", description = "Check if a Server is registered at scamEX by ID") 
async def checkserver(interaction, server_id: int):
    print(f"Getting data for Server {server_id}")
    await interaction.channel.send(f"Checked the Server with the ID: {server_id}")


@tree.command(name="usercheck", description = "Check if a user is registered at scamEX by ID")
async def checkuser(interaction, server_id: int):
    print(f"Getting data for user {server_id}")
    await interaction.channel.send(f"Checked User with {server_id}")

@tree.command(name="serverreport", description="Report a server to scamEX")
async def serverreport(interaction, server_id: int, reason: str, invite: str):
    reported_server_id=server_id
    reported_reason=reason
    reported_server_invite=invite
    interaction_user = interaction.user
    username = interaction_user.name
    user_id = interaction_user.id
    interaction_server = interaction.guild
    interaction_server_name = interaction_server.name
    interaction_server_id = interaction_server.id
    await interaction.channel.send(f"Thanks for your report, we will check it and get back to you! You can report again in 24h")
    embedVar = discord.Embed(title="Server Report", description="ID: soon", color=0x00ff00)
    embedVar.add_field(name="User information", value=f"Username: {username}\n User-ID: {user_id} \n from Server name: {interaction_server_name} \nfrom Server ID: {interaction_server_id}", inline=False)
    embedVar.add_field(name="Server information", value=f"Server-ID: {reported_server_id} \n Reason: {reported_reason} \n Server invite: {reported_server_invite}", inline=False)
    channel = client.get_channel(1104404031713054730)
    await channel.send(embed=embedVar)
    print("Got a new SERVER Report with report-ID = soon")
 
@tree.command(name="userreport", description="Report a user to scamEX")
async def serverreport(interaction, user_id: int, reason: str):
    reported_user_id=user_id
    reported_reason=reason
    interaction_user = interaction.user
    username = interaction_user.name
    user_id = interaction_user.id
    interaction_server = interaction.guild
    interaction_server_name = interaction_server.name
    interaction_server_id = interaction_server.id
    def create_discord_timestamp(target_time):
        unix_timestamp = int(target_time.timestamp())
        discord_timestamp = f"<t:{unix_timestamp}:R>"
        return discord_timestamp

    def create_future_timestamp():
        current_time = datetime.datetime.now()
        target_time = current_time + datetime.timedelta(hours=24)
        discord_timestamp = create_discord_timestamp(target_time)
        return discord_timestamp
    future_timestamp = create_future_timestamp()
    await interaction.response.send_message(f"Thanks for your report, we will check it and get back to you! You can report again {future_timestamp}", ephemeral=True)
    embedVar = discord.Embed(title="User Report", description="ID: soon", color=0x00ff00)
    embedVar.add_field(name="User information", value=f"Username: {username}\n User-ID: {user_id} \n from Server name: {interaction_server_name} \nfrom Server ID: {interaction_server_id}", inline=False)
    embedVar.add_field(name="Server information", value=f"Server-ID: {reported_user_id} \n Reason: {reported_reason}", inline=False)
    channel = client.get_channel(1104404031713054730)
    await channel.send(embed=embedVar)
    print("Got a new USER Report with report-ID = soon")
    time.sleep(24 * 60 * 60)
    await interaction.respo

# MOD - only commmands
@tree.command(name="addscam", description="MOD ONLY - Add a new scam to the system", guild=discord.Object(id=1057656714163404830))
async def addscam(interaction):
    await interaction.channel.send("Soon")

@client.event
async def on_ready():
    await tree.sync()
    guilds = len(client.guilds)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"out for scams on {guilds} servers"))
    print(f"Logged in on {guilds} guilds")

client.run(token)
