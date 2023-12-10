

def add_safety_layer(clean_content):
    clean_content = [['.'] + x + ['.'] for x in clean_content]
    #add first and last rows 
    clean_content = [['.' for _ in range(len(clean_content[0]))]] + clean_content 
    clean_content = clean_content  + [['.' for _ in range(len(clean_content[0]))]]

    return clean_content

def get_star_coordinates(clean_content):
    coordinates = [] 
    
    for i, line in enumerate(clean_content):
        indexes = [(i,j) for j,element in enumerate(line) if element == '*']
        coordinates += indexes

    return coordinates



def get_adjacent_numbers(coordinate,clean_content):
    x,y = coordinate

    frame_coordinates = [] 
    for coord1 in range(x-1, x+2):
        for coord2 in range(y-1, y+2):
            frame_coordinates.append((coord1,coord2))
    
    frame_coordinates.remove((x,y))

    n_digits_around = 0
    checked_coordinates = []
    number_1, number_2 = '', ''
    for c1,c2 in frame_coordinates : 
        try: 
            number_1 = str(int(clean_content[c1][c2]))
            checked_coordinates.append((c1, c2))
            for c3 in range(c2-1, -1, -1):
                try : 
                    number_1 = str(int(clean_content[c1][c3])) + number_1 
                    checked_coordinates.append((c1, c3))
                except : 
                    break 
            
            for c3 in range(c2+1,len(clean_content[0])):
                try : 
                    number_1 = number_1 + str(int(clean_content[c1][c3]))
                    checked_coordinates.append((c1, c3))
                except : 
                    break 
            break
        except : 
            pass 
    
    for c1,c2 in frame_coordinates : 
        if (c1,c2) not in checked_coordinates :
            try: 
                number_2 = str(int(clean_content[c1][c2]))
                checked_coordinates.append((c1, c2))
                for c3 in range(c2-1, -1, -1):
                    try : 
                        number_2 = str(int(clean_content[c1][c3])) + number_2
                        checked_coordinates.append((c1, c3))
                    except : 
                        break 
                
                for c3 in range(c2+1,len(clean_content[0])):
                    try : 
                        number_2 = number_2 + str(int(clean_content[c1][c3]))
                        checked_coordinates.append((c1, c3))
                    except : 
                        break 

            except : 
                pass 

    try : 
        return int(number_1)*int(number_2)
    except : 
        return 0 

    


with open('input/03.txt', 'r') as f : 
    raw_content = f.read()

clean_content = [list(x) for x in raw_content.split('\n')]

clean_content = add_safety_layer(clean_content)

print(sum([get_adjacent_numbers(coordinate,clean_content) for coordinate in get_star_coordinates(clean_content)]))


