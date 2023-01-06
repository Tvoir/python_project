# print("Hello from inside a file!")

def arb_args(*args):
  for a in args:
    print(a)

arb_args('Tomm',"Tommy","TomTom")

def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())

inner_func("1","2")