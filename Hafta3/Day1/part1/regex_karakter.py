import re  #Regular Expression lib, it's use to search for pattern

text="AABC 123 983 1A3 1_2 354 2 78 23458 Aabc"

#pattern=r"\d\d\d"  # 3 points in a row
#pattern=r"\d{3}" # same 3 points in a row
#pattern=r"\d+"  # one or more numbers
# pattern=r"\d{3,5}"  #Between 3 to 5
pattern=r"[a-zA-Z]{3}"  # 3 letter (up/lowercase)

# match=re.search(pattern, text)
match=re.findall(pattern, text) #Findall is return the nonoverlapping match

sonuc=match

print(sonuc)

# match=re.finditer(pattern, text)

# for i in match:
#     print(i.group())