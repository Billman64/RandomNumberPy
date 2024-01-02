import random
import sys

# Arguments:
#  max, min, suppress


max = 6 # defaults - comparable to rolling dice
min = 1
outputMsg = "Random number:\n"

# check arguments for max and min values
if (len(sys.argv)>1):
        max = int(sys.argv[1])
        #if sys.argv[2]:
         #   min = int(sys.argv[2])
          #  print("min: " + str(sys.argv[2]))
        #if sys.argv[3]:
         #   outputMsg = ""
            
# generate random number
#r = int(round(random() * max + min, 0))
r = random.randint(min,max)


# output
print(outputMsg + str(r))






# experimental scrap code
#r = random.randint(0,255)

