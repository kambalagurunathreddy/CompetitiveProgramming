def MaximumProductOfATriplet(i_array):
	try:
		i_length=len(i_array)
		if (i_length<3):
			raise ValueError('Need Atleast Three values for this function')
		i_array.sort()
		result=i_array[i_length-1]*i_array[i_length-2]*i_array[i_length-3]
		return result
	except Exception as e:
		print(str(e))

i_array=[]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")


i_array=[1]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[1,8]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[1,8,2]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[1,8,2,6,5]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[1,8,2,-6,5]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")


i_array=[2,2,2,2]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

