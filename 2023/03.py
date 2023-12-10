with open('input/03.txt', 'r') as f : 
    raw_content = f.read()

content = [list(x) for x in raw_content.split('\n')]


def get_line_numbers(line,row=0):
    numbers = []
    number = ''
    for i,x in enumerate(line):
        try: 
            number += str(int(x))
            if len(number) == 1 : 
                start = i 
            end = i
        except : 
            if number != '' : 
                numbers.append((number, start, end, row))
                number = ''
        
        if i==len(line)-1 and number!='':
            numbers.append((number, start, end, row))
    
    return numbers


def get_number_perimeter(numbers_from_line, content):
    number, start, end, row = numbers_from_line
    limit_x = len(content[0])-1
    limit_y = len(content)-1

    perimeter = []
    p_start = max(0,start-1)
    p_end = min(limit_x,end+1)

    if row-1 >= 0 : 
        perimeter += content[row-1][p_start:p_end+1]
    
    if start != p_start : 
        perimeter += [content[row][p_start]]

    if end != p_end : 
        perimeter += [content[row][p_end]]
    
    if row+1 <= limit_y : 
        perimeter += content[row+1][p_start:p_end+1]

    return perimeter 

def get_number_value(number, perimeter):
    perimeter = list(set(perimeter)) 

    if perimeter == ['.'] : 
        return 0 
    
    for digit in [str(x) for x in range(1,10)]:
        while digit in perimeter:
            perimeter.remove(digit)
    
    if perimeter == ['.'] : 
        return 0 
    else : 
        return int(number)


number_positions = []
for row, line in enumerate(content) : 
    number_positions += get_line_numbers(line,row=row)

sum_valid_numbers = 0
for n_p in number_positions : 
    number = n_p[0]
    number_perimeter = get_number_perimeter(n_p, content)
    number_value = get_number_value(number, number_perimeter)
    sum_valid_numbers += number_value


print(sum_valid_numbers)
