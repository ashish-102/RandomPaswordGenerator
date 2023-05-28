import random
chars = '0qweQWE1rtyRTY2uiopUIOP3[]4asdASD5fghFGH6jklJKL7zxcZXC8vbnVBN9mM@#$%&-_!'
password = ''

n = int(input())
for i in range(n):
    password += random.choice(chars) 

print(password)
