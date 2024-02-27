# list = [3,5,7,8,3]
# gt = iter(list)
# print(gt)
# print(gt.__next__())


# generator function of factorial

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        # print(i)
        fact = fact * i
        yield fact
    return
   

result = factorial(5)
# for i in result:
print(result)
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
