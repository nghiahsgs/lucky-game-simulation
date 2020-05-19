from random import randint

def gen_lucky_number():
    return randint(0,99)>50

def analysis_10_first_round(L):
    dem=0
    for l in L:
        if l>1000:
            dem+=1
    if dem>7:
        return True # continue play
    else:
        return False



def play_each_day():
    my_money=1000
    unitmoney=1
    list_money=[]

    # INITAL VALUE
    isTai=gen_lucky_number()
    isPlayTai=False

    for i_phien in range(10):
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

    isContinue=analysis_10_first_round(list_money)
    if not isContinue:
        profit=my_money-1000
        #print(list_money)
        #print('fail')
        #input(profit)
        return profit


    for i_phien in range(90):
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
        if my_money> 1005:
            #print(list_money)
            #input('win and stop')
            profit=my_money-1000
            return profit
        
        if my_money< 990:
            #print(list_money)
            #input('fail and stop')
            profit=my_money-1000
            return profit

    profit=my_money-1000
    return profit

list_profit=[]
for iday in range(1000):
    profit=play_each_day()
    list_profit.append(profit)
print('sum list profit',sum(list_profit))
'''
Chien luoc choi nhu sau:
    quan sat 10 phien dau:
    tien lon hon 1000 chiem 8 phien: choi tiep cat lo va lai 5% => chi thoa man dki nay moi choi
    tien nho hon 1000 chien 7-8 phien: stop => nhieu cau sole
'''
