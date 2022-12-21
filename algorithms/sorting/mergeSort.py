    def mergeSort(arr):
        if len(arr) > 1:
 
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
 
            mergeSort(sub_array1)
            mergeSort(sub_array2)
         
            i = j = k = 0
 
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
 
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
 
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
 
    arr = [10, 9, 2, 4, 6, 13]
    mergeSort(arr)
    print(arr)
