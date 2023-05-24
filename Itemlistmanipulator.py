import pickle

#add new items

f=open("Itemlist.dat","rb+")

while True:
        '''name=input('Enter name of new item')
        price =int(input('Enter price'))
        desc=input('Enter description(brief)')'''
        temp=pickle.load(f)
        print(temp['newitem'])
        '''temp[name]=[price,'',desc]
        pickle.dump(temp,f)
        chk=input('would you like to continue')'''
        if chk!='y':
            break

