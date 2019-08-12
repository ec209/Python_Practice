import cv2
import numpy as np
import random
import threading
import time

l=[]
def generate():
    D={0:"stone",1:"paper",2:"scissors"}
    x=random.randint(0,2)
    threading.Timer(2, generate).start()
    l.append((D[x]))
    
generate()


stone_cascade = cv2.CascadeClassifier('rock.xml')
paper_cascade = cv2.CascadeClassifier('paper.xml')
sci_cascade = cv2.CascadeClassifier('scissor.xml')
none_cascade = cv2.CascadeClassifier('none.xml')

cap = cv2.VideoCapture(0)
countS=0
countP=0
countSC=0
countNumber=0
countWin=0
countLose=0
countTie=0
while True:
    
    ret, img = cap.read()
    img=img[100:346,100:346]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stone = stone_cascade.detectMultiScale(gray, 1.1, 5)
    paper = paper_cascade.detectMultiScale(gray, 1.2, 5)
    scissors = sci_cascade.detectMultiScale(gray, 1.1, 150)
    none = none_cascade.detectMultiScale(gray, 1.1, 1)
    
    for(x,y,w,h) in stone:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
        _gray = gray[y:y+h,x:x+w]
        _color = img[y:y+h,x:x+w]
        countS+=1
        if(countS==1):
            countP=0
            countNumber=0
            countSC=0
            cv2.destroyWindow('none')
            if(l[len(l)-1]=="scissors"):
                img1=cv2.imread("scissors.png")
                cv2.imshow('OUT',img1)
                print("플레이어 승!")
                time.sleep(2)
                countWin+=1
            elif(l[len(l)-1]=="paper"):
                img1=cv2.imread("paper.png")
                cv2.imshow('OUT',img1)
                print("플레이어 패!")
                time.sleep(2)
                countLose+=1
            else:
                img1=cv2.imread("stone.png")
                cv2.imshow('OUT',img1)
                print("무승부")
                time.sleep(2)
                countTie+=1

    for(x,y,w,h) in paper:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
        _gray = gray[y:y+h,x:x+w]
        _color = img[y:y+h,x:x+w]
        countP+=1
        if(countP==1):
            countS=0
            countNumber=0
            countSC=0
            cv2.destroyWindow('none')
            if(l[len(l)-1]=="stone"):
                img1=cv2.imread("stone.png")
                cv2.imshow('OUT',img1)
                print("플레이어 승!")
                time.sleep(2)
                countWin+=1
            elif(l[len(l)-1]=="scissors"):
                img1=cv2.imread("scissors.png")
                cv2.imshow('OUT',img1)
                print("플레이어 패!")
                time.sleep(2)
                countLose+=1
            else:
                img1=cv2.imread("paper.png")
                cv2.imshow('OUT',img1)
                print("무승부")
                time.sleep(2)
                countTie+=1
    if len(stone)==0 and len(paper)==0:
        for(x,y,w,h) in scissors:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
            _gray = gray[y:y+h,x:x+w]
            _color = img[y:y+h,x:x+w]
            countSC+=1
            if(countSC==1):
                cv2.destroyWindow('none')
                countS=0
                countNumber=0
                countP=0
                if(l[len(l)-1]=="paper"):
                    img1=cv2.imread("paper.png")
                    cv2.imshow('OUT',img1)
                    print("플레이어 승!")
                    time.sleep(2)
                    countWin+=1
                elif(l[len(l)-1]=="stone"):
                    img1=cv2.imread("stone.png")
                    cv2.imshow('OUT',img1)
                    print("플레이어 패!")
                    time.sleep(2)
                    countLose+=1
                else:
                    img1=cv2.imread("scissors.png")
                    cv2.imshow('OUT',img1)
                    print("무승부")
                    time.sleep(2)
                    countTie+=1
            
                
    if len(stone)==0 and len(paper)==0 and len(scissors)==0:
        for(x,y,w,h) in none:
            img1=cv2.imread("none.jpg")
            cv2.imshow('none',img1)
            countNumber+=1
            if(countNumber==1):
                countP=0
                countS=0
                countSC=0
                cv2.destroyWindow('OUT')
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break


print("최종 점수 발표")
print("승:",countWin,"패:",countLose,"무:",countTie)
cap.release()
cv2.destroyAllWindows()
