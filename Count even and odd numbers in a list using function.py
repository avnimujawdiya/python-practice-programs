def count_even_odd(lst):
    even,odd =0,0
    for num in lst:
        if num%2==0:
            even +=1
        else:
            odd+=1
    return even,odd
lst = [6,3,7,9,8]
even,odd = count_even_odd(lst)
print("even:",even,"odd",odd)