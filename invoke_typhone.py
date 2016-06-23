# read config_txt.proto and make config_xml.proto


config_txt = open("config_txt.proto", 'r', encoding="utf8")
config_xml = open("config_xml.proto", 'w', encoding="utf8")

target_lines = [
	r'File = "IO/output.txt";',
	r'		Format = text;'
]

for line in config_txt:
	if target_lines[0] in line:
		print(line)
	if target_lines[1] in line:
		print(line)