def midpoint(imin, imax):
	return (imax + imin) >> 1


def binary_search(arrlist, item, left, right):
	if right < left:
		return -1
	
	imid = int(midpoint(left, right))

	if imid >= len(arrlist):
		return -1
	
	if arrlist[imid] > item:
		return binary_search(arrlist, item, left, imid - 1)
	else:
		if arrlist[imid] < item:
			return binary_search(arrlist, item, imid + 1, right )
	return imid

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(arr, 6, 0, len(arr)))