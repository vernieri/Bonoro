#!/usr/bin/python3
import time
import hashlib
import linecache

bonoro = 'bonoro'
name1 = 'i'



def procedure():
   time.sleep(2.5)


def random_bonoro(str):

	stringList = []

	t0 = time.process_time()
	procedure()
	string1 = str(time.process_time() - t0)

	t0 = time.time()
	procedure()
	string2 = str(time.time() - t0)

	stringList.append(string1)
	stringList.append(string2)

	return stringList	

def get_bonoro():
	random_bonoro('bolsonaro')
	return bonoro

print(get_bonoro())
