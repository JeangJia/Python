class Student:
    def __init__(self, name, chinese: float = 0.0, math: float = 0.0, english: float = 0.0):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return (f"姓名: {self.name:5} | "
                f"语文: {self.chinese:3.1f} | "
                f"数学: {self.math:3.1f} | "
                f"英语: {self.english:3.1f} | "
                f"总分: {self.chinese + self.math + self.english}")

    def update_score(self, chinese: float = 0.0, math: float = 0.0, english: float = 0.0):
        self.chinese = chinese
        self.math = math
        self.english = english


class EduManageMent:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.students_list = []

    # 添加学生成绩
    def add_student(self):
        name = input("输入要添加学生姓名:")
        for i in self.students_list:
            if i.name == name:
                print("该学生已存在,添加失败!")
                return
        chinese = float(input("输入学生语文成绩:"))
        math = float(input("输入学生数学成绩:"))
        english = float(input("输入学生英语成绩:"))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            self.students_list.append(Student(name, chinese, math, english))
            print("添加成功 ~")
        else:
            print("请输入有效成绩,添加失败!")

    # 修改学生成绩
    def update_student(self):
        name = input("输入要修改学生姓名:")
        for i in self.students_list:
            if i.name == name:
                print(f"当前: {i}")
                while True:
                    chinese = float(input("重新输入学生语文成绩:"))
                    math = float(input("重新输入学生数学成绩:"))
                    english = float(input("重新输入学生英语成绩:"))
                    if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                        i.update_score(chinese, math, english)
                        print("更新成功!")
                        return
                    else:
                        print("请输入有效成绩! 重新输入!")
        print("不存在该学生!")

    # 删除学生成绩
    def del_student(self):
        name = input("输入要删除的学生姓名:")
        for i in self.students_list:
            if i.name == name:
                self.students_list.remove(i)
                print("删除成功!")
                return
        print("不存在该学生!")

    # 查找学生成绩
    def find_students(self):
        name = input("输入要查询的学生姓名:")
        for i in self.students_list:
            if i.name == name:
                print(f"当前: {i}")
                return
        print("不存在该学生!")

    # 展示所有学生成绩
    def show_students(self):
        if len(self.students_list) == 0:
            print("还不存在学生成绩!")
        else:
            for i in self.students_list:
                print(i)

    # 菜单
    def run(self):
        while True:
            print("=" * 40)
            print(f"\t\t\t{self.system_name} {self.system_version}")
            print("1. 添加学生")
            print("2. 修改学生成绩")
            print("3. 删除学生")
            print("4. 查询学生")
            print("5. 显示所有学生")
            print("0. 退出系统")
            print("=" * 40)
            choice = input("请输入操作序号：")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.del_student()
                case "4":
                    self.find_students()
                case "5":
                    self.show_students()
                case "0":
                    print("退出系统成功！")
                    break
                case _:
                    print("输入无效，请重新输入！")


if __name__ == '__main__':
    # 创建系统对象并启动菜单
    system = EduManageMent()
    system.run()
