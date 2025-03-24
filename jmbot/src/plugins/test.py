from importlib.metadata import version
import os
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
)
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.plugin.on import on_command
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.params import Depends, RegexGroup
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    Bot,
    Message,
    MessageSegment
)
import jmcomic

# 配置常量
PDF_DIR = "E:\\document\\jm\\pdf\\"  # PDF文件存储目录
COMMAND_PREFIX = "/jm"  # 命令前缀
# 创建正则匹配事件响应器，捕获数字参数
jm = on_regex(
    pattern=rf"^{COMMAND_PREFIX}\s+(\d+)$",  # 匹配 /jm 后跟数字的格式
    priority=3,
    block=True
)
# jm = on_command("/jm", aliases={"/JM"}, priority=2, block=True)
Test = on_regex(pattern=r'^测试$', priority=1)


@Test.handle()
async def Test_send(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = "Bot启动正常"
    await Test.finish(message=Message(msg))


# @jm.handle()
# async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
#     id = msg.extract_plain_text().strip()
#
#     await jm.send("正在下载中...", at_sender=True)
#
#     await bot.upload_group_file(
#         group_id=event.group_id,
#         file=PDF_DIR + f"{id}.pdf",
#         name=f"{id}.pdf",
#     )

@jm.handle()
async def handle_jm_command(
        bot: Bot,
        event: GroupMessageEvent,
        state: T_State,
        params: tuple = RegexGroup()
):
    num = params[0]
    file_name = num + ".pdf"
    file_path = PDF_DIR + num + ".pdf"
    jmdownload(num, file_path)
    await bot.upload_group_file(
        group_id=event.group_id,
        file=file_path,
        name=file_name
    )


def jmdownload(jmid, file_path):
    # 创建配置对象
    option = jmcomic.create_option_by_file('D:/programme/py/QQBOT/source/option.yml')
    # 使用option对象来下载本子
    if not os.path.exists(file_path):
        jmcomic.download_album(jmid, option)
        # 等价写法: option.download_album(422866)
