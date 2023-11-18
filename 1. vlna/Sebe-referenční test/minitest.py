slovo = "1"
for i in range(15):
    slovo += "0"

zhoda = 0
print(slovo)

if slovo[1:].count("0") >= 14 and slovo[0] == "1":
    zhoda += 1
elif slovo[1:].count("0") < 14 and slovo[0] == "0":
    zhoda += 1
                                                                
if "11" not in slovo and slovo[1] == 1:
    zhoda += 1
elif "11" in slovo and slovo[1] == 0:
    zhoda += 1

print(slovo[1:].count("0") >= 14)
print(slovo[0] == 1)
print(zhoda)