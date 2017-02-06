import os
import re

XML_CONFIG_NAME = os.path.normpath(r'config_xml.proto')
TEXT_INPUT = os.path.normpath(r'IO/manual_input.txt')
TEXT_OUTPUT = os.path.normpath(r'IO/preprocessed_input.txt')

SOURCE_DATE_TEMPLATE = re.compile(r'(\d{2})(?:/|\.)(\d{2})(?:/|\.)((1[6-9])|(\d{4})).?')
INSIDE_DATE_TEMPLATE = re.compile(r'\d{2}/\d{2}/\d{4}')

DATE_TEMPLATE = re.compile(r'\d{2}.\d{2}.\d{4}')

# For classifier
INPUT_FILE = os.path.normpath(r'IO\output.xml')
PREPROCESSED_INPUT = os.path.normpath(r'IO\preprocessed_input.txt')
OUTPUT_EXCEL = os.path.normpath(r'IO\report.xlsx')
SAME_CATEGORY_DELIMITER = r'__'
EMPTY_COLS = ["Комплектация", "Цена клиента", "Наша цена", "Утилизация", "Решение клиента"]
