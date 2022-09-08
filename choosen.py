#!/usr/bin/env python3
import queue
import heapq
import argparse
import os
import random
import sys

def parse_args():
    parser = argparse.ArgumentParser(description=f'Stream Sampler')
    parser.add_argument('--seed', type=int, default=None, help='Seed of random number generator.')
    parser.add_argument('n', nargs='?', type=int, default=100, help='Sample N elements from the stream')
    parser.add_argument('fd', nargs='?', type=str, default=None, help='From STDIN or a file')
    return parser.parse_args()

args = parse_args()
our_seed = args.seed
n = int(args.n)

if our_seed is None:
    our_seed = random.randint(0,2**32-1)
else:
    our_seed = int(our_seed)
random.seed(our_seed)
    
# q = queue.PriorityQueue()
q = []
fd = sys.stdin
if args.fd is not None:
  fd = open(args.fd)

try:
    for line in fd:
        v = random.random()
        t = (v,line.rstrip('\r\n'))
        # could compare against the known min in the queue
        heapq.heappush(q,  t )
        # keep the queue to q.size() <= n
        while (len(q) > n):
            _ = heapq.heappop(q)
except KeyboardInterrupt as e:
    #print(str(e), file=sys.stderr)
    None
except IOError as e:
    #print(str(e), file=sys.stderr)
    None

# ensure we have only n or less
while (len(q) > n):
    _ = heapq.heappop(q)

while len(q) > 0:
    (v,l) = heapq.heappop(q)
    # print(f'{v} {len(l)} {l}')
    print(l)
