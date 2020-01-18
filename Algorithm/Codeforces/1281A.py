for _ in range(int(input())):
	string=input()
	if string[len(string)-1]=='o':
		print("FILIPINO")
	elif string[len(string)-1]=='a':
		print("KOREAN")
	else:
		print("JAPANESE")