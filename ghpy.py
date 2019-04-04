#!/usr/bin/env python3
import argparse
import sys
import commands

def switch(action_type):
    if (action_type == 'new'):
        commands.new.parse_new()
    elif (action_type == 'rm'):
        commands.rm.parse_rm()

switch(sys.argv[1])