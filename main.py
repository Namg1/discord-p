# prefix: $
# example my message: $poll , are you a human , yes no


async def poll(ctx):
    p_polls = ctx.message.split(" , " ,3)[1:]
    if len(p_polls) >= 2:
         options_p = p_polls[1]
         options_polls = options_p.split(" ", 10)[0:]
         questions_p = p_polls[0]
         if len(options_polls) <= 1:
                 await message.send("You need to provide at least 2 options.")
                 return
         if len(options_polls) > 10:
                 await message.send("You can't provide more than 10 options.")
                 return

         # create the poll message
         message_polls = f"**{questions_p}**\n"
         for i, option in enumerate(options_polls):
                 message_polls += f"{i + 1}\U000020e3 {option}\n"

         poll = await channel_polls_id.send(message_polls)
         # add reactions to the poll message
         for i in range(len(options_polls)):
                 emojis = f"{i + 1}\U000020e3"
                 await poll.add_reaction(emojis)
         # countdown timer
         duration_p = 10    # set the duration to 60 seconds (change as needed)
         for i in range(duration_p):
                 await asyncio.sleep(1)
                 time_left = duration_p - i
                 if time_left % 10 == 0:
                         await poll.edit(content=f"{message_polls}\n\n**Time Left:** {time_left} seconds")

         # get poll results
         poll = await channel_polls_id.fetch_message(poll.id)
         reactions = poll.reactions
         results = []
         voters = 0
         for reaction in reactions:
                 for ind, emoji in enumerate(emojis):
                         if reaction.emoji == emoji:
    results[ind + 1] = reaction.count - 1
    if reaction.count > 1:
            voters += 1

         # create results message
         message_results = ""
         for ind, count in enumerate(results):
                 percent_p = round(results[ind + 1] / voters * 100)
                 message_results += f"{options_polls[ind]} ~ {percent_p}% ({results[ind + 1]} votes)\n"
         # send poll message with results
         embed = discord.Embed(title=f"POLL RESULTS: {questions_p}", description=results,
                        color=discord.Color.random())
         await channel_polls_id.send(embed=embed)
         #delete old poll message
         await poll.delete()
bot.run('Token')
