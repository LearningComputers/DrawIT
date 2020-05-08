import pygame, imagehash
from PIL import Image
from pygame.locals import *

pygame.init()
time= pygame.time.Clock()
sw=1000
sh=800
offset1=600
offset2=300
s=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Draw IT")

bg=pygame.transform.scale(pygame.image.load("Backroud.png"),(sw,sh))
personface=pygame.image.load("Face.png")
personbody=pygame.image.load("Body.png")
cn=pygame.image.load("Canvas.png")
cnrec=cn.get_rect()
cnst=pygame.transform.scale(pygame.image.load("CanvasStand.png"),(250,300))
rd=pygame.transform.scale(pygame.image.load("Redo.png"),(50,50))
rdrec=rd.get_rect()
crs=pygame.image.load("PEN.png")
crsrec=crs.get_rect()
def game():
    pygame.mouse.set_visible(False)
    while True:
        crsrec.bottomleft=pygame.mouse.get_pos()
        rdrec.topleft=(sw-rdrec[2],0)
        s.blit(bg,(0,0))
        pygame.draw.rect(bg,(255,0,0),((950,750),(50,30)))
        bg.blit(cn, (cnrec[0]+offset1,cnrec[1]+offset2))
        bg.blit(cnst, (cnrec[0]+offset1,cnrec[1]+offset2+150))
        bg.blit(personface, (200,15))
        bg.blit(personbody, (100,100))
        s.blit(crs,crsrec)
        bg.blit (rd, rdrec)
        pygame.display.update()
        time.tick(260)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>950 and pygame.mouse.get_pos()[1]>750:
                    pygame.image.save(cn, "output.png")
                    img1 = imagehash.average_hash(Image.open("output.png"))
                    Image.alpha_composite(Image.open("Canvas.png"), Image.open("Face.png")).save("output2.png")
                    img2 = imagehash.average_hash(Image.open("output2.png"))
                    imgn = img1-img2
                    if imgn==1:
                        print (1000)
                    if 2<=imgn<=3:
                        print (800)
                    if 4<=imgn<=5:
                        print (500)
                    print (imgn)
                if pygame.mouse.get_pos()[0]>rdrec[0]-rdrec[2] and pygame.mouse.get_pos()[1]>rdrec[1]-rdrec[3]:
                    print ("worked")
                    s.blit(cn, (cnrec[0]+offset1,cnrec[1]+offset2))
            if pygame.mouse.get_pressed()[0]:
                try:
                    pygame.draw.rect(cn,(0,0,0),((pygame.mouse.get_pos()[0]-offset1,pygame.mouse.get_pos()[1]-offset2),(4,4)))
                except AttributeError:
                    pass
game()
