def hello(*names):
    for name in names:
        print(f"hello{name}")
        # write a function that accepts a number of intergers and returns the answer

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer


# write a function that accepts a number of intergers and returns the answer
def multiply(*nums):
    answ=1
    for num in nums:
        answ*=num
        return answ
        # A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*args):
   new_string=','.join(args)
   print(new_string)
   # A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    for keyword,value in kwargs.items():
      print(f"{keyword}:{value}")
    