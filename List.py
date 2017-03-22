
# Van-st
import time
start_time = time.time()
temp_list = []
sum_list = 0
print("computing the time....")
while True:
	input_sen = input("if you finish the work, you must input the message 'end': ")
	# if input_sen == 'a':
	# 	sum_list += 10
	if input_sen == 'end':
		end_time = time.time()
		delta_time = round(end_time - start_time,0)
		delta_hour = int(delta_time // 60 // 60)
		delta_min = int((delta_time // 60 )% 60)
		delta_sec = int(delta_time % 60)
		print("Running time ",str(delta_hour)+":"+str(delta_min)+":"+str(delta_sec))
		print("The score is",sum_list)
		break
	print("plus the score ")