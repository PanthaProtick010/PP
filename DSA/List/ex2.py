heros=['spider man','thor','hulk','iron man','captain america']
print("The length of the list is:",str(len(heros)))
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3,"black panther")
heros[1:3]=["doctor strange"]
print(heros)
heros.sort()
print(heros)