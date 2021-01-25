from typing import List, Union, Optional
import datetime

import discord


class SField(object):
    """
    Represents a Field.
    Every attribute can be set during initialisation.
    

    Attributes
    -----------
    name : str
        The name of the field.
    value : str
        The value of the field.
    inline : str
        Whether the field should be displayed inline.
    """
    def __init__(self, name, value, inline=True):
        self.name = name
        self.value = value
        self.inline = inline


class SAuthor(object):
    """
    Represents an Author.
    Every attribute can be set during initialisation.
    

    Attributes
    -----------
    name : str
        The name of the author.
    icon_url : str
        The icon URL of the author.
    url : str
        The URL of the author.
    """
    def __init__(self, name: str, icon_url: str = None, url: str = None):
        self.name = name
        self.icon_url = icon_url
        self.url = url


class SFooter(object):
    """
    Represents a Footer.
    Every attribute can be set during initialisation.
    

    Attributes
    -----------
    text : str
        The text of the footer.
    icon_url : str
        The icon URL of the footer.
    """
    def __init__(self, text: str, icon_url: str = None):
        self.text = text
        self.icon_url = icon_url


class SEmbed(discord.Embed):
    """
    Represents a Discord embed.
    Every attribute can be set during initialisation.

    Attributes
    -----------
    title : str
        The title of the embed.
    description : str
        The description of the embed.
    url : str
        The URL of the embed.
    timestamp : datetime.datetime
        The timestamp of the embed content. This could be a naive or aware datetime.
    color : Union[discord.Color, int]
        The color code of the embed.
    image_url : str
        The image URL of the embed.
    thumbnail_url : str
        The thumbnail URL of the embed.
    fields : List[SEmbed]
        Fields of the embed. Up to 10.
    author : SAuthor
        The author of the embed.
    footer : SFooter
        The footer of the embed.
    
    
    """
    
    def __init__(self, title: str = "", description: str = "", *, url: str = "",
                 timestamp: datetime.datetime = None, color: Union[discord.Color, int] = None,
                 image_url: str = None, thumbnail_url: str = None,
                 fields: List[SField] = [], author: SAuthor = None, footer: SFooter = None):
        self.title: str = title
        self.description: str = description
        if color is None:
            self._raw_color = None
        elif isinstance(color, discord.Color):
            self._raw_color = color
        else:
            self._raw_color = discord.Color(color)
        self._raw_fields = fields
        self._raw_timestamp = timestamp
        self.image_url: str = image_url
        self.thumbnail_url: str = thumbnail_url
        self._raw_author = author
        self._raw_footer = footer
        self._raw_url = url
        self.type = "rich"

    @property
    def timestamp(self):
        return self._raw_timestamp
    
    @timestamp.setter
    def timestamp(self, val: datetime.datetime):
        self._raw_timestamp = val
    
    @property
    def url(self):
        return self._raw_url
    
    @url.setter
    def url(self, val: Optional[str]):
        self._raw_url = val

    @property
    def author(self):
        return self._raw_author
    
    @author.setter
    def author(self, val: Optional[SAuthor]):
        self._raw_author = val

    @property
    def footer(self):
        return self._raw_footer
    
    @footer.setter
    def footer(self, val: Optional[SFooter]):
        self._raw_footer = val

    @property
    def _fields(self):
        return [{"name": rf.name, "value": rf.value, "inline": rf.inline} for rf in self._raw_fields]

    @_fields.setter
    def _fields(self, val: List[SField]):
        self._raw_fields = val

    @property
    def fields(self):
        return self._raw_fields

    @fields.setter
    def fields(self, val: List[SField]):
        self._raw_fields = val

    @property
    def _author(self):
        if self.author:
            return {"name": self.author.name, "icon_url": self.author.icon_url or None, "url": self.author.url or None}
        else:
            raise AttributeError("_author")

    @property
    def _footer(self):
        if self.footer:
            return {"text": self.footer.text, "icon_url": self.footer.icon_url or None}
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
    def color(self, val: Union[discord.Color, int]):
        self._raw_color = val

    @property
    def _colour(self):
        return self._raw_color or discord.Embed.Empty

    @_colour.setter
    def _colour(self, val):
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
