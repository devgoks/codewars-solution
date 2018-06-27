def find_missing(sequence):
    diff=sequence[1]-sequence[0]
    diff2=sequence[-1]-sequence[-2]
    count=diff < diff2
    if(count == True): count=diff
    if(count == False): count=diff2 
    for i in range(0,len(sequence)-1):       
            if(sequence[i+1] !=sequence[i] + count): 
                 return  sequence[i] + count   