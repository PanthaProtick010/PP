import string

with open("D://Python//Files//poems.txt", "r") as f1:
    m = {}
    for line in f1:
        words = line.split()
        for word in words:
            word = word.lower()
            empty = ""
            for myChar in word:
                if myChar in string.ascii_letters:
                    empty += myChar
                else:
                    if empty:
                        if empty in m:
                            m[empty] += 1
                        else:
                            m[empty] = 1
                    empty = ""
            if empty:
                if empty in m:
                    m[empty] += 1
                else:
                    m[empty] = 1
max_occurance=0
for item in m:
    if(m[item]>=max_occurance):
        max_occurance=m[item]
for item in m:
    if(m[item]==max_occurance):
        print("The word with max occurance",item,":",str(max_occurance))
