Aim:Given the participants' score sheet for your University Sports Day,
    you are required to find the runner-up score. You are given scores.
    Store them in a list and find the score of the runner-up.
list1 = [10, 20, 4, 45, 99] 
max=max(list1[0],list1[1]) 
secondmax=min(list1[0],list1[1]) 
  
for i in range(2,len(list1)): 
    if list1[i]>max: 
        secondmax=max
        max=list1[i] 
    else: 
        if list1[i]>secondmax: 
            secondmax=list1[i] 
  
print("Second highest number is : ",str(secondmax)) 
