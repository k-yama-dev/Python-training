array = [3, 9, 4, 1, 7, 5, 2, 8]
i = array[0]
j = array[i + 1]
t = None
for i in array:
    if i < len(array) - 1:
        i += 1
        for j in array:
            if j < len(array):
                j += 1
                if i > j:
                    t = i
                    i = j
                    j = t
print(array)


arrayi = [3, 9, 4, 1, 7, 5, 2, 8]
for i in range(len(arrayi) - 1):
    for j in range(i + 1, len(arrayi)):
        if arrayi[i] > arrayi[j]:
            t = arrayi[i]
            arrayi[i] = arrayi[j]
            arrayi[j] = t
print(arrayi)
