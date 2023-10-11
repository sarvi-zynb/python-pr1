def fun1():
    student = {
        'username' : 'zynb',
        'email' : 'a@gmail.com',
        'id' : 1234,
        'age' : 24
    }

    student.pop('email')
    print(student)



def fun2():
    myColor = ['blue' , 'pink' , 'red' , 'yellow' , 'green']

    myColor.pop(1)
    # del myColor[1]
    print(myColor)


def fun3():
    names = ('zynb' , 'reza' , 'ali' , 'sara')

    # A tuple is a collection which is unchangeable.
    print(names)


fun1()
fun2()
fun3()