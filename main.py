import asyncio
from pytgcalls import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py

bot.start()
print("Userbot Started")
call_py.start()
print("Vc Client Started")
pyidle()
idle()
