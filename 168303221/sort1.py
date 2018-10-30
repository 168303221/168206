def BinarySearch(arr, key):

      min = 0
    max = len(arr) - 1
 
   if key in arr:

       while True:

            center = int((min + max) / 2)
             if arr[center] > key:
             max = center - 1
            elif arr[center] < key:
                 min = center + 1
           elif arr[center] == key:
                print(str(key) + "在数组里面的第" + str(center) + "个位置")
                return arr[center]
    else:
        print("没有该数字!")
