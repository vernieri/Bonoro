#!/usr/bin/python3
import time
import hashlib
import linecache

def procedure():
   time.sleep(2.5)


def process(code):

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

def principales():
  process()

anagrama(principales())
