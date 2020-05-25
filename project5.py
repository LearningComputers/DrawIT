import pygame, imagehash , pygame.freetype
from PIL import Image
from pygame.locals import *

pygame.init()
sw=1000
sh=800
offset1=600
offset2=300
s=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Draw IT")

fcnr="Face1.png","Face2.png","Face3.png","Face4.png","Face5.png"
bg=pygame.transform.scale(pygame.image.load("Backroud.png"),(sw,sh))
personface=pygame.image.load(fcnr[0])
personbody=pygame.image.load("Body.png")
cn=pygame.image.load("Canvas.png")
cnrec=cn.get_rect()
cnst=pygame.transform.scale(pygame.image.load("CanvasStand.png"),(250,300))
rd=pygame.transform.scale(pygame.image.load("Redo.png"),(50,50))
rdrec=rd.get_rect()
rdpls=pygame.transform.scale(pygame.image.load("RedoPlus.png"),(50,50))
rdplsrec=rdpls.get_rect()
crs=pygame.image.load("PEN.png")
crsrec=crs.get_rect()
gf= pygame.freetype.SysFont("Comic Sans MS", 20)

pixlpos =[]

def game():
    x=0
    pygame.mouse.set_visible(False)
    gotpaid=False
    while True:
        def ref():
            crsrec.bottomleft=pygame.mouse.get_pos()
            rdrec.topleft=(sw-rdrec[2],0)
            rdplsrec.topleft=(sw-rdrec[2]-rdplsrec[2],0)
            s.blit(bg,(0,0))
            pygame.draw.rect(bg,(255,0,0),((950,750),(50,30)))
            bg.blit(cn, (cnrec[0]+offset1,cnrec[1]+offset2))
            bg.blit(cnst, (cnrec[0]+offset1,cnrec[1]+offset2+150))
            bg.blit(pygame.image.load(fcnr[x]), (200, 15))
            bg.blit(personbody, (100,100))
            s.blit(crs,crsrec)
            bg.blit (rd, rdrec)
            bg.blit (rdpls, rdplsrec)
            pygame.display.update(s)
        ref()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if gotpaid==True:
                x+=1
                gotpaid=False
            if event.type==MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>950 and pygame.mouse.get_pos()[1]>750:
                    pygame.image.save(cn, "output.png")
                    img1 = imagehash.average_hash(Image.open("output.png"))
                    Image.alpha_composite(Image.open("Canvas.png"), Image.open(fcnr[x])).save("output2.png")
                    img2 = imagehash.average_hash(Image.open("output2.png"))
                    #print (img1,img2)
                    imgn = img1-img2
                    if imgn<=1:
                        gf.render_to(bg, (450,150), "I pay 1000$ for this.", (0,0,0))
                        pygame.display.update()
                        gotpaid=True
                    if 2<=imgn<=5:
                        gf.render_to(bg, (450,150), "I pay 800$ for this.", (0,0,0))
                        pygame.display.update()
                        gotpaid=True
                    if 6<=imgn<=10:
                        gf.render_to(bg, (450,150), "I pay 500$ for this.", (0,0,0))
                        pygame.display.update()
                        gotpaid=True
                    if 11<=imgn:
                        gf.render_to(bg, (450,150), "Sorry, but this looks like garbage.", (0,0,0))
                        pygame.display.update()

                if pygame.mouse.get_pos()[0]>rdrec[0] and pygame.mouse.get_pos()[1]<rdrec[3]-rdrec[1]:
                    if len(pixlpos)<5:
                        for pixl in pixlpos:
                            pygame.draw.rect(cn,(255,255,255),(pixl))
                    else:
                        i= len(pixlpos)-1
                        while i>= len(pixlpos)-1-4:
                            pygame.draw.rect(cn,(255,255,255),(pixlpos[i]))
                            i-=1
                    if len(pixlpos)<5:
                        del(pixlpos[0:len(pixlpos)])
                    else:
                        del(pixlpos[len(pixlpos)-5:len(pixlpos)])
                if sw-rdrec[2]-rdplsrec[2]<pygame.mouse.get_pos()[0]<rdrec[0] and pygame.mouse.get_pos()[1]<rdplsrec[3]:
                    for pixl in pixlpos:
                            pygame.draw.rect(cn,(255,255,255),(pixl))
                    del(pixlpos[0:len(pixlpos)])
            if pygame.mouse.get_pressed()[0]:
                try:
                    pygame.draw.rect(cn,(0,0,0),((pygame.mouse.get_pos()[0]-offset1,pygame.mouse.get_pos()[1]-offset2),(4,4)))
                    if 600<pygame.mouse.get_pos()[0]<850 and 300<pygame.mouse.get_pos()[1]<600:
                        pixlpos.append(((pygame.mouse.get_pos()[0]-offset1,pygame.mouse.get_pos()[1]-offset2),(4,4)))
                except AttributeError:
                    pass
game()