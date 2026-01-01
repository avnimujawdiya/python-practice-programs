list = [12,2,7,9,4]
even,odd = 0,0
for num in list:
    if num%2==0:
        even = even+1
    else:
        odd = odd+1
        print("even: ",even,"odd: ",odd)
