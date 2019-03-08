"using various methods"

txt = 'RrEeDdVvEeLlVvEeTt'
ret= txt[1::2]
print (ret)


msg1="hey reveluv"
msg2=" hwa ee ting!"
display_msg= msg1+ ',' +msg2*3+ '~!'
print(display_msg)


msg3= input('please enter msg: ')
if 'red' in msg3:
    print ('you have a red flavor')
else:
    print("you are not luvy")


txt= "A lot of things occur each day. every day blackpink in your area. redvelvet"
offset1= txt.find('e')
offset2= txt.find('blackpink')
offset3= txt.find('redvelvet',30)
print(offset1)
print(offset2)
print(offset3)

txt1= "My Password is Blackpink1234"
ret1= txt.replace('1','26')
ret2= txt.replace('blackpink', 'redvelvet')
print(ret1)
print(ret2)

range1= range(10)
range2= range(10,20)
print(list(range1))
print(list(range2))


listdata=[1,2,'a','b','c',[4,5,6,7]]
val1= listdata[1]
val2= listdata[3]
val3= listdata[5][1]


Redvelvet= ['Irene','Seulgi','Wendy','Joy','Yeri','Seulgi']
Bias='Seulgi'
pos= Redvelvet.index(Bias)
print('%s is the main dancer of the member, standing %d th place' %(Bias,pos))
pos= Redvelvet.index(Bias, 2)
print('%s is the main dancer of the member, standing %d th place' %(Bias,pos))

listdata =list(range(1,21))
evenlist= listdata[1::2]
print(evenlist)
oddlist = listdata[0::2]
print(oddlist)


listdata = ['irene','seulgi','wendy','joy','yeri']


ret4= listdata[::-1]
print(listdata)
"print(ret3)"
print(ret4)

listdataRed = ['irene','seulgi','wendy','joy','yeri']
listdataBlack= ['lisa','jenny','rose','jiso']

listdatablackvelvet= listdataRed+listdataBlack
print(listdatablackvelvet)


listdataRedvelvet =[]
for i in range(5):
    redvelvetmembers = input ('please add each member of red velvet[%d/5]: '%(i+1))
    listdataRedvelvet.append(redvelvetmembers)
    print(listdataRedvelvet)


jisoo = listdataBlack.index('jiso')
listdataBlack.insert(jisoo, 'jisoo')
print(listdataBlack)

del listdataBlack[-1]
print(listdataBlack)
