## Turtle Dahil etme
import turtle
import math
import random

skor = 0
canHakki = 3
maksHedef = 5
maksDusman = 5
hedefler = []
dusmanlar = []
oyuncuHizi = 1

## Ekran ayarlama
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.tracer(3)

## Sınır Çizme
mypen = turtle.Turtle()
mypen2 = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


## Oyuncu oluşturma
oyuncu = turtle.Turtle()
oyuncu.color("purple")
oyuncu.shape("triangle")
oyuncu.penup() ## iz bırakmayı engelleme
oyuncu.speed(0)


## Hedefleri Yerleştirme
for indeks in range(maksHedef):
    hedefler.append(turtle.Turtle())
    hedefler[indeks].color("blue")
    hedefler[indeks].shape("circle")
    hedefler[indeks].penup()
    hedefler[indeks].speed(0)
    hedefler[indeks].setposition(random.randint(-300,300),random.randint(-300,300))

## Dusmanları Ayarlama
for indeks in  range(maksDusman):
    dusmanlar.append(turtle.Turtle())
    dusmanlar[indeks].color("Red")
    dusmanlar[indeks].shape("square")
    dusmanlar[indeks].penup()
    dusmanlar[indeks].speed(0)
    dusmanlar[indeks].setposition(random.randint(-300,300),random.randint(-300,300))


def solaDon():
    oyuncu.left(30) ## 30 derece sola dön

def sagaDon():
    oyuncu.right(30) ## 30 derece sağa dön

def hedefKontrol(oyuncu,hedef):
    d = math.sqrt(math.pow(oyuncu.xcor()-hedef.xcor(),2) + math.pow(oyuncu.ycor()-hedef.ycor(),2))
    if d < 20:
        return True
    else:
        return False

def dusmanKontrol(oyuncu,dusman):
    d = math.sqrt(math.pow(oyuncu.xcor()-dusman.xcor(),2) + math.pow(oyuncu.ycor()-dusman.ycor(),2))
    if d < 20:
        return True
    else:
        return False

## Klavye dinleme 
turtle.listen()
turtle.onkey(solaDon , "Left")
turtle.onkey(sagaDon, "Right")

while True:
    oyuncu.forward(oyuncuHizi)
   
    ## Oyuncunun Sınır Kontrolü
    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180) ## Geriye dön
    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)

    for indeks in range(maksHedef):
        hedefler[indeks].forward(1)
        ## Hedefler için sınır kontrolü
        if hedefler[indeks].xcor() > 290 or hedefler[indeks].xcor() < -290:
            hedefler[indeks].right(180)
        if hedefler[indeks].ycor() > 290 or hedefler[indeks].ycor() < -290:
            hedefler[indeks].right(180)

        if hedefKontrol(oyuncu,hedefler[indeks]):
            hedefler[indeks].setposition(random.randint(-300,300),random.randint(-300,300))
            hedefler[indeks].right(random.randint(0,360))
            skor += 10
        
        ## Ekrana skor yazma
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            skorString = "Skor: %s" %skor
            mypen.write(skorString,False,align="left",font=("Arial",14,"normal"))



    for indeks in range(maksDusman):
        dusmanlar[indeks].forward(1)
        ## dusmanlar için sınır kontrolü
        if dusmanlar[indeks].xcor() > 290 or dusmanlar[indeks].xcor() < -290:
            dusmanlar[indeks].right(180)
        if dusmanlar[indeks].ycor() > 290 or dusmanlar[indeks].ycor() < -290:
            dusmanlar[indeks].right(180)

        if dusmanKontrol(oyuncu,dusmanlar[indeks]):
            dusmanlar[indeks].setposition(random.randint(-300,300),random.randint(-300,300))
            dusmanlar[indeks].right(random.randint(0,360))
            canHakki -= 1
            skor -= 20
        
        ## Ekrana can yazma
            mypen2.undo()
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(-290,330)
            canString = "Can: %s" %canHakki
            mypen2.write(canString,False,align="left",font=("Arial",14,"normal"))
            mypen.undo()
            mypen.penup()
            mypen.setposition(-290,310)
            skorString = "Skor: %s" %skor
            mypen.write(skorString,False,align="left",font=("Arial",14,"normal"))

    if canHakki == 0:
        mypen.hideturtle()
        mypen.penup()
        mypen.setposition(0,0)
        mypen.write("OYUN BİTTİ..",False,align="center",font = ("Arial",50,"normal"))
        mypen2.penup()
        mypen2.setposition(0,-50)
        mypen2.write("SKORUNUZ: %s" %skor,False,align="center",font = ("Arial",50,"normal"))










    
