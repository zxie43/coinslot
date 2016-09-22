import socket
import re
import math
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('misc.chal.csaw.io',8000))


recvnumber = 50

for x in range(0, 700):
	data = s.recv(100)
	print data
	list1 = list(data)
	numbers = re.findall(r"[-+]?\d*\.\d+|\d+", data)
	fl1 = numbers[0]
	print fl1
	fl1 = float(fl1)
	fl1 = fl1*100.00
	int1 = int(round(fl1))
	print int1
	if int1 >= 1000000:
		value = int1 - 1000000
		s.send(str(int1/1000000) + "\n")
		int1 = int1 % 1000000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
	#print data
	if int1 >= 500000:
		value = int1 - 500000
		s.send(str(int1/500000) + "\n")
		int1 = int1 % 500000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-1)
	#print data
	if int1 >= 100000:
		value = int1 - 100000
		s.send(str(int1/100000) + "\n")
		int1 = int1 % 100000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-1)
	#print data
	if int1 >= 50000:
		value = int1 - 50000
		s.send(str(int1/50000) + "\n")
		int1 = int1 % 50000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-2)
	#print data

	if int1 >= 10000:
		value = int1 - 10000
		s.send(str(int1/10000) + "\n")
		int1 = int1 % 10000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-2)
	#print data

	if int1 >= 5000:
		value = int1 - 5000
		s.send(str(int1/5000) + "\n")
		int1 = int1 % 5000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-3)
	#print data

	if int1 >= 2000:
		value = int1 - 2000
		s.send(str(int1/2000) + "\n")
		int1 = int1 % 2000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-3)
	#print data

	if int1 >= 1000:
		value = int1 - 1000
		s.send(str(int1/1000) + "\n")
		int1 = int1 % 1000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-4)
	#print data

	if int1 >= 500:
		value = int1 - 500
		s.send(str(int1/500) + "\n")
		int1 = int1 % 500
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber-4)
	#print data

	if int1 >= 100:
		value = int1 - 100
		s.send(str(int1/100) + "\n")
		int1 = int1 % 100
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
	#print data

	if int1 >= 50:
		value = int1 - 50
		s.send(str(int1/50) + "\n")
		int1 = int1 % 50
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
	#print data

	if int1 >= 25:
		value = int1 - 25
		s.send(str(int1/25) + "\n")
		int1 = int1 % 25
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
	#print data

	if int1 >= 10:
		value = int1 - 10
		s.send(str(int1/10) + "\n")
		int1 = int1 % 10
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
	#print data

	if int1 >= 5:
		value = int1 - 5
		s.send(str(int1/5) + "\n")
		int1 = int1 % 5
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
	#print data


	if int1 >= 1:
		value = int1 - 1
		s.send(str(int1/1) + "\n")
		int1 = int1 % 1
	else:
		s.send(str(0) + "\n")

