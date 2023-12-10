with open('input/04.txt', 'r') as f : 
    raw_content = f.read()

clean_content = raw_content.split('\n')

winners = [x.split(':')[1].split('|')[0].strip().replace('  ',' ').split(' ') for x in clean_content]
luckies = [x.split(':')[1].split('|')[1].strip().replace('  ',' ').split(' ') for x in clean_content]

sum_card_values = 0

for card in zip(winners,luckies):
    www, lll = card 

    card_value = 0
    for w in www : 
        if w in lll : 
            card_value = max(card_value*2,1)
    
    sum_card_values += card_value


print(sum_card_values)