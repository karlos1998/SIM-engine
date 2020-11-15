import serial

import time

SERIAL_PORT = "/dev/ttyS0"

ser = serial.Serial(SERIAL_PORT, baudrate = 115200, timeout = 0.5)

SendLineInProgress = False

ReadQueue = []

def SendLine(line, wait = True, onlyFirstLine=False, arrBytes=False, arrBytesLength=0, skipChars=[]):
	global SendLineInProgress
	ser.write(str.encode(line + "\r"))
	s = ""
	bts = bytearray()
	bts_l = 0

	skipLinesInBytes = 2
	skippedLinesInBytes = 0
	previousChar = 0
	StopBuffer = False

	if(wait == True):
		SendLineInProgress = True
		if arrBytes:
			time.sleep(3)

		while 1:
			ch = ser.read();
			#print(">" + str(ch) + "<")
			#print(ord(ch))
			#if len(ch) == 0 or ch == "" or ch == "\n" or ord(ch) == 10:
			if len(ch) == 0:
				break
			if arrBytes:

				
				#time.sleep(0.1)

				ch_nr = ord(ch)

				if ch_nr in skipChars: 
					print("Skipping char...")
					continue

				if skippedLinesInBytes >= skipLinesInBytes:

					#if ch_nr == 10 and previousChar == 13:
					if bts_l >= arrBytesLength:
						StopBuffer = True

					if StopBuffer:
						s += ch.decode()
					else:

						#try:
							#print(str(ord(ch)) + " -> " + ch.decode() )
						#except:
							#print(str(ord(ch)) + " -> " + "NULL" )

						bts.append(ch_nr)
						bts_l += 1

					previousChar = ch_nr

				elif ch_nr == 10:
					skippedLinesInBytes += 1

			else:
				s += ch.decode()
		print(s)
		SendLineInProgress = False
	
		if arrBytes:
			ReadQueue.append(s)
			print(s)
			return bts

		s = s.split("\r\r\n")
		s.pop(0)
		s = "\n".join(s)
		s = s.rstrip(chr(10))
		s = s.rstrip(chr(13))
		
		if onlyFirstLine is True:
			return s.split("\n").pop(0)

	return s
		#TODO: Zapisywac to co sie tu wypisze jako listy danych a potem te listy czytac jako piorytet podczas sprwadzania nowych danych w petli
		#CEL ^ zeby podczas zbierania informacji tutuaj typu "OK" nie przyszedl miedzyczasie jakis np SMS, z ktorym nic sie nie zrobi

def Read():
	return ser.read()

def ReadLine():
	return ser.readline()

def Write(s, encode = True):
	if encode == True:
		return ser.write(s.encode())
	else:
		return ser.write(s)