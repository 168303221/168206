list = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
 def find(list,aim):
     mid = len(list)//2
    if list[mid] > aim:
        new_l = list[:mid]
       find(new_l,aim)
    elif list[mid] < aim:
        new_l = list[mid+1:]
        find(new_l, aim)
   elif list[mid] == aim:
        print('找到了:',mid,aim,l[mid])
 find(l,66)
