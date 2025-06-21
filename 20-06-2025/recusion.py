#recusion:A function called by itself
#Syntax:
'''def function_name(Parameters):
    if base_condition:
        return result
    return function_name(modified_name)'''
def add_list  (n,sum):
    if bool(n): 
        sum=sum+n
        return add_list(n-1,sum)
    return sum
print(add_list(5,0))