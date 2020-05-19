from random import randint

def gen_lucky_number():
    return randint(0,99)>50



my_money=1000
unitmoney=1
list_money=[]

# INITAL VALUE
isTai=gen_lucky_number()
isPlayTai=False

for i_phien in range(1,100):
    if isTai:
        #play up
        isPlayTai=True
    else:
        #play down
        isPlayTai=False
    my_money=my_money-1
    isTai=gen_lucky_number()
    
    if isTai:
        if isPlayTai:
            my_money = my_money + 2
    if not isTai:
        if not isPlayTai:
            my_money = my_money + 2
    list_money.append(my_money)
    print('isPlayTai',isPlayTai)
    print('isTai',isTai)
    print('my_money',my_money)
    print('-----------------------------')

print('min_money:',min(list_money))
print('max_money:',max(list_money))
print('list_money',list_money)

'''
Chien luoc choi nhu sau:
    quan sat 10 phien dau:
    tien lon hon 1000 chiem 8 phien: choi tiep cat lo va lai 5% => chi thoa man dki nay moi choi
    tien nho hon 1000 chien 7-8 phien: stop => nhieu cau sole
'''
