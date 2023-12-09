def get_game_power(game):
    red, green, blue = 0, 0, 0 
    
    reveals = game.split(':')[1].strip().split(';')
    
    for reveal in reveals : 
        for cube_set in reveal.split(','):
            colour = cube_set.strip().split(' ')[1].strip() 
            n_cubes = int(cube_set.strip().split(' ')[0].strip())

            match colour : 
                case 'red':
                    red = max(red,n_cubes)
                case 'green':
                    green = max(green,n_cubes)
                case 'blue':
                    blue = max(blue,n_cubes)
    
    game_power = red*green*blue
    return game_power

def get_sum_game_power(content):
    sum_g_power = 0 

    for game in content : 
        sum_g_power += get_game_power(game)
    
    return sum_g_power


#read the input data
with open('input/02.txt', 'r') as f : 
    content = f.read().split('\n')


print(get_sum_game_power(content))