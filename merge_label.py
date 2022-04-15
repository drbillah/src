import os
from glob import glob

test = open("/home/mbillah/Lab/stdDetector/test.txt")
train = open("/home/mbillah/Lab/stdDetector/train.txt")

test_class = test.readlines()
train_class = train.readlines()

test_wider = glob(os.path.join("/home/mbillah/Lab/stdDetector/pubVal","*.jpg"))
train_wider = glob(os.path.join("/home/mbillah/Lab/stdDetector/pubTrain","*.jpg"))

f_test = test_class + test_wider
f_train = train_class + train_wider

f1 = open("final_train.txt", 'w')
f2 = open("final_test.txt", 'w')

for sample in f_train:
    sample = sample.strip()
    f1.write("{}\n".format(os.path.basename(sample)))
    
for sample in f_test:
    sample = sample.strip()
    f2.write("{}\n".format(os.path.basename(sample)))

f1.close()
f2.close()
