#!/usr/bin/env python3
import queue
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
    
q = queue.PriorityQueue()
fd = sys.stdin
if args.fd is not None:
  fd = open(args.fd)

try:
    for line in fd:
        v = random.random()
        t = (v,line.rstrip('\r\n'))
        # could compare against the known min in the queue
        q.put_nowait( t )
        # keep the queue to q.size() <= n
        while (q.qsize() > n):
            _ = q.get_nowait()
except KeyboardInterrupt as e:
    #print(str(e), file=sys.stderr)
    None
except IOError as e:
    #print(str(e), file=sys.stderr)
    None

# ensure we have only n or less
while (q.qsize() > n):
    _ = q.get_nowait()

while not q.empty():
    (v,l) = q.get_nowait()
    # print(f'{v} {len(l)} {l}')
    print(l)
