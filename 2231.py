a = int(input())

def digit_sum(number):

    total = 0
    num_str = str(abs(number))  
    
    for digit in num_str:
        total += int(digit) 
        
    return total

for i in range(a-len(str(a))*9,a):
  if i+digit_sum(i)==a:
    print(i)
    break
  if(i==a-1):
    print(0)