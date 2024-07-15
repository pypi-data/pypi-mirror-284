'''
Name: ChickenSoup
Author: Monarchdos
Date: 2023-01-11 16:04:41
LastEditTime: 2024-07-15 15:51:41
'''
from nonebot import on_command, logger, get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment, GroupMessageEvent
from .config import Config
import requests

__plugin_meta__ = PluginMetadata(
    name = "心灵鸡汤",
    description = "来一碗心灵鸡汤吧",
    usage = "鸡汤,毒鸡汤",
    type="application",
    homepage="https://github.com/Monarchdos/nonebot_plugin_soup",
    supported_adapters={"~onebot.v11"},
)

plugin_config = get_plugin_config(Config)

jt = on_command('鸡汤', priority=1, block=True)
@jt.handle()
async def jt_(bot: Bot, event: GroupMessageEvent):
    try:
        core = "68747470733a2f2f6170692e61796672652e636f6d2f6a743f747970653d626f74267665723d312e312e30"
        res = ("\n" if plugin_config.chickensoup_reply_at else "") + str(requests.get(bytes.fromhex(core).decode()).text)
        if "wwwroot" in res or "html" in res or len(res) == 1: return
        await jt.send(message=Message(res), at_sender=plugin_config.chickensoup_reply_at)
    except requests.RequestException as e:
        logger.warning("Server connection failed.")

djt = on_command('毒鸡汤', priority=1, block=True)
@djt.handle()
async def djt_(bot: Bot, event: GroupMessageEvent):
    try:
        core = "68747470733a2f2f6170692e61796672652e636f6d2f646a743f747970653d626f74267665723d312e312e30"
        res = ("\n" if plugin_config.chickensoup_reply_at else "") + str(requests.get(bytes.fromhex(core).decode()).text)
        if "wwwroot" in res or "html" in res or len(res) == 1: return
        await djt.send(message=Message(res), at_sender=plugin_config.chickensoup_reply_at)
    except requests.RequestException as e:
        logger.warning("Server connection failed.")
