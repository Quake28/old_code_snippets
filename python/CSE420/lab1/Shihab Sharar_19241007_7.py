def check_int(x):
	try:
		int(x)
		return True
	except:
		return False
def check_float(x):
	try:
		float(x)
		return True
	except:
		return False

def main():
	file1=open("input1.txt","r")
	x=file1.read().split("\n")
	for a in range(len(x)):
		y=x.pop(0)
		x+=y.split()
	#print(x)
	arr1=[[] for a in range(6)]
	arr2=["Keywords:","Identifiers:","Math Operators:","Logical Operators:","Numerical Values:","Others"]
	list_symbols=[".",",",";","(",")","{","}","[","]"]
	list_logic=["==","!=",">","<",">=","<="]
	list_math=["+","-","*","/","%","="]
	list_keywords=["auto", "double", "int", "struct", "break", "else", "long", "switch", "case", "enum", "register", "typedef", "char", "extern", "return", "union", "continue", "for", "signed", "void", "do", "if", "static", "while", "default", "goto", "sizeof", "volatile", "const", "float", "short", "unsigned"]
	for a in x:
		len_a=len(a)
		if a[-1] in list_symbols:
			if a[-1] not in arr1[5]:
				arr1[5].append(a[-1])
			a=a[:-1]
			len_a-=1
		if len_a==0:
			continue
		elif check_int(a):
			if not a in arr1[4]:
				arr1[4].append(a)
		elif check_float(a):
			if a not in arr1[4]:
				arr1[4].append(a)
		elif a in list_logic:
			if a not in arr1[3]:
				arr1[3].append(a)
		elif a in list_math:
			if a not in arr1[2]:
				arr1[2].append(a)
		elif a in list_keywords:
			if a not in arr1[0]:
				arr1[0].append(a)
		else:
			if a not in arr1[1]:
				arr1[1].append(a)

	for a in range(len(arr1)):
		joiner=", "
		if a==len(arr1)-1:
			joiner=" "
		z=joiner.join(arr1[a])
		print(arr2[a],z)
main()