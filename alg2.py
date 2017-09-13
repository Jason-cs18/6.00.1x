#coding:utf-8
#   一个有意思的猜数题（0到100之间，不包括0和100）
#   使用2分法，算法复杂度为O(logN)
#   每次电脑猜完后，需要告诉他猜的数大了，还是小了
import math
# 设置的数
secret = 36
low = 0
high = 100
# 电脑猜的数字
guess = (low+high)/2
# 电脑猜的次数
guess_num = 0
# 提示用户猜数范围
print('Please think of a number between 0 and 100!')
while True:
    guess_num += 1
    print('Is your secret number %d ?' % guess)
    a = input("Enter 'h' to indicate the guess is too high."
            "Enter 'l' to indicate the guess is too low. "
            "Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was: %d' % guess)
        break
    elif a == 'h':
        high = guess
    elif a == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
        continue
    # 重新猜
    guess = math.floor((low+high)/2)
