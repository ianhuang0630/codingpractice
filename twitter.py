import sys

start_time = 0
end_time = 0

line_num = 1
	
timepoints = set()
time_to_data = {}
time_rounded_to_data = {}

def concat_time(date):
	"""
	Inputs:
		date (string): date in YYYY-MM-DD
	"""
	if len(date) == 7:
		return int(date[:4] + date[5:7])*100
	elif len(date) == 10:
		return int(date[:4] + date[5:7] + date[8:])

def format_output(time, value):
	orig = str(time)[:4]+"-"+str(time)[4:6]
	
	for element in value:
		orig += ", " + element[0] + ", "+ element[1][:-1]

	assert "\n" not in orig, "Screwup"

	return orig

for line in sys.stdin:
	if line_num == 1:
		times = line.split(", ")
		times[1] = times[1][:-1]
		start_time = concat_time(times[0])
		end_time = concat_time(times[1])

	elif line_num == 2:
		pass
	
	else:
		variables = line.split(", ")

		# first in variables is times
		time_marker = concat_time(variables[0])
		# # ceil to hundreds
		# time_marker = time_marker//100 * 100
		timepoints.add(time_marker)

		# saving category and count in the dictionary
		if time_marker in time_to_data:
			time_to_data[time_marker].append([variables[1], variables[2]])
		else:
			time_to_data[time_marker] = [[variables[1], variables[2]]]

	line_num += 1

# now we find the relevant times
output = ""

# dropping valid times into 2nd dictionary, combining categories
for i in sorted(timepoints):
	if i<end_time and i>start_time:
		time_rounded = i//100*100
		if time_rounded in time_rounded_to_data:
			time_rounded_to_data[time_rounded].extend(time_to_data[i])
		else:
			time_rounded_to_data[time_rounded] = time_to_data[i]

		# time_to_data[i] holds the activities and counts

for i in sorted(time_rounded_to_data.keys()):
	output = format_output(i, time_rounded_to_data[i]) + "\n" + output

output = output[:-1] # take off \n
print(output)
