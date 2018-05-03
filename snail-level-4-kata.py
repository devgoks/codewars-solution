def snail(array):
  result=[]
  while (len(array)):
    if(result):
#gets top row 
        result+=array.pop(0) 
    else:
#gets first top row
        result=array.pop(0)
#gets far right column
    for i in range(len(array)):
      result.append(array[i].pop())
    if(array):
#gets bottom row and reverses it
        result += reversed(array.pop())
#gets far left column
    for i in range(1,len(array)):
      result.append(array[len(array)-i].pop(0))
  return result;