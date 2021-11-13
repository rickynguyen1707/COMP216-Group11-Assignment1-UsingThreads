import time
import random
import glob
import threading

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

def third_function():
    time_start = time.perf_counter()
    for file in glob.glob('./*.txt'):
        second_function(file)
    time_stop = time.perf_counter()

    print(f'Number of files processed in parallel: {len(glob.glob("./*.txt"))} \nElapsed time in seconds: {time_stop - time_start}' )

#test third_function
#print(third_function())

def fourth_function():
    x = threading.Thread(target=third_function,args=())
    x.start()

#test fourth_function
'''
print(fourth_function())
print("text22222 should be inbetween total numbers")
time.sleep(0.021)
print("text33333 should be inbetween total numbers")
time.sleep(0.03)
print("text4444 should be inbetween total numbers")
'''
