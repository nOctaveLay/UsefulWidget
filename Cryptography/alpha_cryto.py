#alpha -> cryto
import os
input_string_sec = input("What are you carrying out? ")
while (input_string_sec == '\n' or input_string_sec == ' '):
	print("you didn't write anything.")
	print("plz write some strings.")
	wait(1)
	input_string_sec = input("What are you carrying out? ")
print("complete, Well done!")
print("your cryto code is...")
cryto_code = ''
for x in input_string_sec :
	cryto_code += str(ord(x))+"/"
cryto_code = cryto_code[:len(cryto_code)-1]
if not os.path.isdir("write_cryto.txt"):
	f = open("write_cryto.txt",'w')
else:
	f = open("write_cryto.txt",'w')
f.write(cryto_code)
f.close()
print("complete!")
