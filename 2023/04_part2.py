with open('input/04.txt', 'r') as f : 
    raw_content = f.read()

clean_content = raw_content.split('\n')

initial_results = []
for line in clean_content : 
    winners = line.split(':')[1].split('|')[0].strip().replace('  ',' ').split(' ')
    luckies = line.split(':')[1].split('|')[1].strip().replace('  ',' ').split(' ')
    hits = 0
    for w in winners : 
        if w in luckies : 
            hits += 1
    
    initial_results.append([1,hits])

final_results = initial_results[:].copy()

for i,result in enumerate(final_results): 

    current_card_copies, current_card_score = result 

    for x in range(i+1,i+current_card_score+1):
        final_results[x][0] += current_card_copies 


print(sum([x[0] for x in final_results]))