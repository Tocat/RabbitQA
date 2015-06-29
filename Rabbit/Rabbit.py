# coding: utf-8

# Copyright (c) 2015, Tocat.
# This file is part of RabbitQA and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Tocat <tocat@outlook.com>

#run: ask

import sys
from answersys import Answersys

if __name__ == "__main__":
	if sys.argv[1]=="A":
		print "A"
		question = []
		length = len(sys.argv)
		for i in range(3,length):
			question.append(sys.argv[i])
		question = " ".join(question)
		ans = Answersys(sys.argv[2], question)
		ans.buildBase()
	elif sys.argv[1]=="Q":
		print "Q"
	else:
		print "error"
		exit()
