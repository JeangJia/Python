def calc_score1(score_list):
    """
    计算最低分,最高分,平均分
    Args:
        score_list: 分数列表

    Returns:最低分,最高分,平均分

    """
    return min(score_list), max(score_list), round(sum(score_list) / len(score_list), 1)


a, b, c = calc_score1([89, 67, 68, 86, 90, 60])
print(a, b, c)

# 不定长传参方式
"""
    *args：接收任意多个位置参数，是元组
    **kwargs：接收关键字参数，是字典
"""


def calc_score2(*args, **kwargs):
    ret_min = min(args)
    ret_max = max(args)
    ret_avg = sum(args) / len(args)
    if kwargs.get("round") is not None:
        ret_avg = round(ret_avg, kwargs["round"])
    if kwargs.get("print"):
        print(f"最小值:{ret_min}\n最大值:{ret_max}\n平均值:{ret_avg}")
    return ret_min, ret_max, ret_avg


print(calc_score2(12, 23, 3423, 34, 23, 7, 85, 6, round=2, print=True))
print(calc_score2(12, 23, 3423, 34, 23, 7, 85, 6))

# 匿名函数
out_line = lambda: print("------------------")
out_line()

# sort()
s = [123, 345, 23, 3, 23, 67547]
s.sort(key=lambda x: len(str(x)))
print(s)
