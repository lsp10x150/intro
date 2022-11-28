a_map = dict()
with open('alice_in_wonderland.txt', 'r') as f:
    for line in f:
        for word in line.split(' '):
            word = word.strip().lower()
            if word == '':
                continue
            if word in a_map:
                a_map[word] += 1
            else:
                a_map.update({word: 1})
n_print = 10
for k, v in reversed(sorted(a_map.items(), key=lambda item: item[1])):
    print(k, v)
    n_print -= 1
    if n_print == 0:
        break