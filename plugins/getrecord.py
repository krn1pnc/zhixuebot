from alicebot import Plugin

from help import manual
from utils.crud import get_account
from utils.msg import gen_quote


class GetRecord(Plugin):
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
            await self.event.reply(manual["getrecord"])
            return

        msg_list = []
        for subject in subjects:
            record = stu.get_answer_records(subject, exam)
            msg = [f"{subject.name} 的批卷记录："]
            for topic in record:
                msg.append(f"{topic.title}：{topic.score} / {topic.standard_score}")
                if topic.subtopic_records is not None:
                    for idx, subtopic in enumerate(topic.subtopic_records, 1):
                        msg.append(f"({idx})：{subtopic.score}")
                        if subtopic.marking_records is not None:
                            for record in subtopic.marking_records:
                                msg.append(f"{record.teacher_name} 在 {record.time} 打出了 {record.score} 分．")
            msg_list.append("\n".join(msg))

        await self.event.reply(gen_quote("批卷记录", f"{exam.name}", msg_list))

    async def rule(self) -> bool:
        return str(self.event.message).split()[0] == "/getrecord"
