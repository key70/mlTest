# def add(a,b):
#     r = a + b
#     return r

#연습)위의 함수를 람다식으로 만들어 봅니다.
add = lambda a,b: a+b
print(add(5,7))


# def max(a,b):
#     r = a
#     if b > r:
#         r = b
#     return r

# max = lambda a,b : a   if a>b  else b
#
# print(max(5,30))