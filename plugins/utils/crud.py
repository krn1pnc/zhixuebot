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

from utils.db import DB

from zhixuewang import login_student
from zhixuewang.student import StudentAccount


def get_account(qqid: int) -> StudentAccount:
    try:
        account = DB.execute("SELECT username, password FROM users WHERE qqid=?", (qqid,)).fetchone()
    except Exception as e:
        raise Exception(f"数据库错误：{e}")

    if account is None:
        raise Exception("您尚未绑定账号．")

    (username, password) = account

    try:
        stu = login_student(username, password)
    except Exception as e:
        raise Exception(f"智学网登录错误：{e}")

    return stu
