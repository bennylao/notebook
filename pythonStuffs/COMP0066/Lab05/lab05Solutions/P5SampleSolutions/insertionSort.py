import time


def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element


unsorted_list  = [64, 34, 25, 12, 22, 11, 90]

start_time = time.time()
sorted(unsorted_list )
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
insertion_sort(unsorted_list )
print("--- %s seconds ---" % (time.time() - start_time))


