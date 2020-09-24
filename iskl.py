import random

def cut_cake(people):
    try:

        z = 1 / people
        
        print(f"Каждый получит {z} пирога")
    except:
   
        print('Программа принимает только числа')

while True:
    z = random.randint(1,10)   

    cut_cake(z)