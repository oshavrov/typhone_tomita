import sys
import subprocess
import time
from python_modules import classifier
from python_modules import input_preprocessor
from python_modules.constants import XML_CONFIG_NAME

def run_tomita():
    subprocess.call(["tomitaparser.exe", XML_CONFIG_NAME])

def invoke():
    start = time.time()
    input_preprocessor.preprocess_input()
    run_tomita()
    classifier.classify()
    end = time.time()
    print("Затраченное время:", end - start, "сек.")

if __name__ == "__main__":
    invoke()