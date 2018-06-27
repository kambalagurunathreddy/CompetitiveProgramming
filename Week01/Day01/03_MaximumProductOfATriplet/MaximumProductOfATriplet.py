def MaximumProductOfATriplet(i_array):
	try:
		i_length=len(i_array)
		if (i_length<3):
			raise ValueError('Need Atleast Three values for this function')
		i_array.sort()


		result=max(i_array[0] * i_array[1] * i_array[-1], i_array[-3] * i_array[-2] * i_array[-1])
		#result=i_array[i_length-1]*i_array[i_length-2]*i_array[i_length-3]
		return result
	except Exception as e:
		print(str(e))

i_array=[1, 2, 3, 4]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")


i_array=[6, 1, 3, 5, 7, 8, 2]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[-5, 4, 8, 2, 3]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[-10, 1, 3, 2, -10]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[-5, -1, -3, -2]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")

i_array=[]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")


i_array=[1]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")


i_array=[1,1]
print("i_array",i_array)
print(MaximumProductOfATriplet(i_array))
print("#######################")



