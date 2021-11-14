#Group 11
#Juneau Gawat
#Amir Shayan Armaghan
#Pablo Saldarriaga Gonzalez
#Nguyen Khang Nguyen
#Edgar Mejia Razo

import time
import random
import glob
import threading
import argparse

NUM_FILES = 10
total = 0


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

def third_function():
    time_start = time.perf_counter()
    for file in glob.glob('./*.txt'):
        second_function(file)
    time_stop = time.perf_counter()

    print(f'Number of files processed: {len(glob.glob("./*.txt"))} \nElapsed time in seconds: {time_stop - time_start}' )


def fourth_function():
    x = threading.Thread(target=third_function,args=())
    x.start()

#When executing the program, typing "python .\one.py -h" will prompt the instructions if needed.
parser = argparse.ArgumentParser()
parser.add_argument('--function', type=str, help='Hello. Type "--function seed" for create mode, or type "--function third_function" for serial mode, or type "--function fourth_function" for threaded mode ')
args = parser.parse_args()
userOption=args.function
if args.function == "seed":
    print(seed())
    print("Create Mode")
if args.function == "third_function":
    print(third_function())
    print("Serial Mode")
if args.function == "fourth_function":
    print(fourth_function())
    print("Threaded Mode")
