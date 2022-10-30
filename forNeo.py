import random
import time
from colorama import Fore

#
# def get_random_string():
#     out_list = [chr(j) for j in range(500, 10500)]
#     random.shuffle(out_list)
#     # symbol = random.choice(out_list)
#     out_string = ''.join(out_list)
#     return out_string
#
#
# for i in range(1, 10_000):
#     print(Fore.GREEN + get_random_string())

for j in range(1, 100_001):
    print(Fore.GREEN + f"{j}^{j} = {pow(j, j)}")
    time.sleep(1)

