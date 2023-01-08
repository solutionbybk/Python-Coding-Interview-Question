def common_letter(str1,str2):
    s1 = set(str1.lower())
    s2 = set(str2.lower())
    return list(s1 & s2)

def comman_letter2(str1,str2):
    common = []
    for val in set(str1.lower()):
        if val in str2.lower():
            common.append(val)
    return list(set(common))

output = comman_letter2("Nitin","Naina")
print(output)
