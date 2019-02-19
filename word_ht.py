
user_input = input('Please enter a sentence: ')
lower = user_input.lower()
split = lower.split()

top_count = {}

for x in split:
    top_count[x] = top_count.get(x, 0) + 1

print(top_count)