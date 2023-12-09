def get_line_digits(line):
    digits = ''
    for i, y in enumerate(line) : 
        try : 
            digits += str(int(y))
        except : 
            for j, digit_string in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
                if line[i:i+len(digit_string)] == digit_string : 
                    digits += ['1','2','3','4','5','6','7','8','9'][j]
    
    return digits

def get_calibration_code(digits):
    return int(digits[0]+digits[-1])

def get_sum_codes(content):
    sum_codes = 0
    for line in content : 
        digits = get_line_digits(line)
        number = get_calibration_code(digits)
        sum_codes += number 
    
    return sum_codes 



#read the input data
with open('input/01.txt', 'r') as f : 
    content = f.read().split('\n')


print(get_sum_codes(content))