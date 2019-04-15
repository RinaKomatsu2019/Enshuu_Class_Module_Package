def transform(a,b):
    output=[]
    div=a
    while(div>b):
        div=int(div/b)
        mod=a%b
        output.append(mod)
    output.append(div%b)
    if int(div/b)!=0:
        output.append(int(div/b))

    print("Result a={} to {} base".format(a,b))
    for i in range(len(output)-1,-1,-1):
        print("{} ".format(output[i]),end="")
