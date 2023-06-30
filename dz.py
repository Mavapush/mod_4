r=input()

def pal(s):
    slovo_naoborot = s[::-1]
    if slovo_naoborot == s:
        print("True")
    else:
        print("False")
pal(r)  