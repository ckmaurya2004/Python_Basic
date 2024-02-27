# a=5
# b=6
# c= sum((a,b))
# print(c)

# def func(a,b):
#     """this is a  function  that generate average of two number """
   
#     return (a+b)/2

# print(func.__doc__)
# print(func(2,4))


# there are 4 type of function arguments
"""
1-> default arguments
2-> required arguments
3-> variable_length arguments
4-> keyword arguments

"""
# default arguments

# def avg(a=3,b=2):
#     print((a+b)/2)
# avg()


# required arguments

# def avg(a,b):
#     print((a+b)/2)
# avg(3,5)

# variable_length arguments

# def avg(*n):
#     print(sum(n)/len(n))
# avg(2,4)
# avg(2,4,5)

# keyword arguments

def avg(a,b=1):
    print((a+b)/2)

avg(b=4,a=5)
