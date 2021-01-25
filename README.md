# sembed
[![PyPi](https://img.shields.io/pypi/v/sembed.svg)](https://pypi.org/project/sembed/)

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
### Translate
```python
import asyncio
from sembed 

 
async def coro():
    g = async_google_trans_new.google_translator()
    print(await g.translate("こんにちは、世界！","en"))
loop=asyncio.get_event_loop() 
loop.run_until_complete(coro())
-> Hello world!
```
***

Advanced Usage
=====
### Translate 
### Multi Translate
```python
import asyncio
from async_google_trans_new import google_translator

 
async def coro():
    g = google_translator()
    texts = ["こんにちは、世界！", "こんばんは、世界！", "おはよう、世界！"]
    gathers = []
    for text in texts:
    	  gathers.append(g.translate(text, "en"))
    
    print(await asyncio.gather(*gathers))

loop=asyncio.get_event_loop() 
loop.run_until_complete(coro())
-> ['Hello World! ', 'Good evening, the world! ', 'Good morning, the world! '] 
```
***

Prerequisites
====
* **Python 3.8 (Please make GitHub issue if you can use this lib on different python version)**  
* **aiohttp**  
* **urllib3**  
***
  
License
====
Please see [LICENSE](https://github.com/sevenc-nanashi/async_google_trans_new/blob/main/LICENSE).
