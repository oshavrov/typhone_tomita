import os.path
import shutil
import re
from python_modules.constants import *

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
    file_iterator = f.read().splitlines()

    for line in file_iterator:
        if re.match(SOURCE_DATE_TEMPLATE, line) is not None:
            date_string = re.sub(SOURCE_DATE_TEMPLATE, r'\1/\2/\3', line);
        else:
            if re.match(r'.{3}', line):
                prepared_string = date_string + " " + line
                print(prepared_string, file=preprocessed_input)
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
            print(without_dots + '.', file=preprocessed_input)
    f.close()
    preprocessed_input.close()
    shutil.move(output_filename, input_filename);

def preprocess_input():
    move_txt_config_to_xml_one()
    threat_dates_in_input()
    replace_dots_in_line()
 
if __name__ == "__main__":
    preprocess_input() 