import random

from sqlalchemy import false


PrisonerNum = random.sample(range(100),100);
BoxNum = random.sample(range(100),100);
found = false;
numFound = 0;
boxValue = 0;
numsDictionary = {};
for i in BoxNum:
    numsDictionary[BoxNum[i]] = PrisonerNum[i];
#print(numsDictionary);

for i in PrisonerNum:
    for j in range(1,50):
        boxValue = numsDictionary[i];
        if boxValue == i:
            ++numFound;
