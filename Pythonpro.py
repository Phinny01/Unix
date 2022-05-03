import sys
key = int(sys.argv[1])
message = input("Input the message: ")
result = ""
string = ""
for i in message:
    if ord(char) < 64:
        result += i
    elif i == i.upper():  
        result += chr((ord(i) + key -65) % 26 +65)
    elif  i == i.lower():
        result += chr((ord(char) + key - 97) % 26 +97)
count1 = 0
count2 = 0
final = ""

string = result.replace(" ", "")
for j in string:
    if count1 == 5 and count2 != 50:
        final += " "
        count1 = 0
    elif count2 == 50:
        final += "\n"
        count2 = 0
    else:
        final += j 
        count1 += 1
        count2 += 1
print(final)         
