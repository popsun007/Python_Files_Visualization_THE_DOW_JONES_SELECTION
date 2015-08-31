import os
import os.path
import matplotlib.pyplot as plt
path = './dow_input.txt'
if os.path.isfile(path):
	handle = open(path, 'r')
	text = handle.read()   # answer 1
	word = text.split()
	output_list = []
	days_greater_5_billion = []
	days_greater_5_billion_ADJ = []
	ADJ_list = []
	for i in range(len(word)):
		row = word[i].split(',')  # answer 3
		if int(row[4]) > 5.5e9:   # answer 4
			output_list.append(i)
			days_greater_5_billion.append(i + 1)
			days_greater_5_billion_ADJ.append(row[5])
		ADJ_CLOSE = row[5]
		ADJ_list.append(ADJ_CLOSE)
	how_many_days = str(len(output_list))  # answer 5
	output_list_string = ','.join(str(e) for e in output_list)
	output_file = open('dow_output.txt', 'w')
	output_file.write("The dow volume has been above 5.5 billion on " + how_many_days + " days this year. The high_vol_index: [" + output_list_string + "].")
	output_file.close()   # answer 6

	days = range (1, len(word) + 1)
	plt.plot(days,ADJ_list, label = 'ADJ Line') # answer 7
												# answer 8 below
	plt.scatter(days_greater_5_billion, days_greater_5_billion_ADJ, label = 'VOLUME Greater than 5.5 billion', color = 'red', s = 25, marker = 'o')
	plt.xlabel('Day to day')
	plt.ylabel('ADJ_CLOSE')
	plt.title('Everyday ADJ CLOSE in 2008')
	plt.legend()
	plt.show()

else:
	print ("File does not exist!") # answer 2

