for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                for i in range(2):
                                    for j in range(2):
                                        for k in range(2):
                                            for l in range(2):
                                                for m in range(2):
                                                    for n in range(2):
                                                        for o in range(2):
                                                            for p in range(2):
                                                                zhoda = 0
                                                                slovo = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)

                                                                #1
                                                                if slovo[1:].count("0") >= 14 and slovo[0] == "1":
                                                                    zhoda += 1
                                                                elif slovo[1:].count("0") < 14 and slovo[0] == "0":
                                                                    zhoda += 1
                                                                
                                                                #2
                                                                if "11" not in slovo and slovo[1] == "1":
                                                                    zhoda += 1
                                                                elif "11" in slovo and slovo[1] == "0":
                                                                    zhoda += 1

                                                                #3
                                                                if slovo[1] == slovo[3] and slovo[2] == "1":
                                                                    zhoda += 1
                                                                elif slovo[1] != slovo[3] and slovo[2] == "0":
                                                                    zhoda += 1
                                                                
                                                                #4
                                                                if slovo[2] == slovo[4] and slovo[3] == "1":
                                                                    zhoda += 1
                                                                elif slovo[2] != slovo[4] and slovo[3] == "0":
                                                                    zhoda += 1
                                                                
                                                                #5
                                                                if slovo[3] != slovo[5] and slovo[4] == "1":
                                                                    zhoda += 1
                                                                elif slovo[3] == slovo[5] and slovo[4] == "0":
                                                                    zhoda += 1
                                                                
                                                                #6
                                                                if slovo[4] == slovo[6] and slovo[5] == "1":
                                                                    zhoda += 1
                                                                elif slovo[4] != slovo[6] and slovo[5] == "0":
                                                                    zhoda += 1

                                                                #7

                                                                #8
                                                                if "1111" in slovo and slovo[7] == "1":
                                                                    zhoda +=1
                                                                elif "1111" not in slovo and slovo[7] == "0":
                                                                    zhoda +=1

                                                                #9
                                                                if "101" not in slovo and slovo[8] == "1":
                                                                    zhoda +=1
                                                                elif "101" in slovo and slovo[8] == "0":
                                                                    zhoda +=1
                                                                
                                                                #10
                                                                
                                                                #11
                                                                if "1001" in slovo and slovo[10] == "1":
                                                                    zhoda +=1
                                                                elif "1001" not in slovo and slovo[10] == "0":
                                                                    zhoda +=1
                                                                
                                                                #12
                                                                if "0" not in slovo[12:] and slovo[11] == "1":
                                                                    zhoda += 1
                                                                elif "0" in slovo[12:] and slovo[11] == "0":
                                                                    zhoda += 1

                                                                #13
                                                                if "01" not in slovo and slovo[12] == "1":
                                                                    zhoda +=1
                                                                elif "01" in slovo and slovo[12] == "0":
                                                                    zhoda +=1
                                                                
                                                                #14
                                                                if slovo[12] != slovo[14] and slovo[13] == "1":
                                                                    zhoda += 1
                                                                elif slovo[12] == slovo[14] and slovo[13] == "0":
                                                                    zhoda += 1
                                                                
                                                                #15
                                                                if slovo[13] != slovo[15] and slovo[14] == "1":
                                                                    zhoda += 1
                                                                elif slovo[13] == slovo[15] and slovo[14] == "0":
                                                                    zhoda += 1
                                                                
                                                                #16
                                                                if "1100" in slovo and slovo[12] == "1":
                                                                    zhoda +=1
                                                                elif "1100" not in slovo and slovo[12] == "0":
                                                                    zhoda +=1


                                                                if zhoda == 14: # spravna odpoved 0001010000100110
                                                                    print(slovo)