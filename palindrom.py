def is_palindrom(line):
    if line == line[::-1]:
        return True
    else:
        return False

print(is_palindrom('лепсспел'))
print(is_palindrom('helloworld'))