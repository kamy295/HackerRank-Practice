#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 6):
            print("not wired")
        elif n in range(6, 21):
            print("weird")
        elif n > 20:
            print("not weird")
