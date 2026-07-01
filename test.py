import unittest
import os
import csv
from main import students, load_data, save_data, add_student

class TestStudentSystem(unittest.TestCase):
    def setUp(self):
        """每个测试前重置数据"""
        global students
        students = []

    def test_add_student(self):
        """测试用例1：添加学生"""
        global students
        # 模拟输入
        original_input = input
        input_values = ["测试", "90"]
        def mock_input(s):
            return input_values.pop(0)
        import main
        main.input = mock_input
        main.add_student()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "测试")
        self.assertEqual(students[0]["score"], 90)

    def test_calculate_average(self):
        """测试用例2：计算平均分"""
        global students
        students = [
            {"name": "A", "score": 80},
            {"name": "B", "score": 90},
            {"name": "C", "score": 100}
        ]
        total = sum(s["score"] for s in students)
        avg = total / len(students)
        self.assertEqual(avg, 90.0)

    def test_save_and_load(self):
        """测试用例3：保存和加载文件"""
        global students
        test_data = [{"name": "赵六", "score": 88}]
        students = test_data
        save_data()
        students = []
        load_data()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "赵六")

if __name__ == "__main__":
    unittest.main()