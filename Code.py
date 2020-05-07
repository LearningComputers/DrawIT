import pygame, imagehash
from PIL import Image
from pygame.locals import *

pygame.init()
time= pygame.time.Clock()
sw=1000
sh=800
offset=200
s=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Draw IT")

bg=pygame.transform.scale(pygame.image.load("Backroud.png"),(sw,sh))
cn=pygame.image.load("Canvas.png")
cnrec=cn.get_rect()
crs=pygame.image.load("PEN.png")
crsrec=crs.get_rect()
def game():
    pygame.mouse.set_visible(False)
    while True:
        crsrec.bottomleft=pygame.mouse.get_pos()
        s.blit(bg,(0,0))
        pygame.draw.rect(bg,(255,0,0),((950,750),(50,30)))
        bg.blit(cn, (cnrec[0]+offset,cnrec[1]+offset))
        s.blit(crs,crsrec)
        pygame.display.update()
        time.tick(260)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>950 and pygame.mouse.get_pos()[1]>750:
                    pygame.image.save(cn, "output.png")
                    img1 = imagehash.average_hash(Image.open("output.png"))
                    img2 = imagehash.average_hash(Image.open("Face.png"))
                    imgn = img1-img2
                    print(img1)
                    print(img2)
                    print(imgn)

                    
            if pygame.mouse.get_pressed()[0]:
                try:
                    pygame.draw.rect(cn,(0,0,0),((pygame.mouse.get_pos()[0]-offset,pygame.mouse.get_pos()[1]-offset),(4,4)))
                except AttributeError:
                    pass
game()
