#Implement Merge Sort and explain its performance using the Big O notation

import unittest
def test_int(self):
    self.assertEqual(11, 10, 12, 4, 5, 6)


def mergeSort(L):
    if len(L)> 1:
        mid = len(L)// 2 # finding out the mid of the array
        A = L[:mid]# A array is halfed 
        B = L[mid:]# B array is also halfed
        #the array elements have been divided 

        mergeSort(A) # this function callled the first half of the array
        mergeSort(B) # this function also called the second half of the array

        i = j = k = 0

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                L[k] = L[i]
                i+=1
            else:
                L[k] = B[j]
                j+=1
            k+=1
        #the while loop if there are any elemts left 
        while i < len(A):
            L[k] = A[i]
            i+=1
            k+=1
        while j < len(B):
            L[k] = B[j]
            j+=1
            k+=1
        #the function below prints the list
# ths function prints the list
def merge(L):
    for i in range(len(L)):
        print(L[i])
    print()
# the main function tests the code above
if __name__ == '__main__':
    L = [11, 10, 12, 4, 5, 6]
    print ("The array given is")
    merge(L)
    mergeSort(L)
    print("Sorted array is now: ")
    merge(L)

    unittest.main()
            


 
