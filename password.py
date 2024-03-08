import random 
import string
def create(l):
    char=string.ascii_lowercase+string.digits+string.ascii_uppercase
    password=''.join(random.choice(char)for i in range(l))
    return password
l=int(input("enter a suitable length for your password:"))
print("your password is:",create(l))