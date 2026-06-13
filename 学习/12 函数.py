def calc_score(score_list):
    """
    计算最低分,最高分,平均分
    Args:
        score_list: 分数列表

    Returns:最低分,最高分,平均分

    """
    return min(score_list), max(score_list), round(sum(score_list) / len(score_list), 1)


a, b, c = calc_score([89, 67, 68, 86, 90, 60])
print(a, b, c)
