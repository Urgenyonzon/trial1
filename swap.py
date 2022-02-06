
a = int(input("Enter the 1st number: "))           # 3 bits
b = int(input("Enter the 2nd number: "))           # 3 bits
a = a + b       #11  #4 bits  #we could use xor instead of + or - which uses only 3 bits as a and b
b = a - b       #5
a = a - b       #6
print("After swapping: ")
print(a)
print(b)