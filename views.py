from discord import Client, Intents
from discord.ext import commands
from discord.utils import get
import discord

class pingview(discord.ui.View):

    @discord.ui.select(
        placeholder="Who to ping?",
        options=[
            discord.SelectOption(label="Lucas", value="Lucas"),
            discord.SelectOption(label="UhOh_ICEY", value="UhOh_ICEY")
        ]
    )
    async def select_callback(self, interaction : discord.Interaction, select):
        if select.values[0] == "Lucas":
            
            await interaction.response.send_message("<@" + "479768035566288916" + ">")
        else:
            
            await interaction.response.send_message(f"<@" + "402142267051212802" + ">")

class rolesview(discord.ui.View):
    embed = discord.Embed()
    embed.title = "Role Request"
    embed.set_author(name="Fur & Foliage Retreat")
    embed.description = "Please select the roles you want!"


    @discord.ui.button(label="test1", style=discord.ButtonStyle.red)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.button):
        role1 = interaction.guild.get_role(1214332072940933170)
       
        
        await interaction.user.add_roles(role1)
        await interaction.response.send_message(f"You have been given the {role1.mention}")



    @discord.ui.button(label="test2", style=discord.ButtonStyle.green)
    async def callback2(self, interaction: discord.Interaction, button: discord.ui.button):
        role2 = interaction.guild.get_role(1214332105052659744)
       
        
        await interaction.user.add_roles(role2)
        await interaction.response.send_message(f"You have been given the {role2.mention}")



    @discord.ui.button(label="test3", style=discord.ButtonStyle.blurple)
    async def callback3(self, interaction: discord.Interaction, button: discord.ui.button):
        role3 = interaction.guild.get_role(1214332137055199284)
       
        
        await interaction.user.add_roles(role3)
        await interaction.response.send_message(f"You have been given the {role3.mention}")



    @discord.ui.button(label="test4", style=discord.ButtonStyle.danger)
    async def callback4(self, interaction: discord.Interaction, button: discord.ui.button):
        role4 = interaction.guild.get_role(1214332168822853723)
       
        
        await interaction.user.add_roles(role4)
        await interaction.response.send_message(f"You have been given the {role4.mention}")