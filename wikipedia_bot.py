import discord
from discord.ext import commands
import wikipedia

client = commands.Bot(command_prefix='fox', help_command=None)

@client.event
async def on_ready():
    print("fox bot is ready")

@client.command()
async def help(ctx):
    await ctx.channel.send("```hi there, my name is fox bot the friendly furry wikipedia bot \n"
                           "my commands are:\n"
                           "foxsearch (insert language) (insert search)```")

@client.command()
async def search(ctx, language, search):
    print("someone is searching")
    wikipedia.set_lang(language)
    try:
        searches = wikipedia.search(search)
        search_page = wikipedia.page(searches[0])
        print(searches)

        # this try and except block is use for finding the summary of every wikipedia pages
        try:
            search_summary = search_page.summary
        except:
            search_summary = wikipedia.summary(search_page)
        
        print(search_page)
        minimize = search_summary.split(' ')
        if len(minimize) > 200:
            print("minimizing")
            minimize = minimize[:199]
            message = discord.Embed(title=search_page.title, description=' '.join(minimize))
            await ctx.channel.send(message)
            await ctx.channel.send(f"to see the rest, see the page for this topic{search_page.url}")
        else:
            message = discord.Embed(title=search_page.title, description=search_summary)
            await ctx.channel.send(message)
    except Exception as e:
        print("ERROR: sorry can't find the page for that")
        await ctx.channel.send("sorry, i can't find the page for that")
        await ctx.channel.send(search)

client.run("bot id")
