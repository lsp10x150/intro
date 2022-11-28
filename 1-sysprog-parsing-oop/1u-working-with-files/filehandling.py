import sys

animal_to_search = sys.argv[1]
f = open('animals.txt', 'r')
i = 1
for line in f:
	if line.find(animal_to_search) != -1:
		print(f'#{i} {line}', end='')
	i += 1
f.close()
