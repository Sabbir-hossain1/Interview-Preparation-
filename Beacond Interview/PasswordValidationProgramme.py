import re
# Password must have al least one alphabet and at least 1 number
# def passValidation(password):
#     if re.search('[a-zA-z]',password) and re.search('[0-9]',password) and len(password)>=8:
#         return True
#     else: 
#         return False

def passwordValidator(password): 
    l,u,d,sp = 0,0,0,0   
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    specialchar="$@_"
    digits="0123456789"
    if len(password)>=8:
        for ch in password:
            if ch in smallalphabets:
                l+=1
            if ch in capitalalphabets:
                u+=1
            if ch in specialchar:
                sp+=1
            if ch in digits:
                d +=1
        if (l>=1 and u>=1 and sp>=1 and d>=1 and l+u+sp+d==len(password)):
            return True
        else:
            return False            
            
    else:
        print("Invalid password")


if __name__== '__main__':
    s = "R@m@_f0rtu9e$"
    if passwordValidator(s):
        print("valid password")
    else:
        print("Invalid password")
