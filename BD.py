import random

alphabet = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
DB = []
for i in alphabet:
    for j in alphabet:
        DB.append(f"{i}омбили {j}омбас")

for i in range(len(DB)):
    print(random.choice(DB))
