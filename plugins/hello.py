from alicebot import Plugin


class Hello(Plugin):
    async def handle(self) -> None:
        await self.event.reply("你好，这里是 zhixuebot，一个智学网查分机器人．")

    async def rule(self) -> bool:
        return str(self.event.message) == "/hello"
