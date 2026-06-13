shopping = {
    "K70": {"price": 1999, "num": 5},
    "iphone": {"price": 9999, "num": 3},
}

while True:
    print("""
######## 购物车系统 ########
#     1. 添加购物车        #
#     2. 修改购物车        #
#     3. 删除购物车        #
#     4. 查询购物车        #
#     5. 退出购物车        #
##########################
""", end=" ")
    inp = input("请输入要执行的操作(1-5):")

    match inp:
        case "1":
            name = input("商品名称:")
            price = float(input("商品价格:"))
            num = int(input("商品数量:"))
            shopping[name] = {"price": price, "num": num}
            print("添加成功!")
        case "2":
            name = input("输入要修改的商品名称:")
            if name in shopping:
                price = float(input("商品价格:"))
                num = int(input("商品数量:"))
                shopping[name] = {"price": price, "num": num}
                print("修改完毕!")
            else:
                print("商品不存在!")
        case "3":
            name = input("输入要删除的商品名称:")
            if name in shopping:
                del shopping[name]
                print("删除完毕!")
            else:
                print("商品不存在!")
        case "4":
            if shopping:
                # 表头对齐
                print("商品名称\t\t\t价格\t\t\t数量")
                print("-" * 40)
                # 内容统一排版
                for name, info in shopping.items():
                    print(f"{name:10}\t{info['price']:8.1f}\t{info['num']:5}")
            else:
                print("购物车为空!")
        case "5":
            print("已退出!")
            break
        case _:
            print("请输入有效值!")
