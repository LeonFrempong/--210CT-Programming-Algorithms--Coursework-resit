
def mergeSort(L):
    if len(L)> 1:
        mid = len(L)// 2
        A = L[:mid]
        B = L[mid:]

        mergeSort(A)
        mergeSort(B)

        i = j = k = 0

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                L[k] = L[i]
                i+=1
            else:
                L[k] = B[j]
                j+=1
            k+=1

        while i < len(A):
            L[k] = A[i]
            i+=1
            k+=1
        while j < len(B):
            L[k] = B[j]
            j+=1
            k+=1
        #the function below prints the list

def merge(L):
    for i in range(len(L)):
        print(L[i],end=" ")
    print()

if __name__ == '__main__':
    L = [12, 11, 13, 5, 6, 7]
    print ("The array given is", end="\n")
    merge(L)
    mergeSort(L)
    print("Sorted array is now: ", end="\n")
    merge(L)
            


 
