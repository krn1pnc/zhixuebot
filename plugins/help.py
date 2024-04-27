# This file is part of zhixuebot.
#
# zhixuebot is free software: you can redistribute it and/or modify it under the terms of the
# GNU Affero General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# zhixuebot is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License along with zhixuebot.
# If not, see <https://www.gnu.org/licenses/>.

from alicebot import Plugin

manual = {
    "hello":
    """hello 用法：
/hello：和机器人打招呼！
""",

    "help":
    """help 用法：
/help：获取命令列表．
/help [cmd]：获取命令 cmd 的帮助．""",

    "bind":
    """bind 用法：
/bind [username] [password]：绑定账号 username，密码为 password．
仅支持在私聊中使用此命令．
注意：您的账号和密码将会被 **明文** 储存在数据库中，自行衡量风险．""",

    "getexam":
    """getexam 用法：
/getexam：获取所有考试．
/getexam [n]：获取最近的 n 场考试．
需要先使用 /bind 绑定账号．""",

    "getscore":
    """getscore 用法：
/getscore：获取在最新考试中全科的成绩．
/getscore [exam_id]：获取在 exam_id 对应的考试中全科的成绩．
/getscore [exam_id] [subject]：获取在 exam_id 对应的考试中 subject 学科的成绩． 
需要先使用 /bind 绑定账号．""",

    "getrecord":
    """getrecord 用法：
/getrecord：获取在最新考试中全科的批卷记录．
/getrecord [exam_id]：获取在 exam_id 对应的考试中全科的批卷记录．
/getrecord [exam_id] [subject]：获取在 exam_id 对应的考试中 subject 学科的批卷记录．
需要先使用 /bind 绑定账号．"""
}


class Help(Plugin):
    async def handle(self) -> None:
        args = str(self.event.message).split()

        if len(args) == 1:
            await self.event.reply("目前可用的命令有：\n" + "\n".join([x for x in manual.keys()]))
        elif len(args) == 2:
            cmd = args[1]
            if cmd not in manual:
                await self.event.reply(f"{cmd} 不是一个命令．")
            else:
                await self.event.reply(manual[args[1]])
        else:
            await self.event.reply(manual["help"])

    async def rule(self) -> bool:
        return str(self.event.message).split()[0] == "/help"
