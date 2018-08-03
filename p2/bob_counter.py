'''Assume s is a string of lower case chara
Number of times bob occurs is: 2'''
def main():
	"""string"""
	str1_= input()
	# the input string is in s
	# remove pass and start your code here
	st_ ='bob'
	cou_ = 0
	for i in range(len(str1_)-2):
		if st_ == str1_[i]+str1_[i+1]+str1_[i+2]:
			cou_ = cou_ + 1
	print(cou_)
if __name__== "__main__":
	main()
