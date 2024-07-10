# -*- coding: utf-8 -*-
"""
Some constants for carbatpy usage are set here

* The two (!) Refprop installation directories (with dll, fluids etc.)
* he directory, where the results shall be written.

Created on Sun Nov  5 16:01:02 2023

@author: atakan
"""

import os
# global _T_SURROUNDING, _P_SURROUNDING, _RESULTS_DIR, _CARBATPY_BASE_DIR
_T_SURROUNDING = 288.15 # K
_P_SURROUNDING =1.013e5  # Pa
_TREND = {"USE_TREND":False, "TREND_DLL":"", 'TREND_PATH':""}

directory = os.getcwd()
try:
    _CARBATPY_BASE_DIR = os.environ["CARBATPY_BASE_DIR"]
except:
    _CARBATPY_BASE_DIR = directory

# The two installations of REFPROP , one for the working fluid
# and one for the secondary fluid. With only one installation, the instances
# mix up ...
os.environ['RPPREFIX'] = r'C:/Program Files (x86)/REFPROP'
os.environ['RPPREFIXs'] = r'C:/Program Files (x86)/REFPROP/secondCopyREFPROP'
if _TREND["USE_TREND"]:
    try:
        _TREND["TREND_DLL"] = os.environ['TREND_DLL']
        _TREND["TREND_PATH"] = os.environ['TREND_PATH']
    except:
        print("Trend not found! Check the environmentvariable TREND_DLL, TREND_PATH")
        _TREND_DLL = ""
        _TREND_PATH = ''
    
try:
    _RESULTS_DIR = os.environ['CARBATPY_RES_DIR']
except:
    try:
        _RESULTS_DIR = os.environ['TEMP']
    except:
        try:
            
            _RESULTS_DIR = directory + r"\\tests\\test_files"
        except Exception as no_file:
            print("Please set the envirionment variable: CARBATPY_RES_DIR !", no_file)