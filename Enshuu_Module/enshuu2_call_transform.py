import enshuu2_transform

print('input a=?')
a=input()
print('input b=?')
b=input()

if (a.isdecimal())  and (b.isdecimal()):
    enshuu2_transform.transform(int(a),int(b))
else:
    print("Invalid input !")