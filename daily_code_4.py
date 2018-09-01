'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

list_nums1 = [3, 4, -1, 1]
list_nums2 = [1, 2, 0]
list_nums3 = [0, 100, 101, 10]

def missing_positive_integers(list_nums):
	for i in range(1, max(list_nums)):
		if i not in list_nums:
			return i

	return max(list_nums) + 1


print(missing_positive_integers(list_nums1))
print(missing_positive_integers(list_nums2))
print(missing_positive_integers(list_nums3))