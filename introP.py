
#!/usr/bin/python

str = raw_input('enter string ')
print(str)
num = len(str)
chars = [" "]
while num >= 0:
	chars.append(str[num:num+1])
	num -= 1
for element in chars:
	print element
