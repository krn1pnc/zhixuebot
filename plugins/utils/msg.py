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
