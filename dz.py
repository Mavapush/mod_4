slovo = input()
a = len(slovo) // 2
print(slovo[:a] == slovo[:len(slovo)-a-1:-1])