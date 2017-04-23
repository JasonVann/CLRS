def test1_3():
    n = 1
    while True:
        time1 = 100*n**2
        time2 = 2**n
        if time1 >= time2:
            n += 1
        else:
            break
    print(n, time1, time2)

test1_3()
