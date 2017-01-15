import math
def my_sd_function(numbers): 
    'my_sd_function' #docstring 
    N=len(numbers) 
    S1=0 
    S2=0 
    for num in numbers: 
        S1+=num 
    mu=S1/N 
    for num in numbers: 
        S2+= (num-mu)**2 
    return math.sqrt(S2/N)

my_list=range(1,6) 
print(my_sd_function(my_list))