import sys
from random import random
## ZeroR - our first learning algorithm.
### assume that list_of_examples is a list of strings. For example:
### ['outlook,temperature,humidity,windy,play\n', 'sunny,hot,high,FALSE,no\n', 'sunny,hot,high,TRUE,no\n', 'overcast,hot,high,FALSE,yes\n', 'rainy,mild,high,FALSE,yes\n', 'rainy,cool,normal,FALSE,yes\n', 'rainy,cool,normal,TRUE,no\n', 'overcast,cool,normal,TRUE,yes\n', 'sunny,mild,high,FALSE,no\n', 'sunny,cool,normal,FALSE,yes\n', 'rainy,mild,normal,FALSE,yes\n', 'sunny,mild,normal,TRUE,yes\n', 'overcast,mild,high,TRUE,yes\n', 'overcast,hot,normal,FALSE,yes\n', 'rainy,mild,high,TRUE,no\n']
### your code should get the last element in each string, which is the classification, and return the most common one.

def zeroR(list_of_examples) :
    yesCount = 0
    totalCount = 0
    for line in list_of_examples[1:]:
        choice = line.strip().split(",")[-1]
        if choice == "yes":
            yesCount+=1
        totalCount+=1
    if yesCount > (totalCount/2):
        return "yes"
    else:
        return "no"
    #return "zeroR" # you fix this.

### assume that list_of_examples is a list of strings. For example:
### ['outlook,temperature,humidity,windy,play\n', 'sunny,hot,high,FALSE,no\n', 'sunny,hot,high,TRUE,no\n', 'overcast,hot,high,FALSE,yes\n', 'rainy,mild,high,FALSE,yes\n', 'rainy,cool,normal,FALSE,yes\n', 'rainy,cool,normal,TRUE,no\n', 'overcast,cool,normal,TRUE,yes\n', 'sunny,mild,high,FALSE,no\n', 'sunny,cool,normal,FALSE,yes\n', 'rainy,mild,normal,FALSE,yes\n', 'sunny,mild,normal,TRUE,yes\n', 'overcast,mild,high,TRUE,yes\n', 'overcast,hot,normal,FALSE,yes\n', 'rainy,mild,high,TRUE,no\n']
### your code should get the last element in each string, which is the classification, and use random.choice() to select one and return it

def randR(list_of_examples) :
    yesCount = 0
    totalCount = 0
    for line in list_of_examples[1:]:
        choice = line.strip().split(",")[-1]
        if choice == "yes":
            yesCount += 1
        totalCount += 1
    choiceNum = random.randint(1,11)
    if choiceNum>4:
        if yesCount>(totalCount/2):
            return "yes"
        else:
            return "no"
    else:
        if yesCount<(totalCount/2):
            return "yes"
        else:
            return "no"

    #return "randR" # you fix this.



## Our main. We should be able to run from the command line like so:
## python ZeroR.py tennis.csv
## python ZeroR.py -z tennis.csv
## python ZeroR.py -r tennis.csv

if __name__ == '__main__' :

    classify_type = "-z"
    if len(sys.argv) < 2:
        print("Usage:  classify {-z|-r} file")
        sys.exit(-1)
    if len(sys.argv) == 3 :
        classify_type = sys.argv[1]
        if classify_type != "-z" and classify_type != "-r" :
            print("Usage:  classify {-z|-r} file")
            sys.exit(-1)
    fname = sys.argv[-1]

    with open(fname) as f :
        data = f.readlines()
        if classify_type == "-z" :
            print(zeroR(data))
            ## change this to use ZeroR to find the most common classification, and then
            ## compare that value to the true classification for each line to compute accuracy.
            ## (fraction of answers that are correct.)
        else :
            print(randR(data))
            ## change this so that, for each line in the dataset, you are calling RandR to generate a prediction
            ## and comparing that to the actual classification. Use this to compute accuracy.
            ## (fraction of answers that are correct.)
