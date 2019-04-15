from myCalc.calc_class import Calculate

a=4
b=2
c1=Calculate(a,b)
sum=c1.sum()
dif=c1.dif()
mul=c1.multi()
div=c1.div()

print("{}+{}={}".format(a,b,sum))
print("{}-{}={}".format(a,b,dif))
print("{}*{}={}".format(a,b,mul))
print("{}/{}={}".format(a,b,div))

