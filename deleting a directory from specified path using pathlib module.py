# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:39:07 2022

@author: TOBBY
"""
try:

    import pathlib

    # Deleting an empty folder
    empty_dir = r"C:/Users/TOBBY/Desktop/Python/Tobii_2.py"
    path = pathlib.Path(empty_dir)
    path.rmdir()

except FileNotFoundError:
    print("path does not exist")
else:
    print("Deleted '%s' directory successfully" % empty_dir)