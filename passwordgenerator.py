import random
password_length = int(input("Enter the length of the password"))
sh = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ' '.join(random.sample(sh, password_length))
print(password)