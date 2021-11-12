import time
import random

NUM_FILES = 10


def seed():
    def genfile(idx):
        filename = f'integers-{idx}.txt'
        with open(filename, "w") as file:
            intcount = random.randint(5, 10)
            for _ in range(0, intcount):
                randint = random.randint(100, 1000)
                file.writelines([randint.__str__(), '\n'])

    for idx in range(1, NUM_FILES + 1):
        genfile(idx)


if __name__ == "__main__":
    seed()

def second_function(filename):
    total1=0
    with open(filename, 'r') as inp:
      for line in inp:
       try:
           num = float(line)
           total1 += num
       except ValueError:
           print('{} is not a number!'.format(line))
    
    print('Total of all numbers: {}'.format(total1))
    time.sleep(0.00001)

#for testing
#print (second_function("D:/Centennial Semester 5/Networking Soft/COMP216-Group11-Assignment1-UsingThreads/COMP216-Group11-Assignment1-UsingThreads/integers-5.txt"))
