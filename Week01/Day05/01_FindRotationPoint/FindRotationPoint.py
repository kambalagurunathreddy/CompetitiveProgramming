import unittest


def find_rotation_point(array):
	l=len(array)
	if(l==0):
		return
	elif(l==1):
		return 0
	return rp(array,0,l-1)
def rp(array,low,high):
	while(low<high):
		mid=(low+high)//2
		if (array[mid]<array[mid-1] and array[mid]<array[mid+1]):
			return mid
		low=mid+1
	if (mid+1==high):
	    if(array[low-1]<array[high]):
	        return 0
	    else:
	        return high
	return -1










# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'zebra'])
        expected = 0
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)