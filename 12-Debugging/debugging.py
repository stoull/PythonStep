# debuging


# 1. linting

# 2. ide / editor

# 3. read errors

# 4. pdb

import pdb 		# like The LLDB Debugger on XCode
# more detail https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/gdb_to_lldb_transition_guide/document/Introduction.html


def add(num1, num2):
	pdb.set_trace()
	t = num1 * num2
	return num1 + num2

add(2, "s")
