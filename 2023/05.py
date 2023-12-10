with open('input/05.txt', 'r') as f : 
    raw_content = f.read()

seeds = [int(x) for x in raw_content.split('\n\n')[0].split(':')[1].strip().split(' ')] 
converters = [[[int(y) for y in x.split(' ')] for x in line.split(':')[1].strip().split('\n')] for line in raw_content.split('\n\n')[1:]]

location_list = []

for seed in seeds : 
    converted_seed_nr = seed 
    for convertions in converters : 
        for rule in convertions:
            dest_start,source_start,conv_range = rule 
            if  source_start <= converted_seed_nr <= source_start + conv_range : 
                converted_seed_nr = converted_seed_nr - source_start + dest_start 
                break

    location_list.append(converted_seed_nr)

print(min(location_list))