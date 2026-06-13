score_list = {
    "Jeang": {"Chinese": 70.0, "Math": 70.0, "English": 30.0},
    "Jia": {"Chinese": 80, "Math": 90, "English": 70},
}

while True:
    print("""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出学生信息  6. 统计班级成绩  7. 退出  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
""")
    inp = int(input("输入执行操作(1-7):"))

    match inp:
        case 1:
            name = input("输入学生姓名:")
            chinese = float(input("语文成绩:"))
            math = float(input("数学成绩:"))
            english = float(input("英语成绩:"))
            score_list[name] = {"Chinese": chinese, "Math": math, "English": english}
            print("添加成功!")

        case 2:
            name = input("输入要修改的学生姓名:")
            if name in score_list:
                chinese = float(input("语文成绩:"))
                math = float(input("数学成绩:"))
                english = float(input("英语成绩:"))
                score_list[name] = {"Chinese": chinese, "Math": math, "English": english}
                print("修改成功!")
            else:
                print("不存在!")

        case 3:
            name = input("输入要删除的学生姓名:")
            if name in score_list:
                del score_list[name]
                print("删除成功！")
            else:
                print("不存在!")

        case 4:
            name = input("输入要查询的学生姓名:")
            if name in score_list:
                print(f"{name}\t语文:{score_list[name]['Chinese']}\t数学:{score_list[name]['Math']}\t英语:{score_list[name]['English']}")
            else:
                print("不存在!")

        case 5:
            if not score_list:
                print("暂无学生信息")
            else:
                print("姓名\t\t语文\t\t数学\t\t英语")
                print("-" * 50)
                for name, score in score_list.items():
                    print(f"{name:<10}{score['Chinese']:<12.1f}{score['Math']:<12.1f}{score['English']:<12.1f}")

        case 6:
            if not score_list:
                print("暂无成绩可统计")
                continue

            # 统一拼写 Chinese
            chinese_dict = {}
            math_dict = {}
            english_dict = {}

            for name, score in score_list.items():
                chinese_dict[name] = score["Chinese"]
                math_dict[name] = score["Math"]
                english_dict[name] = score["English"]

            # 语文
            c_min_name = min(chinese_dict, key=chinese_dict.get)
            c_max_name = max(chinese_dict, key=chinese_dict.get)
            c_sum = sum(chinese_dict.values())
            c_avg = c_sum / len(chinese_dict)

            # 数学
            m_min_name = min(math_dict, key=math_dict.get)
            m_max_name = max(math_dict, key=math_dict.get)
            m_sum = sum(math_dict.values())
            m_avg = m_sum / len(math_dict)

            # 英语
            e_min_name = min(english_dict, key=english_dict.get)
            e_max_name = max(english_dict, key=english_dict.get)
            e_sum = sum(english_dict.values())
            e_avg = e_sum / len(english_dict)

            # 输出
            print("====== 班级成绩统计 ======")
            print(f"语文 | 最高分：{c_max_name}({chinese_dict[c_max_name]}) 最低分：{c_min_name}({chinese_dict[c_min_name]}) 平均分：{c_avg:.1f}")
            print(f"数学 | 最高分：{m_max_name}({math_dict[m_max_name]}) 最低分：{m_min_name}({math_dict[m_min_name]}) 平均分：{m_avg:.1f}")
            print(f"英语 | 最高分：{e_max_name}({english_dict[e_max_name]}) 最低分：{e_min_name}({english_dict[e_min_name]}) 平均分：{e_avg:.1f}")

        case 7:
            print("已退出!")
            break

        case _:
            print("请输入 1~7 之间的数字")