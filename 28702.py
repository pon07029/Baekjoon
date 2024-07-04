a = input()
b = input()
c = input()
d =0
if(a.isdecimal()):
  d= int(a)+3
elif b.isdecimal():
  d =int(b)+2
elif c.isdecimal():
  d =int(c)+1

if d% 15 == 0 :
  print("FizzBuzz")
elif d%5 ==0:
  print("Buzz")
elif d%3 ==0:
  print("Fizz")
else :
  print(d)