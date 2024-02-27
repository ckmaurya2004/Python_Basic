import argparse
import sys

def calc(args):
    if args.o =="add":
        return args.x+args.y
    if args.o =="sub":
        return args.x-args.y
    if args.o =="mul":
        return args.x*args.y
    if args.o =="div":
        return args.x/args.y
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type= float,default=0.1)
    parser.add_argument('--y',type= float,default=0.5)
    parser.add_argument('--o',type = str,default="add")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))