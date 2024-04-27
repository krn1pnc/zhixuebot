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
