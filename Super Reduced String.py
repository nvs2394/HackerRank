s = raw_input()
stack = []
i = 0
for i in xrange(len(s)):
    if not stack or s[i] != stack[-1]:
        stack += [s[i]]
    else:
        stack.pop()
if stack:
    print ''.join(stack)
else:
    print 'Empty String'