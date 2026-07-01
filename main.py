# 模块1：数据管理模块 - 负责人：蒋鑫
# 模块2：文件读写模块 - 负责人：蒋鑫
# 模块2：文件读写模块 - 负责人：蒋鑫
import csv
import os

DATA_FILE = "students.csv"
students = []

def load_data():
    """从 CSV 文件加载数据（文件读写模块）"""
    global students
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = [{"name": row["name"], "score": float(row["score"])} for row in reader]
    print(f"已加载 {len(students)} 条学生记录")

def save_data():
    """保存数据到 CSV 文件（文件读写模块）"""
    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(students)
    print("数据已保存")

def add_student():
    """添加学生成绩（数据管理模块）"""
    name = input("请输入学生姓名：")
    score = float(input("请输入成绩："))
    students.append({"name": name, "score": score})
    print(f"已添加：{name}，{score}分")

def view_students():
    """查看所有学生（数据管理模块）"""
    if not students:
        print("暂无学生数据")
        return
    print("\n姓名\t成绩")
    print("-" * 20)
    for s in students:
        print(f"{s['name']}\t{s['score']}")
    print("-" * 20)
    total = sum(s["score"] for s in students)
    avg = total / len(students)
    print(f"总人数：{len(students)}，总分：{total:.1f}，平均分：{avg:.1f}")

def sort_students():
    """按成绩排序（数据管理模块）"""
    sorted_list = sorted(students, key=lambda x: x["score"], reverse=True)
    print("\n成绩排名（从高到低）")
    print("姓名\t成绩")
    print("-" * 20)
    for s in sorted_list:
        print(f"{s['name']}\t{s['score']}")

def show_menu():
    """显示菜单（用户交互模块）"""
    while True:
        print("\n=== 学生成绩管理系统 ===")
        print("1. 添加学生成绩")
        print("2. 查看所有成绩")
        print("3. 成绩排名")
        print("4. 保存数据")
        print("5. 退出")
        choice = input("请选择：")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            sort_students()
        elif choice == "4":
            save_data()
        elif choice == "5":
            print("退出系统")
            break
        else:
            print("无效输入，请重新选择")

if __name__ == "__main__":
    load_data()
    show_menu()