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

import zhixuewang
from zhixuewang.exceptions import *

from help import manual
from utils.db import DBCON, DB


class Bind(Plugin):
    async def handle(self) -> None:
        if self.event.type == "GroupMessage":
            await self.event.reply("仅支持私聊绑定．")
            return

        args = str(self.event.message).split()
        if len(args) != 3:
            await self.event.reply(manual["bind"])
            return

        (username, password) = (args[1], args[2])

        try:
            zhixuewang.login_student(username, password)
        except Exception as e:
            await self.event.reply(f"智学网登录错误：{e}")
            return

        try:
            DB.execute("INSERT INTO users VALUES (?, ?, ?) ON CONFLICT (qqid) DO UPDATE SET (username, password) = (excluded.username, excluded.password)",
                       (self.event.sender.id, username, password))
            DBCON.commit()
        except Exception as e:
            await self.event.reply(f"数据库错误：{e}")
            return

        await self.event.reply("绑定成功")

    async def rule(self) -> bool:
        return str(self.event.message).split()[0] == "/bind"
