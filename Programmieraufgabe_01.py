"""
Coding Problem:
----------------------
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
                   
In contrast to the problem the pair is returned. 
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
