
from cgi import test
import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    half = int(len(testcase)/2) #split test case in half

    if firstHalf: #sort first half of shared list 
        unsortedFirstHalf = testcase[:half] #initialize first half of unsorted list

        for i in range (0,half): #for loop to cycle through half of test case
            firstHalfMin = i #initialize index to find smallest value in list

            for j in range (i+1,half): 
                if unsortedFirstHalf[j] < unsortedFirstHalf[firstHalfMin]: #compare each number in the list 
                    firstHalfMin = j #if true, j will be the index for the smallest number

            if i != firstHalfMin: #if i index and smallest index in the first half is not the same
                unsortedFirstHalf[i], unsortedFirstHalf[firstHalfMin] = unsortedFirstHalf[firstHalfMin], unsortedFirstHalf[i] #swap numbers in the unsorted list 

            sortedFirstHalf.append(unsortedFirstHalf[i]) #append smallest value to sorted list
        

    if not firstHalf: #sort second half of shared  list
        unsortedSecondHalf = testcase[half:] #initialize second half of unsorted list

        for x in range (0, half):
            secondHalfMin = x

            for y in range(x+1, half):
                if unsortedSecondHalf[y] < unsortedSecondHalf[secondHalfMin]:
                    secondHalfMin = y
            
            if x != secondHalfMin:
                unsortedSecondHalf[x], unsortedSecondHalf[secondHalfMin] = unsortedSecondHalf[secondHalfMin], unsortedSecondHalf[x]   

            sortedSecondHalf.append(unsortedSecondHalf[x])

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    unsortedFullList = sortedFirstHalf + sortedSecondHalf #initilize unsorted full list for sorting
    length = len(unsortedFullList)

    for i in range(0, length):
        min = i
        for j in range(i+1, length):
            if unsortedFullList[j] < unsortedFullList[min]:
                min = j
        
        if i != min:
            unsortedFullList[i], unsortedFullList[min] = unsortedFullList[min], unsortedFullList[i]

        SortedFullList.append(unsortedFullList[i])

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    #testcase = [1,343,1123,2,152,124,51,211]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #start sorting using mergingWorker
    firstHalfThread = threading.Thread(target=sortingWorker,args=(True,)) #thread to sort first half
    secondhalfThread = threading.Thread(target=sortingWorker,args=(False,)) #thread to sort second half

    firstHalfThread.start()
    secondhalfThread.start()

    firstHalfThread.join()
    secondhalfThread.join()

    #wait for sortingWorker to join before starting mergingWorker
    mergeThread = threading.Thread(target=mergingWorker)
    mergeThread.start()
    mergeThread.join()
    
    #print(sortedFirstHalf)
    #print(sortedSecondHalf)
    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)