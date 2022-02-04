def minimumNumber(n, password):
    numbers=set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    pas=set(password)
    chars=0
    chars+=1 if len(numbers.intersection(pas))==0 else 0
    chars+=1 if len(lower_case.intersection(pas))==0 else 0
    chars+=1 if len(upper_case.intersection(pas))==0 else 0
    chars+=1 if len(special_characters.intersection(pas))==0 else 0
    if n+chars<6:
        return 6-n
    else:
        return chars
     
print(minimumNumber(11,'#HackerRank'))

