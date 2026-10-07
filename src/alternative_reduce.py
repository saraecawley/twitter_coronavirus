#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys',nargs='+',required=True)
parser.add_argument('--input_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# scan through data in outputs folder
daily = defaultdict(lambda: [])
filenames = sorted(os.listdir(args.input_folder))

for filename in filenames:
    if not filename.endswith('.lang'):
        continue
    path = os.path.join(args.input_folder,filename)
    with open(path) as f:
        tmp = json.load(f)

    for k in args.keys:
        if k in tmp:
            daily[k].append(sum(tmp[k].values()))
        else:
            daily[k].append(0)

# plot one line per input hashtag
for k in args.keys:
    x = range(1,len(daily[k])+1)
    plt.plot(x,daily[k],label=k)

plt.xlabel('Date')
plt.ylabel('Number of tweets w/ #')
plt.legend()
plt.savefig('alternative_reduce.png')
