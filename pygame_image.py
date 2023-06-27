import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    #koukaton_list =  [koukaton_img,pg.transform.rotozoom(koukaton_img, 1, 1.0), pg.transform.rotozoom(koukaton_img, 2, 1.0), pg.transform.rotozoom(koukaton_img, 3, 1.0), pg.transform.rotozoom(koukaton_img, 4, 1.0), pg.transform.rotozoom(koukaton_img, 5, 1.0), pg.transform.rotozoom(koukaton_img, 6, 1.0), pg.transform.rotozoom(koukaton_img, 7, 1.0), pg.transform.rotozoom(koukaton_img, 8, 1.0), pg.transform.rotozoom(koukaton_img, 9, 1.0), pg.transform.rotozoom(koukaton_img, 10, 1.0), pg.transform.rotozoom(koukaton_img, 9, 1.0), pg.transform.rotozoom(koukaton_img, 8, 1.0), pg.transform.rotozoom(koukaton_img, 7, 1.0), pg.transform.rotozoom(koukaton_img, 6, 1.0), pg.transform.rotozoom(koukaton_img, 5, 1.0), pg.transform.rotozoom(koukaton_img, 4, 1.0), pg.transform.rotozoom(koukaton_img, 3, 1.0), pg.transform.rotozoom(koukaton_img, 2, 1.0), pg.transform.rotozoom(koukaton_img, 1, 1.0)]
    koukaton_list = [koukaton_img,pg.transform.rotozoom(koukaton_img, 10,1.0)]
    gb_img = pg.transform.flip(bg_img,True,False)
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0 - x, 0])
        screen.blit(gb_img,[1600 - x , 0])
        screen.blit(bg_img, [3200 - x, 0])
        screen.blit(koukaton_list[tmr%2],[300,200])
        
        pg.display.update()
        tmr += 1     
        x += 1
        if x >= 3200:
            x = 0   
            
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()




    