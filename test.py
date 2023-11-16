import random




def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

odds_count = 0


times = 10000000
for i in range(times):
    odds = [random.randint(1, 10),
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        # random.randint(1, 10),
        # random.randint(1, 10)
        ]
    
    if all_equal(odds):
        odds_count += 1
    

print(f"equal {odds_count} - range of {times}")