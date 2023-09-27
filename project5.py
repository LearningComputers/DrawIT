import pygame, imagehash , pygame.freetype
from PIL import Image
from pygame.locals import *

pygame.init()
sw=1000
sh=sw*0.8
offset1=sw*0.6
offset2=sw*0.3
s=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Draw IT")

faceArray="Face1.png","Face2.png","Face3.png","Face4.png","Face5.png"
background=pygame.transform.scale(pygame.image.load("Backroud.png"),(sw,sh))
personface=pygame.image.load(faceArray[0])
personbody=pygame.image.load("Body.png")
canvas=pygame.image.load("Canvas.png")
canvasrec=canvas.get_rect()
canvasStand=pygame.transform.scale(pygame.image.load("CanvasStand.png"),(sw*0.025,sw*0.03))
redo=pygame.transform.scale(pygame.image.load("Redo.png"),(sw*0.05,sw*0.05))
redoBox=redo.get_rect()
redoAll=pygame.transform.scale(pygame.image.load("RedoAll.png"),(sw*0.05,sw*0.05))
redoAllBox=redoAll.get_rect()
cursor=pygame.image.load("PEN.png")
cursorrec=cursor.get_rect()
gf= pygame.freetype.SysFont("Comic Sans MS", sw*0.02)

pixelPos =[]

def game():
    x=0
    pygame.mouse.set_visible(False)
    gotpaid=False
    while True:
        def ref():
            cursorrec.bottomleft=pygame.mouse.get_pos()
            redoBox.topleft=(sw-redoBox[2],0)
            redoAllBox.topleft=(sw-redoBox[2]-redoAllBox[2],0)
            s.blit(background,(0,0))
            pygame.draw.rect(background,(255,0,0),((sw*0.95,sw*0.75),(sw*0.05,sw*0.03)))
            background.blit(canvas, (canvasrec[0]+offset1,canvasrec[1]+offset2))
            background.blit(canvasStand, (canvasrec[0]+offset1,canvasrec[1]+offset2+sw*0.125))
            background.blit(pygame.image.load(faceArray[x]), (sw*0.2, sw*0.015))
            background.blit(personbody, (sw*0.1,sw*0.1))
            s.blit(cursor,cursorrec)
            background.blit (redo, redoBox)
            background.blit (redoAll, redoAllBox)
            pygame.display.update()
        ref()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if gotpaid==True:
                x+=1
                gotpaid=False
            if event.type==MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>sw*0.95 and pygame.mouse.get_pos()[1]>sw*0.75:
                    pygame.image.save(canvas, "output.png")
                    img1 = imagehash.average_hash(Image.open("output.png"))
                    Image.alpha_composite(Image.open("Canvas.png"), Image.open(faceArray[x])).save("output2.png")
                    img2 = imagehash.average_hash(Image.open("output2.png"))
                    #print (img1,img2)
                    imgn = img1-img2
                    if imgn<=1:
                        gf.render_to(background, (450,150), "I pay 1000$ for this.", (0,0,0))
                        pygame.display.update()
                        gotpaid=True
                    elif 2<=imgn<=5:
                        gf.render_to(background, (450,150), "I pay 800$ for this.", (0,0,0))
                        pygame.display.update()
                        gotpaid=True
                    elif 6<=imgn<=10:
                        gf.render_to(background, (450,150), "I pay 500$ for this.", (0,0,0))
                        pygame.display.update()
                        gotpaid=True
                    elif 11<=imgn:
                        gf.render_to(background, (450,150), "Sorry, but this looks like garbage.", (0,0,0))
                        pygame.display.update()

                if pygame.mouse.get_pos()[0]>redoBox[0] and pygame.mouse.get_pos()[1]<redoBox[3]-redoBox[1]:
                    if len(pixelPos)<5:
                        for pixl in pixelPos:
                            pygame.draw.rect(canvas,(255,255,255),(pixl))
                    else:
                        i= len(pixelPos)-1
                        while i>= len(pixelPos)-1-4:
                            pygame.draw.rect(canvas,(255,255,255),(pixelPos[i]))
                            i-=1
                    if len(pixelPos)<5:
                        del(pixelPos[0:len(pixelPos)])
                    else:
                        del(pixelPos[len(pixelPos)-5:len(pixelPos)])
                if sw-redoBox[2]-redoAllBox[2]<pygame.mouse.get_pos()[0]<redoBox[0] and pygame.mouse.get_pos()[1]<redoAllBox[3]:
                    for pixl in pixelPos:
                            pygame.draw.rect(canvas,(255,255,255),(pixl))
                    del(pixelPos[0:len(pixelPos)])
            if pygame.mouse.get_pressed()[0]:
                try:
                    pygame.draw.rect(canvas,(0,0,0),((pygame.mouse.get_pos()[0]-offset1,pygame.mouse.get_pos()[1]-offset2),(4,4)))
                    if sw*0.6<pygame.mouse.get_pos()[0]<sw*0.85 and sw*0.3<pygame.mouse.get_pos()[1]<sw*0.6:
                        pixelPos.append(((pygame.mouse.get_pos()[0]-offset1,pygame.mouse.get_pos()[1]-offset2),(4,4)))
                except AttributeError:
                    pass
game()
