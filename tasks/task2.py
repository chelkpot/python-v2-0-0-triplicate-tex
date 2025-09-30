# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    X, Y, Z = map(int, input("Введите значение: ").split())
    r = 3
    k = r + 2
    f = k + 7
    
    total_cost = (X * r) + (Y * k) + (Z * f)
    print(total_cost)

   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()