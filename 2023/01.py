def get_number(x):
    '''
    get the first and last digits of a string object
    '''

    number = '' 
    for i in x : 
        try : 
            number += str(int(i))
            break 
        except : 
            pass 


    for i in x[::-1] : 
        try : 
            number += str(int(i))
            break 
        except : 
            pass 

    return int(number)


#read the input data
with open('2023/input/01.txt', 'r') as f : 
    content = f.read().split('\n')

#return the sum
print(sum([get_number(x) for x in content]))
