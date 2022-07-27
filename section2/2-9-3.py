import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스변수
class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

u1 = Warehouse("kim")
u2 = Warehouse("park")

print(u1.name)
print(u2.name)
print(u1.__dict__)
print(u2.__dict__)
print(Warehouse.__dict__)
#인스턴스의 네임스페이스 확인 -> 없으면 -> 클래스 네임스페이스로 찾음, 클래스변수는 서로 공유됨
print(u1.stock_num)
print(u2.stock_num)
