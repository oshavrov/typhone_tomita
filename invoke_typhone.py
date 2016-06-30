import re
import subprocess
import sys
import classifier
import time
import os.path
import shutil

SOURCE_DATE_TEMPLATE = re.compile(r'(\d{2})\.(\d{2})\.(\d{4}).?')
INSIDE_DATE_TEMPLATE = re.compile(r'\d{2}/\d{2}/\d{4}')

XML_CONFIG_NAME = "config_xml.proto"
TEXT_INPUT = os.path.normpath(r"IO/manual_input.txt")
TEXT_OUTPUT = os.path.normpath(r'IO/preprocessed_input.txt')

def move_txt_config_to_xml_one():
    config_txt = open("config_txt.proto", 'r', encoding="utf8")
    config_xml = open(XML_CONFIG_NAME, 'w', encoding="utf8")

    output_filename = r'File = "IO/output.txt";'
    output_type = r'Format = text;'

    for line in config_txt:
        if output_filename in line:
            line = line.replace(output_filename, r'File = "IO/output.xml";')
        if output_type in line:
            line = line.replace(output_type, r'Format = xml;')
        config_xml.write(line)

def threat_dates_in_input(input_filename=TEXT_INPUT, output_filename=TEXT_OUTPUT):
    f = open(input_filename, "r", encoding="utf8")
    preprocessed_input = open(output_filename, "w", encoding="utf8")

    date_string = ""
    for line in f.read().splitlines():
        if re.match(SOURCE_DATE_TEMPLATE, line) is not None:
            date_string = re.sub(SOURCE_DATE_TEMPLATE, r'\1/\2/\3', line);
        else:
            if line:
                prepared_string = date_string + " " + line
                preprocessed_input.write(prepared_string + "\n")

            
    f.close()
    preprocessed_input.close()


def replace_dots_in_line(input_filename=TEXT_OUTPUT):
    f = open(input_filename, "r", encoding="utf8")
    output_filename = input_filename + ".tmp"
    preprocessed_input = open(output_filename, "w", encoding="utf8")
    without_dots = ""
    for line in f.read().splitlines():
        if re.match(INSIDE_DATE_TEMPLATE, line):
            without_dots = re.sub(r'т\.р\.?', r'тр', line)
            without_dots = re.sub(r'(р)(\.)(\s?)', r'\1 \3', without_dots)
            without_dots = re.sub(r'\s{2,}', r' ', without_dots)
            without_dots = re.sub(r'(\d)\.(\d)', r'\1,\2', without_dots)
            without_dots = re.sub(r'\.(.)', r' \1', without_dots)
            # make date with dots back
            without_dots = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\1.\2.\3', without_dots)
            print(without_dots)
            preprocessed_input.write(without_dots + ".\n")
    f.close()
    preprocessed_input.close()
    shutil.move(output_filename, input_filename);

def preprocess_input():
    threat_dates_in_input()
    replace_dots_in_line()
    

def run_tomita():
    subprocess.call(["tomitaparser.exe", XML_CONFIG_NAME])


def invoke():
    start = time.time()
    move_txt_config_to_xml_one()
    preprocess_input()
    run_tomita()
    classifier.classify()
    end = time.time()
    print("Затраченное время:", end - start, "сек.")

if __name__ == "__main__":
    invoke()
    print()
    input("Нажмите Enter для выхода")
    