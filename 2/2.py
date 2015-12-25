result_sum = 0
# used to store the current fibonacci numbers
fib_num1 = 1
fib_num2 = 2

while fib_num1 < 4000000:
	if fib_num1 % 2 == 0:
		print fib_num1
		result_sum += fib_num1
		
	tmp = fib_num2
	fib_num2 += fib_num1
	fib_num1 = tmp

print "Result is: %s" % result_sum

	


