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


"""
Notes on run-time:

It is impossible to write a solution that runs in O(n), where n is the 
number of characters in the string. The fastest that a solution can be
is O(nlog(k)) where n is the number of characters and k is the number
of words to return in the final list.

The python collections.Counter class creates and maintains an ordered
dictionary in O(nlog(k)) time. Calling that class's most_common function
actually runs python's heapq.nlargest(k) which runs in O(nlog(k)) time.
The regex parsing runs in linear time. Altogether, parse_freq(doc, num)
would run in O(nlog(k)) time.
"""