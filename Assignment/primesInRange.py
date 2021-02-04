import math


## @param low the lower bound
## @param high the upper bound 
def primesInRange(low = 0, high = 0)->list:
	if not (isinstance(low, int) and isinstance(high, int)):
		return None
	if low < 1 or high > 1000:
		return None
	if low > high:
		return None
	result = list(range(low, high+1));
	stop = int(math.sqrt(high))
	time = 0;
	for divisor in range(2, stop + 1):
		if result == []:
			break
		time = int(low / divisor)
		num = time * divisor;
		while num <= high:
			if time == 1:
				time += 1
				num = time * divisor
				continue
			if num in result:
				result.remove(num)
			time += 1
			num = time * divisor
	
	return result;
	
