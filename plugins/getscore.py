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
