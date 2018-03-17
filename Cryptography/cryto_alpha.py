#cryto -> alpha
f = open("write_cryto.txt",'r')
input_string_sec = f.read()
input_string_sec = input_string_sec.split('/')
random_variable = ""
for x in input_string_sec :
	num = int(x)
	output_alpha = chr(num)
	random_variable += output_alpha
print(random_variable)