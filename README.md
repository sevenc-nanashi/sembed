# sembed
[![PyPi](https://img.shields.io/pypi/v/sembed.svg)](https://pypi.org/project/sembed/) [![PyPI - Downloads](https://static.pepy.tech/badge/sembed)](https://pypi.org/project/sembed/) [![readthedocs](https://readthedocs.org/projects/sembed/badge/?version=latest)](https://sembed.readthedocs.io)  
This is a wrapper of discord.Embed of [discord.py](https://github.com/Rapptz/discord.py).  
  
***
  
  
Installation
====
Run this:
```bash
pip install sembed
```

***
  
  
Basic Usage
=====

## Simple Embed

```python
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
```
![simple_embed](https://raw.githubusercontent.com/sevenc-nanashi/sembed/main/docs/source/_static/simple_embed.png)

## All-in-one Embed

```python
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
```
![all_in_one_embed.png](https://raw.githubusercontent.com/sevenc-nanashi/sembed/main/docs/source/_static/all_in_one_embed.png)

## Edit Embed

```python
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
```
![edited_embed.png](https://raw.githubusercontent.com/sevenc-nanashi/sembed/main/docs/source/_static/edited_embed.png)
***

Prerequisites
====
* **Python 3.8|3.9 (Please make GitHub issue if you can use this lib on different python version)**  
* **[discord.py](https://github.com/Rapptz/discord.py)**   
***
  
License
====
Please see [LICENSE](https://github.com/sevenc-nanashi/sembed/blob/main/LICENSE).
