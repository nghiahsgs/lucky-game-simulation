from random import randint

def gen_lucky_number():
    return randint(0,99)

list_result=[]
# 100 phien dau tien ko lam j de lay du lieu
for i in range(100):
    list_result.append(gen_lucky_number())


#print(list_result)

my_money=1000
unitmoney=1
list_money=[]

for i_phien in range(100,1000):
    arg=sum(list_result[(i_phien-100):i_phien])/100
    print('arg',arg)
    if arg <50:
        #play up arg
        ratio=1+arg/(100-arg)
    else:
        #play down arg
        ratio=1+ (100-arg)/arg
    my_money=my_money-1
    kq=gen_lucky_number()
    print('kq',kq)

    if arg <50:
        #play up arg
        if kq>arg:
            my_money+=1*ratio
    else:
        #play down arg
        if kq<arg:
            my_money+=1*ratio

    list_money.append(my_money)
    print('my_money',my_money)
    print('-----------------------------')

print('min_money:',min(list_money))
print('max_money:',max(list_money))



