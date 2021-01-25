from typing import List, Union
import datetime

import discord


class SField(object):
    def __init__(self, name, value, inline=True):
        self.name = name
        self.value = value
        self.inline = inline


class SAuthor(object):
    def __init__(self, name: str, icon_url: str = None, url: str = None):
        self.name = name
        self.icon_url = icon_url
        self.url = url


class SFooter(object):
    def __init__(self, text: str, icon_url: str = None):
        self.text = text
        self.icon_url = icon_url


class SEmbed(discord.Embed):
    def __init__(self, title: str = "", description: str = "", *, color: Union[discord.Color, int] = None,
                 url: str = "", fields: List[SField] = [], timestamp: datetime.datetime = None,
                 image_url: str = None, thumbnail_url: str = None,
                 author: SAuthor = None, footer: SFooter = None):
        self.title = title
        self.description = description
        if color is None:
            self._raw_color = None
        elif isinstance(color, discord.Color):
            self._raw_color = color
        else:
            self._raw_color = discord.Color(color)
        self._raw_fields = fields
        self._raw_timestamp = timestamp
        self.image_url = image_url
        self.thumbnail_url = thumbnail_url
        self._raw_author = author
        self._raw_footer = footer
        self._raw_url = url
        self.type = "rich"

    @property
    def timestamp(self):
        return self._raw_timestamp
    
    @timestamp.setter
    def timestamp_setter(self, val):
        self._raw_timestamp = val
    
    @property
    def url(self):
        return self._raw_url
    
    @url.setter
    def url_setter(self, val):
        self._raw_url = val

    @property
    def author(self):
        return self._raw_author
    
    @author.setter
    def author_setter(self, val):
        self._raw_author = val

    @property
    def footer(self):
        return self._raw_footer
    
    @footer.setter
    def footer_setter(self, val):
        self._raw_footer = val

    @property
    def _fields(self):
        return [{"name": rf.name, "value": rf.value, "inline": rf.inline} for rf in self._raw_fields]

    @_fields.setter
    def _fields(self, val):
        self._raw_fields = val

    @property
    def _author(self):
        if self.author:
            return {"name": (self.author.name or discord.Embed.Empty), "icon_url": (self.author.icon_url or discord.Embed.Empty), "url": (self.author.url or discord.Embed.Empty)}
        else:
            raise AttributeError("_author")

    @property
    def _footer(self):
        if self.footer:
            return {"text": (self.footer.text or discord.Embed.Empty), "icon_url": (self.footer.icon_url or discord.Embed.Empty)}
        else:
            raise AttributeError("_footer")

    @property
    def _timestamp(self):
        if self.timestamp:
            return self.timestamp
        else:
            raise AttributeError("_footer")
        
    @property
    def color(self):
        return self._raw_color
    
    @color.setter
    def color_setter(self, val):
        self._raw_color = val

    @property
    def _colour(self):
        return self._raw_color or discord.Embed.Empty

    @_colour.setter
    def _colour_setter(self, val):
        self._raw_color = val

    @property
    def _thumbnail(self):
        if self.image_url:
            return {"url": self.thumbnail_url}
        else:
            raise AttributeError("_thumbnail")

    @property
    def _image(self):
        if self.image_url:
            return {"url": self.image_url}
        else:
            raise AttributeError("_image")
