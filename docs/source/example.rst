Examples
========

Simple Embed
------------

.. code-block:: python

    import discord
    import sembed

    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == "please test sembed":
            e = sembed.SEmbed("Did you know that:", "This embed is made by sembed!")
            await message.channel.send(embed=e)

    client.run('your token here')

.. image:: _static/simple_embed.png

All-in-one Embed
----------------

.. code-block:: python

    import discord
    import sembed

    client = discord.Client()


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == "please test sembed":
            e = sembed.SEmbed(title="Title", description="Description", color=0x7289da,
                            fields=[sembed.SField("name1", "value1 - inline", True),
                                    sembed.SField("name2", "value2 - inline", True),
                                    sembed.SField("name3", "value3 - not inline", False)],
                            author=sembed.SAuthor("Author", "https://cdn.discordapp.com/avatars/686547120534454315/a_14261e094afcbfe4ab3abde42ac86987.gif", "https://discord.com"),
                            footer=sembed.SFooter("Footer", "https://cdn.discordapp.com/embed/avatars/2.png"),
                            url="https://github.com",
                            image_url="https://cdn.discordapp.com/embed/avatars/3.png",
                            thumbnail_url="https://cdn.discordapp.com/embed/avatars/0.png")

            await message.channel.send(embed=e)

    client.run('your token here')

.. image:: _static/all_in_one_embed.png

Edit Embed
----------

.. code-block:: python

    import discord
    import sembed

    client = discord.Client()


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == "please test sembed":
            e = sembed.SEmbed(title="Title", description="Description")
            await message.channel.send(embed=e)
            e.author = sembed.SAuthor("You can use SAuthor.")
            e.footer = "And you can set str."
            e.fields.append(sembed.SField("But...", "You must set SField to fields :("))
            await message.channel.send(embed=e)
            e.author.name = "(Edited)"
            e.fields[0].value = "(Edited)"
            e.footer.text = "(Edited)"
            await message.channel.send(embed=e)

    client.run('your token here')

.. image:: _static/edited_embed.png