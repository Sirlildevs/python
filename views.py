from discord import Client, Intents
from discord.ext import commands
from discord.utils import get
import discord





class rolesview(discord.ui.View):
    embed = discord.Embed()
    embed.title = "Role Request"
    embed.set_author(name="Fur & Foliage Retreat")
    embed.description = "Please select the roles you want!"


    @discord.ui.button(label="nsfw access", style=discord.ButtonStyle.red)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.button):
        role1 = interaction.guild.get_role(1206037029591195750)
       
        
        await interaction.user.add_roles(role1)
        await interaction.response.send_message(f"You have been given the {role1.mention}")



    @discord.ui.button(label="Lost and Found", style=discord.ButtonStyle.green)
    async def callback2(self, interaction: discord.Interaction, button: discord.ui.button):
        role2 = interaction.guild.get_role(1211345861280276510)
       
        
        await interaction.user.add_roles(role2)
        await interaction.response.send_message(f"You have been given the {role2.mention}")



    @discord.ui.button(label="polls", style=discord.ButtonStyle.blurple)
    async def callback3(self, interaction: discord.Interaction, button: discord.ui.button):
        role3 = interaction.guild.get_role(1209598488812331080)
       
        
        await interaction.user.add_roles(role3)
        await interaction.response.send_message(f"You have been given the {role3.mention}")



    @discord.ui.button(label="Gorepost Access", style=discord.ButtonStyle.danger)
    async def callback4(self, interaction: discord.Interaction, button: discord.ui.button):
        role4 = interaction.guild.get_role(1206386593083166720)
       
        
        await interaction.user.add_roles(role4)
        await interaction.response.send_message(f"You have been given the {role4.mention}")