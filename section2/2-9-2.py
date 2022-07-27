import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

f = SelfTest()
#f.function1()
print(id(f))
f.function2()#인스턴스 주소값이 전달됨 

#첫번째 function호출하려면? instance하지않고 namespace를 클래스에서 바로 호출해야함
print("----------------------------------------------------")
print(SelfTest.__dict__)
print(SelfTest.function1())
print("----------------------------------------------------")
SelfTest.function1()

print("----------------------------------------------------")
f2 = SelfTest()
SelfTest.function2(f2)
print("----------------------------------------------------")