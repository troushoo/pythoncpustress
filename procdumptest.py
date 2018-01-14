def func2():

        a = 1
        b = 2
        c = 0

        while True:
                c = a + b
                a = b * c
                b = b + c

def func1():
        func2()

func1()
