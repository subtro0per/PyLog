"""
Author: Tilman Steck
License: MIT License Copyright (C) 2021 Tilman Steck

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Informations:
    - The log files will be created in the path of the cmd window from which you are running your python script.
    - Write normal logs with 'pylog.writeLog(log_text)'
    - Write errro logs with 'pylog.writeError(log_error_text, error)'
    - Write placeholder logs with 'pylog.writePlaceholder(log_placeholder_text)'
    - This file has to be saved in 'your-dir/Python38-32/Lib/site-packages/pylog.py'
"""

import time
    
# function to write logs in the .log file
def writeLog(log_text):
    try:
        with open("log.txt", "a+") as logfile:
            logfile.write("\n[INFO] | " + time.strftime("%H:%M:%S") + " | " + log_text)

    except FileNotFoundError:   
        print(time.strftime("[%H:%M:%S]") + " | FileNotFoundError in pylog-module: log.txt does not exist")
    
    except Exception as err:
        print(time.strftime("[%H:%M:%S]") + " | Exception in pylog-module: " + str(err))


# function to write errors in the .log file
def writeError(log_error_text, error):
    try:
        with open("log.txt", "a+") as logfile:
            logfile.write("\n[ERROR] | " + time.strftime("%H:%M:%S") + " | " + log_error_text + ", Error Text: " + error)
    
    except FileNotFoundError:
        print(time.strftime("[%H:%M:%S]") + " | FileNotFoundError in pylog-module: log.txt does not exist")
    
    except Exception as err:
        print(time.strftime("[%H:%M:%S]") + " | Exception in pylog-module: " + str(err))


# function to write a placeholder text in for example empty functions
def writePlaceholder(log_placeholder_text):
    try:
        with open("log.txt", "a+") as logfile:
            logfile.write("\n[INFO] | " + time.strftime("%H:%M:%S") + " | PLACEHOLDER: " + log_placeholder_text)

    except FileNotFoundError:
        print(time.strftime("[%H:%M:%S]") + " | FileNotFoundError in pylog-module: log.txt does not exist")
    
    except Exception as err:
        print(time.strftime("[%H:%M:%S]") + " | Exception in pylog-module: " + str(err))