#!/usr/bin/env python3

'''
A quick'n'dirty wrapper around pyflakes that suppresses warnings for lines that contain '# noqa' or '# NOQA'.
Some spurious warnings are also ignored.

Any command-line arguments and options are passed to pyflakes.
'''

import functools, subprocess, sys, re


IGNORE_COMMENT = '# noqa'

AUTOIGNORE = (
	re.compile(": local variable '_' is assigned to but never used$"),
)



@functools.lru_cache()
def getFileLines(file: str) -> 'List[str]':
	with open(file) as f:
		return f.readlines()


def main() -> int:
	p = subprocess.Popen(['pyflakes'] + sys.argv[1:], stdout = subprocess.PIPE)
	stdout, _ = p.communicate() # type: Tuple[bytes, bytes]

	failed = False
	for warning in stdout.decode('utf-8').strip().split('\n'):
		if warning:
			file, line, _ = warning.split(':', 3) # dir/file.py:5: 'sys' imported but unused
			line = getFileLines(file)[int(line) - 1].strip()
			if IGNORE_COMMENT not in line.lower() and not any(pat.search(warning) for pat in AUTOIGNORE):
				failed = True
				print(warning)

	return int(failed)


if __name__ == '__main__':
	sys.exit(main())
