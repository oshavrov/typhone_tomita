import re
import subprocess

DATE_TEMPLATE = re.compile(r'\d{2}\.\d{2}\.\d{4}')
XML_CONFIG_NAME = "config_xml.proto"

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

def threat_dates_in_input(input_filename, output_filename):
    f = open(input_filename, "r", encoding="utf8")
    preprocessed_input = open(output_filename, "w", encoding="utf8")

    date_string = ""
    for line in f.read().splitlines():
        if re.match(DATE_TEMPLATE, line) is not None:
            date_string = line
        else:
            if line:
                preprocessed_input.write(date_string + " " + line + "\n")
            else:
                print("blank line found > ", line)
    f.close()
    preprocessed_input.close()


def preprocess_input():
    threat_dates_in_input("IO/manual_input.txt", "IO/preprocessed_input.txt")

def run_tomita():
    subprocess.call(["tomitaparser.exe", XML_CONFIG_NAME])

def invoke():
    move_txt_config_to_xml_one()
    preprocess_input()
    run_tomita()



if __name__ == "__main__":
    invoke()
    