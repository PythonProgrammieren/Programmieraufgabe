

# Python Programmieraufgabe 02
# 
# Programmieraufgabe:
#-----------------------------
# Man hat als Input einen Array von Integer. Schreibe eine Funktion welche einen neuen Array von Integer zurück gibt. 
# Die einzelnen Elemente des Arrays sollen das Produkt von allen Zahlen des urspünglichen Arrays sein, augenommen der 
# Zahl welche am selben Index ist.
#       
# Zum Beispiel, für den Input [1, 2, 3, 4, 5] wäre das Ergebnis [120, 60, 40, 30, 24]. 
# Für den Input [3, 2, 1] wäre das Ergebnis [2, 3, 6].
#
# Zusatz: Ist es möglich ohne Division zu lösen?
#
#    author: python-programmieren.com



# Solution with Division
def productArray_01(input_array):
    N = len(input_array)

    output_array = N*[1]

    prod = 1
    for i in range(N):
        prod *= input_array[i]

    for i in range(N):
        output_array[i] = int(prod/input_array[i])

    return output_array


# Solution without Division
def productArray_02(input_array):
    N = len(input_array)

    output_array = N*[1] 
    left_side = N*[1]
    right_side = N*[1]   
    
    for i in range(1, N):
        left_side[i] = input_array[i-1]*left_side[i-1]

    for i in range(N - 2, -1, -1):
        right_side[i] = input_array[i+1]*right_side[i+1]

    for i in range(N):
        output_array[i] = left_side[i] * right_side[i]

    return output_array



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]

    print(productArray_01(array))
    print(productArray_02(array))




