import sys
import os
import contextlib

with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
    import pygame
