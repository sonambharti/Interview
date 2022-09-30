def self_prod_Arr(arr):
	n = len(arr)
	if(n==1):
		print(0)
		return
	Pre = [0]*n
	Suf= [0]*n
	
	Res_prod = [0]*n
	
	Pre[0] = 1
	Suf[n-1] = 1
	
	for i in range(1, n):
		Pre[i] = arr[i-1]*Pre[i-1]
	
	for i in range(n-2, -1, -1):
		Suf[i] = arr[i+1]*Suf[i+1]

	for i in range(n):
		Res_prod[i] = Pre[i] * Suf[i]
		
	return Res_prod


arr = [1,2,3,0,5]
Res = self_prod_Arr(arr)
print(Res)
