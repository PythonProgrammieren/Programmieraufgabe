"""
Programmieraufgabe:
----------------------
Angenommen man hat 2 Input für eine Funktion. Der erste Input ist eine Liste von Integer. 
Der zweite Input ist ein Integer k. Schreibe eine Funktion welche checkt ob 2 Zahlen innerhalb der Liste
addiert k ergeben.

Zum Beispiel [10, 15, 3, 7] und k = 17, sollte true sein da since 10 + 7 = 17.
                    
@author: Python-Programmieren.com
"""


def hasPair(number_list, sum_k):
    
    mDict = []
    mPair = []
    
    for number in number_list:
        if number in mDict:
            mPair = [number, sum_k - number]
            break        
        else:
            mDict.append(sum_k - number)
    
    return mPair


if(__name__ == "__main__"):
    
    number_list = [10, 15, 3, 7]
    
    sum_k = 17
    
    print(hasPair(number_list, sum_k))
