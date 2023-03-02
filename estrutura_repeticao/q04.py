pop_a = 80000
pop_b = 200000
anos_nec = 0
    
while pop_a <= pop_b:
    pop_a += ((pop_a * 3) / 100)
    pop_b += ((pop_b * 1.5) / 100)
    anos_nec += 1

print(f'Anos necessários para que população do país \'A\' alcance a população do país \'B\' = {anos_nec}')
