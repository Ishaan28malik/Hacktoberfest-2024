import pygame
#initialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,800))

pygame.display.set_caption("techvidhaan -magic square solver")
font=pygame.font.Font("freesansbold.ttf",30)
text=font.render("Magic Square Solver",True,(0,255,0))
basic_font=pygame.font.Font(None,25)
text_show=basic_font.render("Enter Value n for a magic square:",True,(255,255,255))
textRect=text.get_rect()
textRect.center=(400,150)



user_text=''
input_rect=pygame.Rect(290,200,240,32)
color_active=pygame.Color('lightskyblue3')
color_passive=pygame.Color('gray15')


color=color_passive
active=False
running=True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active=True
            else:
                active=False
        if event.type==pygame.KEYDOWN:
            if active==True:
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                else:
                    user_text+=event.unicode
                if event.key==pygame.K_RETURN:
                    generateSquare(int(user_text))

    screen.fill((0,0,0))
    if active:
        color=color_active
    else:
        color=color_passive
    pygame.draw.rect(screen,color,input_rect,2)
    screen.blit(text, textRect)
    screen.blit(text_show, (0, 200))
    text_surface = basic_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    input_rect.w=text_surface.get_width()+10

    pygame.display.update()