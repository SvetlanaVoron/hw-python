# Задание 1

class Matrix:
    def __init__(self, num_1_1, num_1_2, num_1_3, num_2_1, num_2_2, num_2_3, num_3_1, num_3_2, num_3_3):
        self.num_1_1 = num_1_1
        self.num_1_2 = num_1_2
        self.num_1_3 = num_1_3
        self.num_2_1 = num_2_1
        self.num_2_2 = num_2_2
        self.num_2_3 = num_2_3
        self.num_3_1 = num_3_1
        self.num_3_2 = num_3_2
        self.num_3_3 = num_3_3

    def __add__(self, other):
        return Matrix(self.num_1_1 + other.num_1_1, self.num_1_2 + other.num_1_2, self.num_1_3 + other.num_1_3,
                      self.num_2_1 + other.num_2_1, self.num_2_2 + other.num_2_2, self.num_2_3 + other.num_2_3,
                      self.num_3_1 + other.num_3_1, self.num_3_2 + other.num_3_2, self.num_3_3 + other.num_3_3)

    def __str__(self):
        return f"| {self.num_1_1}  {self.num_1_2}  {self.num_1_3} |\n" \
               f"| {self.num_2_1}  {self.num_2_2}  {self.num_2_3} |\n" \
               f"| {self.num_3_1}  {self.num_3_2}  {self.num_3_3} |\n"

    def matrix(self):
        print(f"| {self.num_1_1}  {self.num_1_2}  {self.num_1_3} |\n"
              f"| {self.num_2_1}  {self.num_2_2}  {self.num_2_3} |\n"
              f"| {self.num_3_1}  {self.num_3_2}  {self.num_3_3} |\n")

m_obj_1 = Matrix(1, 2, 3, 4, 5, 6, 7, 8, 9)
m_obj_2 = Matrix(10, 20, 30, 40, 50, 60, 70, 80, 90)
print("Матрица 1:")
m_obj_1.matrix()
print("Матрица 2:")
m_obj_2.matrix()
print("Сумма матриц:")
print(m_obj_1 + m_obj_2)


#--------- V2----- не понмиаю как основываясь на материалах курса 
class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def matrix(self):
        for i in self.numbers:
            i = str(i)
            line = " ".join(i).replace(", ", "")
            print(f"| {line[1:-1]} |")

    def __str__(self):
        for line in range(len(self.numbers)):
            for i in range(len(self.numbers[line])):
                return Matrix([self.numbers[line][i] + other.numbers[line][i]])

    def __add__(self, other):
        for line in range(len(self.numbers)):
            for i in range(len(self.numbers[line])):
                return Matrix(str([self.numbers[line][i] + other.numbers[line][i]]))


m_obj_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_obj_2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Матрица 1:")
m_obj_1.matrix()
print("Матрица 2:")
m_obj_2.matrix()
print("Сумма матриц:")
print(m_obj_1 + m_obj_2)