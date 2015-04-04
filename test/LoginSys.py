# coding = gbk
'''
Created on Mar 9, 2014

@author: Administrator
'''
db = {}

def newuser():
    prompt = 'login desired:/'
    while True:
        name = eval(input(prompt))
        if name in db:
            prompt = 'name taken , try another'
            continue
        else:
            break
    db[name] = eval(input('password:'))
            
def olduser():
    name = eval(input('login: '))
    pwd = eval(input('password: '))
    password = db.get(name)
    if pwd == password:
        print(('welcome back',name))
    else:
        print ('login incorrect!')
        
def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter choice:"""
    
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()#delete spaces&chose first letter
            except(EOFError,KeyboardInterrupt): #!!!
                choice = 'q'
            print(('\nYou picked:[%s]' %choice))
            if choice not in 'neq': #!!!
                print ('invalid option , try again')
                continue
            else:
                chosen = True
                done = True
            newuser()
            olduser()

if __name__ == '__main__':
    showmenu()