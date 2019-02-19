
txt = input('Please enter a sentence: ')
small_text = txt.lower()
txt2 = small_text.split()
count = dict()

for x in txt2:
    count[x] = count.get(x, 0) + 1

print(count)
