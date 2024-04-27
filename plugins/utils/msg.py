from typing import List

from configs import qq, bot_name


def gen_quote(name: str, preview: str, messages: List[str]):
    return {
        "type": "Forward",
        "display": {
            "title": name,
            "brief": name,
            "source": name,
            "preview": [preview],
            "summary": "查看{:s}".format(name)
        },
        "nodeList": [
            {
                "senderId": qq,
                "time": 0,
                "senderName": bot_name,
                "messageChain": [{"type": "Plain", "text": s}],
            }
            for s in messages]
    }
