# def add(a,b):
#     answer=a+b
#     return answer

# def subtract (c,d):
#     answer1=c-d
#     return answer1

# def division(t,r):
#     results= t/r
#     return results
# def multiply(g,h):
#     results=g*h
#     return results

# def remainder(e,u):
#     results=e%u
#     return results 
# a function that can accept any number of keyword arguments
    # we define the function with one parameter but appaend two asterics to the argument
 
def student_attributes(**kwargs):
    for key, value in kwargs.items():
     print(f"{key} :{value}")


def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer
def my_country (country="Burundi"):
   print(f"hello from {country}")
#    A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*args):
   new_string=','.join(args)
   print(new_string)
#    def concat(*args, sep="/"):
    # return sep.join(args)

# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    for keyword,keynumber in kwargs.items():
      print(f"{keyword}:{keynumber}")