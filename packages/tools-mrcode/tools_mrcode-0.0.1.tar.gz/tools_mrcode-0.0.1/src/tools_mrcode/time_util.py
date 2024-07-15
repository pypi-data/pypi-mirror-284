from datetime import datetime, timedelta


def time_diff_second(start_time, end_time):
    """
    计算两个时间相差的秒数
    :param start_time:
    :param end_time:
    :return:
    """
    return (end_time - start_time).total_seconds()


def time_diff_minute(start_time, end_time):
    """
    计算两个时间相差的分钟数
    :param start_time:
    :param end_time:
    :return:
    """
    return time_diff_second(start_time, end_time) / 60


def format_time(time, format="%Y-%m-%d %H:%M:%S"):
    """
    格式化时间
    :param time:
    :param format: 格式化字符串
    :return:
    """
    return time.strftime(format)


# 解析时间
def parse_time(time_str, format="%Y-%m-%d %H:%M:%S"):
    """
    解析时间
    :param time_str:
    :param format: 格式化字符串
    :return:
    """
    return datetime.strptime(time_str, format)


