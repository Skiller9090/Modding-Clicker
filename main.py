import pygame

points = 0

pygame.init()

root = pygame.display.set_mode((400,500))
pygame.display.set_caption("Arbitrary Clicker")
#What should i call it?

clock = pygame.time.Clock()

med_font = pygame.font.Font(None, 16)
big_font = pygame.font.Font(None, 32)

but_dim = (125, 110, 150, 150)

white = [255,255,255]
bright_red = [255,0,0]

stop = False

while not stop:
    #Set bg color
    root.fill(white)

    #Set up points counter
    point_counter = "Points: " + str(points) 
    point_text = med_font.render(point_counter, True, [0,0,0])

    point_text_rect = point_text.get_rect()
    point_text_rect.center = (60,20)
    
    root.blit(point_text, point_text_rect)

    #Read mouse pos for button interactivity
    mouse_pos = pygame.mouse.get_pos()
    mouse_isclicked = pygame.mouse.get_pressed()


    click_button = pygame.draw.rect(root, bright_red, but_dim)
    button_text = big_font.render("Click", True, white) # N N L H
    but_l = click_button.center[0] - button_text.get_rect()[2]/2
    but_h = click_button.center[1] - button_text.get_rect()[3]/2
    but = (but_l,but_h)
    root.blit(button_text,but)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

        if mouse_isclicked[0] == 1:
            if click_button.collidepoint(mouse_pos):
                points += 1
        #print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()