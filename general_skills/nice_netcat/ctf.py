import subprocess

# read netcat
result = subprocess.run(["nc", "mercury.picoctf.net", "35652"], stdout=subprocess.PIPE, text=True)
output = result.stdout

# split lines
lines = output.splitlines()

# convert chars to int
modified_lines = [int(item[:-1]) for item in lines]
char_list = [chr(i) for i in modified_lines]

# print message
print(''.join(char_list), end='')