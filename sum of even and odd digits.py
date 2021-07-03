n=int(input())
e_sum=0
o_sum=0
while(n):
	r=n%10
	if(r%2==0):
		e_sum+=r
	else:
		 o_sum+=r
	n=n//10
print("sum of even number",e_sum)
print("sum of odd number",o_sum)


	
	

	