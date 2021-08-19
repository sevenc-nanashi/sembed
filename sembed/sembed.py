from typing import List, Union, Optional
from dataclasses import dataclass
import datetime

import discord


@dataclass
class SField:
    """
    Represents a Field.
    Every attribute can be set during initialisation.

    Attributes
    -----------
    name : str
        The name of the field.
    value : str
        The value of the field.
    inline : bool
        Whether the field should be displayed inline.
    """
    name: str
    value: str
    inline: bool = True


@dataclass
class SAuthor:
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
    name: str
    icon_url: str = None
    url: str = None


@dataclass
class SFooter:
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
    text: str
    icon_url: str


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
        The timestamp of the embed content.
        This could be a naive or aware datetime.
    color : Union[discord.Color, int]
        The color code of the embed.
    image_url : str
        The image URL of the embed.
    thumbnail_url : str
        The thumbnail URL of the embed.
    fields : List[SEmbed]
        Fields of the embed. Up to 10.
    author : Union[SAuthor, str]
        The author of the embed.
    footer : Union[SFooter, str]
        The footer of the embed.
    """

    def __init__(
        self,
        title: str = "",
        description: str = "",
        *,
        url: str = "",
        timestamp: datetime.datetime = None,
        color: Union[discord.Color, int] = None,
        image_url: str = None,
        thumbnail_url: str = None,
        fields: List[SField] = None,
        author: Union[SAuthor, str] = None,
        footer: Union[SFooter, str] = None,
        **kwargs
    ):

        super().__init__(**kwargs)
        self.title = title
        self.description = description

        if color is None:
            self._raw_color = None
        elif isinstance(color, discord.Color):
            self._raw_color = color
        else:
            self._raw_color = discord.Color(color)

        self._raw_fields = fields or []
        self._raw_timestamp = timestamp
        self.image_url = image_url
        self.thumbnail_url = thumbnail_url
        self.author = author
        self.footer = footer
        self._raw_url = url
        self.type = "rich"

    @property
    def timestamp(self) -> datetime.datetime:
        return self._raw_timestamp

    @timestamp.setter
    def timestamp(self, val: datetime.datetime):
        self._raw_timestamp = val

    @property
    def url(self) -> str:
        return self._raw_url

    @url.setter
    def url(self, val: Optional[str]):
        self._raw_url = val

    @property
    def author(self) -> SAuthor:
        """
        The author of the embed.

        Returns
        -------
        SAuthor
            The author of the embed.
        """
        return self._raw_author

    @author.setter
    def author(self, val: Union[SAuthor, str, None]):
        self._raw_author = SAuthor(name=val) if isinstance(val, str) else val

    @property
    def footer(self) -> SFooter:
        return self._raw_footer

    @footer.setter
    def footer(self, val: Union[SFooter, str, None]):
        self._raw_footer = SFooter(text=val) if isinstance(val, str) else val

    @property
    def _fields(self):
        return [
            {"name": rf.name, "value": rf.value, "inline": rf.inline}
            for rf in self._raw_fields
        ]

    @_fields.setter
    def _fields(self, val: List[SField]):
        self._raw_fields = val

    @property
    def fields(self) -> List[SField]:
        return self._raw_fields

    @fields.setter
    def fields(self, val: List[SField]):
        self._raw_fields = val

    @property
    def _author(self):
        if not self.author:
            raise AttributeError("_author")

        return {
            "name": self.author.name,
            "icon_url": self.author.icon_url or None,
            "url": self.author.url or None
        }

    @property
    def _footer(self):
        if not self.footer:
            raise AttributeError("_footer")

        return {
            "text": self.footer.text,
            "icon_url": self.footer.icon_url or None
        }

    @property
    def _timestamp(self):
        if not self.timestamp:
            raise AttributeError("_timestamp")

        return self.timestamp

    @property
    def color(self) -> discord.Color:
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
        if not self.thumbnail_url:
            raise AttributeError("_thumbnail")

        return {"url": self.thumbnail_url}

    @property
    def _image(self):
        if not self.image_url:
            raise AttributeError("_image")

        return {"url": self.image_url}

