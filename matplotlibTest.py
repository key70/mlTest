import matplotlib.pyplot as plt
import numpy as np


#-10에서 10까지의 범위안에 균등하게 간격을 두어 100개의 값(데이터)을 생성해바
x = np.linspace(-10,10, 100)
y = np.sin(x)

plt.plot(x,y)
plt.show()

def not_used4():
    #연습)
    #x의 범위가 -10에서 10일때 x의 제곱을 그려 봅니다.
    x = np.arange(-10,10,0.1)
    y = x ** 2

    plt.plot(x,y,'ro')
    plt.show()


def not_used3():
    x = list(range(-10,11,1))
    y = []

    for a in x:
        y.append(a**2)


    plt.plot(x,y,"ro")
    plt.show()


def not_used2():
    age = [28,16,40,30,20,29,28,17]
    height = [175,180,173,167,170,185,160,172]

    # plt.plot(age, height)
    plt.plot(age,height,'ro')
    plt.xlim(0,60)
    plt.ylim(0,200)
    plt.show()




def not_used():
    # data = [10,20,30,40,50]
    data = [28,16,40,30,20,29,28,17]

    plt.plot(data)
    plt.show()
