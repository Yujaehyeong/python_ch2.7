#1. Local
#2. Enclosing Function(내포한 함수)
#3. Global
#4. Built-in


b = 300  # G
def f():
    b = 200  # E
    def g():
        # b = 100  #L
        print(b)
        print(__name__) #B
    g()


if __name__ == '__main__': # 자신이 import로 호출됐을때는 실행 안되게 함
    f()
