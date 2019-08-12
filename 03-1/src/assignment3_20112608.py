import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        
        if parse[0] == 'add':
            try:
                record = {'Name':str(parse[1]), 'Age':int(parse[2]), 'Score':int(parse[3])} # 수정
            except ValueError:
                print("wrong value")
            if parse[4] is not None: #수정, 의도된것보다 더 많은 인자를 넣는 경우 에러 메세지를 리턴
                print("too many agrs")
            else:
                scdb += [record]
        
        elif parse[0] == 'del':    
            for p in scdb[:]: # 수정
                if p['Name'] == parse[1]:
                    scdb.remove(p)    
        #break - (3) 브레이크를 하면 루프를 나가게 한걸 그냥 지움
        
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        #(1) find 명령 추가
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    for attr in p:
                        print(attr + "=" + str(p[attr]), end=' ') #수정
                    print()

        #(2) inc 명령 추가
        elif parse[0] == 'inc':
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        p['Score'] = p['Score'] + parse[2] # 수정, Score를 int로 받음
                    except:
                        print("NaN")

        # 개인적 추가 부분 decrease 명령어
        #elif parse[0] == 'dec':
        #   for p in scdb:
        #       if p['Name'] == parse[1]:
        #           try:
        #                p['Score'] = str(int(p['Score']) - int(parse[2]))
        #           except:
        #               print("NAN")

        
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ') # 수정 int를 str로 캐스팅
        print()






scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
