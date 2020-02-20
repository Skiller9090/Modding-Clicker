import pygame


class Player():
    def __init__(self):
        self.points = 0
        self.click_power = 1


class Costs():
    def __init__(self):
        self.base_click = 10


player = Player()
costs = Costs()

pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Arbitrary Clicker")
# What should i call it?

clock = pygame.time.Clock()

med_font = pygame.font.Font(None, 16)
big_font = pygame.font.Font(None, 32)

click_button_dim = (125, 110, 150, 150)
upgrade_dim = (125, 260, 150, 150)

white = [255, 255, 255]
bright_red = [255, 0, 0]
bright_blue = [0, 0, 255]

stop = False

while not stop:
    # Set bg color
    screen.fill(white)

    # Set up points counter
    point_counter = "Points: " + str(player.points)
    point_text = med_font.render(point_counter, True, [0, 0, 0])

    point_text_rect = point_text.get_rect()
    point_text_rect.center = (60, 20)
    screen.blit(point_text, point_text_rect)

    # Read mouse pos for button interactivity
    mouse_pos = pygame.mouse.get_pos()
    mouse_isclicked = pygame.mouse.get_pressed()

    click_button = pygame.draw.rect(screen, bright_red, click_button_dim)
    upgrade_button = pygame.draw.rect(screen, bright_blue, upgrade_dim)

    button_text = big_font.render("Click", True, white)  # N N L H
    button_length = click_button.center[0] - button_text.get_rect()[2]/2
    button_height = click_button.center[1] - button_text.get_rect()[3]/2
    button_placement = (button_length, button_height)
    screen.blit(button_text, button_placement)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

        if mouse_isclicked[0] == 1:
            if click_button.collidepoint(mouse_pos):
                player.points += player.click_power

            if upgrade_button.collidepoint(mouse_pos):
                if player.points >= costs.base_click:
                    player.points -= costs.base_click
                    costs.base_click += 10
                    player.click_power += 1
        # print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
