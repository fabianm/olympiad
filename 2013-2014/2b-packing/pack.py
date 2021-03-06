#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# Copyright 2014 Fabian M.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def calc_max(length, width):
	"""
	Calculates the maximum amount of T-shaped objects in a rectangle of the
	  given size.

	Keyword arguments:
	length -- the length of the rectangle.
	width -- the width of the rectangle.
	
	Returns the maximum amount of T-shaped objects in a rectangle of the given
	  size.
	"""
	surface = length * width
	if length < 2 or width < 2 or surface < 6:
		return 0
	elif surface < 10:
		return 1
	elif length == 2 or width == 2:
		return length == 2 and calc_max_two(width) or calc_max_two(length)
	elif length == 3 or width == 3:
		return length == 3 and calc_max_three(width) or calc_max_three(length)
	elif length == 5 or width == 5:
		return length == 5 and calc_max_five(width) or calc_max_five(length)
	elif length == 6 or width == 6:
		return length == 6 and calc_max_six(width) or calc_max_six(length)
	elif length == 7 or width == 7:
		return length == 7 and calc_max_seven(width) or calc_max_seven(length)
	elif length  % 4 == width % 4 == 0:
		return int(surface / 4)
	elif length  % 4 == width % 4 == 2 or length % 4 == 0 or width % 4 == 0:
		return int((surface - 4) / 4)
	elif length % 4 == 0 and width % 4 == 2:
		return int((surface - (length % 4 + 2)) / 4)
	elif length % 4 == 2 and width % 4 == 0:
		return int((surface - (width % 4 + 2)) / 4)

def calc_max_two(length):
	"""
	Assumes that the width equals two and calculates the maximum amount of 
	  T-shaped objects in a rectangle with size __2x__.

	Keyword arguments:
	length -- the length of the rectangle.

	Returns the maximum amount of T-shaped objects in a rectangle with the
	  size __2x__
	"""
	surface = 2 * length
	if length <= 2 or surface < 6:
		return 0
	return int((surface - (2 + (2 * length % 2))) / 4)
	
		
def calc_max_three(length):
	"""
	Assumes that the width equals three and calculates the maximum amount of 
	  T-shaped objects in a rectangle with size __3x__.

	Keyword arguments:
	length -- the length of the rectangle.

	Returns the maximum amount of T-shaped objects in a rectangle with the
	  size __3x__
	"""
	surface = 3 * length
	if length == 3:
		return 1
	elif length % 3 == 0:
		return int((surface - (length / 3)) / 4)
	elif length % 3 == 1:
		return int((surface - (((length + 2) / 3) + 1)) / 4)
	elif length % 3 == 2:
		return int((surface - (((length + 1) / 3) + 1)) / 4)

def calc_max_five(length):
	"""
	Assumes that the width equals five and calculates the maximum amount of
	  T-shaped objects in a rectangle with size __5x__.

	Keyword arguments:
	length -- the length of the rectangle

	Returns the maximum amount of T-shaped objects in a rectangle with the 
	  size __5x__
	"""
	return int((5 * length - ([5, 2, 3, 4][(length - 1) % 4])) / 4)

def calc_max_six(length):
	"""
	Assumes that the width equals six and calculates the maximum amount of
	  T-shaped objects in a rectangle with size __6x__.

	Keyword arguments:
	l -- the length of the rectangle

	Returns the maximum amount of T-shaped objects in a rectangle with the 
	  size __6x__
	"""
	return int((6 * length - (2 + (2 * length % 2))) / 4)

def calc_max_seven(length):
	"""
	Assumes that the width equals seven and calculates the maximum amount of
	  T-shaped objects in a rectangle with size __7x__.

	Keyword arguments:
	length -- the length of the rectangle

	Returns the maximum amount of T-shaped objects in a rectangle with the 
	  size __7x__
	"""
	surface = 7 * length
	if length % 4 == 0:
		return int((surface - 4) / 4)
	elif length % 4 == 1:
		return int((surface - 3) / 4)
	elif length % 4 == 2:
		return int((surface - 2) / 4)
	elif length % 4 == 3:
		return int((surface - 5) / 4)
		
if __name__ == "__main__":
	"""
	Main entry point for this program.
	"""
	width = int(input())
	length = int(input())
	print(calc_max(length, width))