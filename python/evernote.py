#!/usr/bin/env python

import re
import collections

"""List the words appearing in a document, ordered by highest frequency.

:param doc: str, a text document
:param num: int, number of items to return

:returns: list of strings, highest frequency first
"""
def parse_freq(doc, num):
	return [word for (word, count) in collections.Counter(parse_doc(doc)).most_common(num)]

"""Split string into lowercase words and strip non-alphanumeric characters.
"""
def parse_doc(doc):
	return re.findall(r'[0-9a-zA-Z\'\-]+', doc.lower())

"""Do what parse_freq does, but faster. This function runs in O(n) time
versus using Counter's most_common method which does binary heap searching
and runs at fastest, O(n + nlogk).
"""
def parse_freq_better(doc, num):
	# stuff I'll need later
	f_dict = {}
	f_max = 0
	top_f = []
	i = 0
	j = 0
	# map words to frequencies	
	for word in parse_doc(doc): 
		f_dict[word] = 1 if not (word in f_dict) else (f_dict[word]+1)
	# initialize array using highest frequency 
	for word in f_dict:
		f_max = max(f_dict[word], f_max)
	f_array = [None]*(f_max + 1)
	# order words by frequency
	for word in f_dict:
		if f_array[f_dict[word]] == None:
			f_array[f_dict[word]] = [word]
		else:
			f_array[f_dict[word]].append(word)
	# extract the num words
	f_array = f_array[::-1]
	while num > 0:
		try:
			top_f.append(f_array[i][j])
			num -= 1
			j += 1
		except (IndexError, TypeError):
			j = 0
			i += 1
	return top_f

test_string = """Albert is my best friend. Albert loves me so much. Albert
			   will always have my back because I love him like a brother.
			   Brothers do everything with each other, including eat,
			   sleep and shower."""
