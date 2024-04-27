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


class GetScore(Plugin):
    async def handle(self) -> None:
        try:
            stu = get_account(self.event.sender.id)
        except Exception as e:
            await self.event.reply(f"{e}")
            return

        args = str(self.event.message).split()
        exam, subjects = None, None
        if len(args) == 1:
            exam = stu.get_exam()
            subjects = stu.get_subjects()
        elif len(args) == 2:
            exam = stu.get_exam(args[1])
            subjects = stu.get_subjects(exam)
        elif len(args) == 3:
            exam = stu.get_exam(args[1])
            subjects = [stu.get_subject(args[2], exam)]
        else:
            await self.event.reply(manual["getscore"])
            return

        msg = []
        for subject in subjects:
            record = stu.get_answer_records(subject, exam)
            score = sum([topic.score for topic in record])
            msg.append(f"{subject.name}：{score} / {subject.standard_score}")

        await self.event.reply(gen_quote("得分情况", f"{exam.name}", ["\n".join(msg)]))

    async def rule(self) -> bool:
        return str(self.event.message).split()[0] == "/getscore"
