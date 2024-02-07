from tkinter import*


bomb=100
score=0
pressReturn=True
labelBestScore=0
bestScore=0

def saveBestScore(score):    
     try:
        with open("best_score.txt", "r") as file: bestScore = int(file.read())
        if score > bestScore:               
          with open("best_score.txt", "w") as file:
            file.write(str(score))    
     except FileNotFoundError:
         with open("best_score.txt", "w") as file:   file.write(str(score))
     
def loadBestScore():
    global bestScore    
    try:
     with open("best_score.txt", "r") as file:   bestScore = int(file.read())
     labelBestScore.config(text="Best Score: " + str(bestScore), font=("Comic Sans MS", 16))    
    except FileNotFoundError:
        labelBestScore.config(text="Best Score: 0", font=("Comic Sans MS", 15))

def start(event):
     global pressReturn
     global bomb
     global score
     if not pressReturn:
       pass
     else:
        bomb=100
        score=0
        label.config(text=" ")
        updateDisplay()
        updatePoint()
        updateBomb()
        pressReturn=False

def updateDisplay():
    global score
    global bomb
    if bomb >50:
        bombLable.config(image=noPhoto)
    elif 0< bomb <50:
        bombLable.config(image=normalPhoto)
    else:
        bombLable.config(image=bangPhoto)
    fuseLabke.config(text="Fuse=" +str(bomb))
    scoreLable.config(text="Score=" +str(score))
    fuseLabke.after(100,updateDisplay)

def updateBomb():
    global bomb
    bomb-=5
    if isAlive():
       fuseLabke.after(400,updateBomb)

def updatePoint():
    global score
    score+=1
    if isAlive():
       scoreLable.after(3000, updatePoint)

def click():
    global bomb
    if isAlive():
      bomb+=1

def isAlive():
    global bomb
    global pressReturn
    if bomb <=0:
       label.config(text="BAAAAANG!")
       pressReturn=True
       return False
    else:
      return True



root=Tk()
root.title("Bang Bang")
root.geometry("550x550")

label=Label(root, text="Press[Enter] to start the game", font=('Comic Sans MS',12))
label.pack()

fuseLabke=Label(root, text="Bomb:" +str(bomb), font=('Comic Sans MS',14))
fuseLabke.pack()

scoreLable=Label(root, text="Score:" +str(score), font=('Comic Sans MS',14))
scoreLable.pack()

noPhoto=PhotoImage(file="img1.gif")
normalPhoto=PhotoImage(file="img2.gif")
bangPhoto=PhotoImage(file="img3.gif")

bombLable=Label(root, image=normalPhoto)
bombLable.pack()

bestScoreLabel=Label(root,text='Best Score: '+ str(bestScore),font=('Comic Sans MS', 14 ))
bestScoreLabel.pack()

clickButtom=Button(root, text="Click me", font=('Comic Sans MS',14), bg="#000000",fg="#ffffff",command=click, width=15)
clickButtom.pack()

root.bind('<Return>', start)

root.mainloop()