numbers = [5,6,2,9,11,76,100,3,15,3]

highest = float('-inf');

for i in numbers:
	if i > highest:
		highest = i

print(highest)
