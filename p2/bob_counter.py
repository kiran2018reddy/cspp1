'''Assume s is a string of lower case chara
Number of times bob occurs is: 2'''
def main():
	"""string"""
	s_= input()
	# the input string is in s
	# remove pass and start your code here
	st_ ='bob'
	c_ = 0
	for i in range(len(s_)-2):
		if st_ == s_[i]+s_[i+1]+s_[i+2]:
			c_ = c_ + 1
	print(c_)
if __name__== "__main__":
	main()
