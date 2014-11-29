total = 0

lessThan = 1000-1

multiple = 3
curr = 0
for ii in xrange(lessThan/multiple):
    curr += (ii + 1) * multiple

multiple = 5
for ii in xrange(lessThan/multiple):
    candidate = multiple * (ii + 1)
    if candidate % 3 > 0:
        curr += candidate

print curr

