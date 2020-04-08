import random
r = random.randint(1 , 100)
while True:
	num = input('請輸入數字')
	num = int(num)
	if num == r:
		print('賓果')
		break
	elif num > r:
		print('嘻嘻你猜得太大了')
	elif num < r:
		print('嘻嘻你猜得太小了')
