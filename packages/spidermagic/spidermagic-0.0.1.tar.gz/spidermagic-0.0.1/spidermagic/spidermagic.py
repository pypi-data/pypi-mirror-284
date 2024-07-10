from typing import Dict, Tuple
import datetime
import re


class TimedErrorList:
    """
    在规定时间内传入的数据过长就抛出错误,适用于爬虫
    max_age:单位秒,时间长度,保存时间超过这个数就删掉元素
    max_length:元素的数量,在max_age时间长度下,最多允许保存这么多元素,超过即抛出错误
    """

    def __init__(self, max_length: int = 100, max_age: int = 60):
        self.errors: Dict[str, Tuple[str, datetime.datetime]] = {}
        self.max_length = max_length
        self.max_age = max_age  # in seconds

    def append_error(self, error: str):
        now = datetime.datetime.now().isoformat()  # 使用ISO格式作为键，确保唯一性
        if len(self.errors) >= self.max_length:
            raise ValueError("Error list exceeds maximum length.")

        self.errors[now] = (error, datetime.datetime.now())  # 存储错误信息和实际的时间对象

        # 清理旧错误
        to_remove = [k for k, (_, timestamp) in self.errors.items()
                     if (datetime.datetime.now() - timestamp).total_seconds() > self.max_age]
        for key in to_remove:
            del self.errors[key]


def list_to_str(w_list: list, symbol='') -> str:
    if not w_list:
        w_list2 = None
    else:
        w_list1 = symbol.join(w_list).replace("\n", "").replace(" ", "")
        w_list2 = re.sub(r'\s+', '', w_list1)
        if w_list2 == "-":
            w_list2 = None
    return w_list2