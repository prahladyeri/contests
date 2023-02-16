def is_number(s):
    try:
        t = float(s)
        return t
    except ValueError:
        return False
        
def main():
	i = input()
	if i.startswith('-'): i = i[1:] #strip minus sign
	
	if i.isdigit():
		print('This input is of type Integer.')
	elif is_number(i):
		print('This input is of type Float.')
	elif type(i) == str:
		print('This input is of type string.')
	else:
		print('This is something else.')

main()
