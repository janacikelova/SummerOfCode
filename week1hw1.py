#week1hw

import datetime
import math
import sys

# calculate your age in minutes
# born time in my case 13.03.1996 at six in the morning


fmt = '%Y-%m-%d %H:%M:%S'
born_time = datetime.datetime.strptime('1996-03-13 6:00:00', fmt)
current_time = datetime.datetime.now()

difference = current_time - born_time

print("I am ", round(difference.total_seconds()/60), "old.")


# calculate in how many days 32-bit system timeout, if it has a bug with integer overflow and when it will be in case of 32 -bit
start_date = datetime.date(1970,1,1)
def overflow_problem(max_seconds):
	number_of_days = max_seconds/(60*60*24)
	
	#end_date = start_date
	if(max_seconds < sys.maxsize):
		end_date = start_date + datetime.timedelta(seconds = max_seconds)
		print("32 bit system will overflow in ", math.floor(number_of_days), "days, which refers to following date:", end_date)
	else:
		#not possible to calculate the exact date because of deca-millennium bug
		print("63 bit system will overflow in ", math.floor(number_of_days/365), "years.)

# 32-bit case
overflow_problem(2147483647)
# 64-bit case
overflow_problem(sys.maxsize)