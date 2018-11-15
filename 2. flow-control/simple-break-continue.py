spam = 0
while spam < 5 :
    print('Number is : ' + str(spam))
    if spam == 3 :
        break
    spam += 1

spam = 0
while spam < 5 :
    spam += 1
    if spam == 3 :
        continue
        print('3')
    print('Number is : ' + str(spam))