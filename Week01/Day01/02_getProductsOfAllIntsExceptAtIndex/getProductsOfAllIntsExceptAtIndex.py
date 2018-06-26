def getProductsOfAllIntsExceptAtIndex(i_array):
	try:
		i_length=len(i_array)
		if (i_length==1):
			raise ValueError('Need Atleast Two values for this function')
		temp_array=[]
		initialPdt=1
		for i in range(0,i_length):
			temp_array.append(initialPdt)
			initialPdt*=i_array[i]
		initialPdt=1
		for j in range(i_length-1,-1,-1):
			temp_array[j]=temp_array[j]*initialPdt
			initialPdt*=i_array[j]
		return temp_array
	except Exception as e:
		print(str(e))


i_array=[]
print("i_array",i_array)
print(getProductsOfAllIntsExceptAtIndex(i_array))
print("#######################")


i_array=[2]
print("i_array",i_array)
print(getProductsOfAllIntsExceptAtIndex(i_array))
print("#######################")

i_array=[0,0,0,0]
print("i_array",i_array)
print(getProductsOfAllIntsExceptAtIndex(i_array))
print("#######################")

i_array=[1,7,3,4]
print("i_array",i_array)
print(getProductsOfAllIntsExceptAtIndex(i_array))
print("#######################")

i_array=[2,2,2,2]
print("i_array",i_array)
print(getProductsOfAllIntsExceptAtIndex(i_array))
print("#######################")

i_array=[2,0,2,2]
print("i_array",i_array)
print(getProductsOfAllIntsExceptAtIndex(i_array))
print("#######################")

