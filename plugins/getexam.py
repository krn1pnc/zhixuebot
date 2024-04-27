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

from help import manual
from utils.crud import get_account
from utils.msg import gen_quote


class GetExam(Plugin):
    async def handle(self) -> None:
        try:
            stu = get_account(self.event.sender.id)
        except Exception as e:
            await self.event.reply(f"{e}")
            return

        args = str(self.event.message).split()
        n = None
        if len(args) == 1:
            pass
        elif len(args) == 2:
            n = int(args[1])
        else:
            await self.event.reply(manual["getexam"])
            return

        exams = stu.get_exams()[0:n]
        await self.event.reply(gen_quote("考试列表", "", [f"名称：{exam.name}\nid：{exam.id}" for exam in exams]))

    async def rule(self) -> bool:
        return str(self.event.message).split()[0] == "/getexam"
