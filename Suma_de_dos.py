def suma_dos_num(array, num_obj):
    for i in range(len(array) - 1):
        primer_num = array[i]
        for j in range(i + 1, len(array)):
            segundo_num = array[j]
            if primer_num + segundo_num == num_obj:
                return [primer_num, segundo_num]
    return []


##################################################
def suma_dos_num_v2(array, num_obj):
    hash_table = {}
    for num in array:
        if num_obj - num in hash_table:
            return [num_obj - num, num]
        else:
            hash_table[num] = True
    return []

##################################################


def suma_dos_num_v3(array, num_obj):
    array.sort()
    izq = 0
    der = len(array) - 1
    while izq < der:
        suma_actual = array[izq] + array[der]
        if suma_actual == num_obj:
            return [array[izq], array[der]]
        elif suma_actual < num_obj:
            izq += 1
        elif suma_actual > num_obj:
            der -= 1
    return []
