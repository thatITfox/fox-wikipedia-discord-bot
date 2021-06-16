import discord
from discord.ext import commands
import wikipedia


class wiki_search(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("fox bot is ready")

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send("```hi there, my name is fox bot the friendly furry wikipedia bot \n"
                               "my commands are:\n"
                               "foxsearch (insert language) (insert search)```")

    @commands.command()
    async def search(self, ctx, language, search):
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
                await ctx.channel.send(' '.join(minimize))
                await ctx.channel.send(f"to see the rest, see the page for this topic: {search_page.url}")
            else:
                await ctx.channel.send(' '.join(search_summary))
        except Exception as e:
            print("ERROR: sorry can't find the page for that")
            await ctx.channel.send("sorry, i can't find the page for that")
            await ctx.channel.send(search)


def setup(client):
    client.add_cog(wiki_search(client))
