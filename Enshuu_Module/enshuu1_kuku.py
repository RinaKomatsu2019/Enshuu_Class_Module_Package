def generate_kuku(a,b):
    print('a={} b={}'.format(a,b))
    print('   ',end="")
    for i in range(1,a+1):
        if i==a:
          print(' {} '.format(i))
        else:
            print(' {} '.format(i),end="")

    for j in range(1,b+1):
        print(j,end="")
        for i in range(1,a+1):
            if i==a:
                print('  {}'.format(i*j))
            else:
                print('  {}'.format(i*j),end="")
