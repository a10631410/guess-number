import random
start = input('請輸入你要開始的數字')
end = input('請輸入你要結束的數字')
start = int(start)
end = int(end)
r = random.randint(start , end)
count = 0
while True:
	count += 1
	num = input('請輸入數字')
	num = int(num)
	if num == r:
		print('賓果')
		break
	elif num > r:
		print('嘻嘻你猜得太大了')
	elif num < r:
		print('嘻嘻你猜得太小了')
	print('這是你猜的第' , count, '次')