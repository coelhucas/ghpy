import argparse
import utils

_all_ = ['parse_collab']

def parse_collab(args):
    parser = argparse.ArgumentParser(description='Controls github from your terminal.')
    #args = parser.parse_args()
    if args[0] == utils.io.add:
        print('Adding + to your clip')