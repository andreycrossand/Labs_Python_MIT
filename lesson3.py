import time
name = "Vanya" # type: str
second_name: str = "Elena"

def repeater(s: str, n : int) -> str:
    return s * n

# f = open("1.txt", "r")
# f.close()
#
# f = open("12.txt", "x") #создаем и открываем файлик мур мур
# f.write("Hello, world!")
# f = open("12.txt", "a") #дописывает
# f.write(str(5 * 2))
# f.close()

# контекстный менеджер

# with open("1.txt", "a") as f: #открыли "файл на дополнение"
#     f.write(str(5 * 2))
#
# class MyContextManager:
#     def __enter__(self):
#         self.t = time.time()
#         print("Entered")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.e = time.time()
#         print("Exited")
#
#
#         return self
#
#     def __float__(self):
#         return float(self.e - self.t)
#
# with MyContextManager() as mcm:
#     print("AAA")
#     raise Exception("hi")
#
# print(float(mcm))

 # написать контекстный менеджер для управления отступами
 # при входе в блок with количество отступов (табуляций) увеличивается на 1
 # запись ведётся в файл

class ContextManager:
    level = 0
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        ContextManager.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ContextManager.level -= 1

    def write(self, text: str):
        with open(self.filename, "a") as f:
            f.write(f"{'':>{ContextManager}}{text}\n")





