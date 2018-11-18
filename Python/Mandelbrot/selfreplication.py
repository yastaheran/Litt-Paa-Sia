"""
Make a short (but non-empty!) python script which prints its own source code.
Your script should not accomplish this task by accessing the file containing
its own source code, so it should not open any files for reading or call system
utilities which do.
"""
#!/usr/bin/env python
s = 's = %r\nprint(s%%s)'
print(s%s)