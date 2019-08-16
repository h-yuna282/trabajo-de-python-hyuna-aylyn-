x=int(input("Introdusca  el numero al que se desea llegar "))

for y in range(x):
    if y%3==0 and y%5==0:
        print(y,"FIZZ BUZZ")
    else:
        if y%3==0:
            print(y,"FIZZ")
        if y%5==0:
            print(y,"BUZZ")
