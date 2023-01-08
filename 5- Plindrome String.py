def plindrome(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False

def plindrome2(str1):
    reverse = []
    for val in str1:
        reverse.insert(0,val)
    if str1 == "".join(reverse):
        return True
    else:
        return False
    
output = plindrome2("radar")
print(output)
