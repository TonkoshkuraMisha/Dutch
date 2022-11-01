import time
from colorama import Fore

for i in range(2, 1_001):
	for j in range(1, 101):
		print(Fore.GREEN + f"{i}**{j} = {pow(i, j)}")
		time.sleep(0.4)
