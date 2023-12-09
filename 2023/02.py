with open('input/02.txt', 'r') as f : 
    content = f.read().split('\n')

def get_game_value(game, red=0, green=0, blue=0):
    reveals = game.split(':')[1].strip().split(';')
    for reveal in reveals : 
        cube_sets = reveal.split(',') 
        for c_set in cube_sets : 
            colour = c_set.strip().split(' ')[1].strip()
            n_cubs = int(c_set.strip().split(' ')[0].strip())
            match colour : 
                case 'red' : 
                    if n_cubs > red : 
                        return 0 
                        
                case 'blue' : 
                    if n_cubs > blue : 
                        return 0 
                        
                case 'green' : 
                    if n_cubs > green : 
                        return 0 
    
    game_id = int(game.split(':')[0].split(' ')[1])
    return game_id

def get_sum_valid_games(content, red=0, green=0, blue=0):
    sum_game_ids = 0
    for game in content :
        sum_game_ids += get_game_value(game, red=red, green=green, blue=blue)
    
    return sum_game_ids
                        
red = 12
green = 13 
blue = 14 

result = get_sum_valid_games(content, red=red, green=green, blue=blue )

print(result)