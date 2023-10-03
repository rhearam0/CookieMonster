import pygame
import time
import random
pygame.font.init() #initalize font module 

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COOKIE MONSTER")

BG = pygame.transform.scale(pygame.image.load("monster.jpeg"), (WIDTH, HEIGHT)) #putting the background image 

#Creating the character (LABELING THE VARIABLES)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 70

PLAYER_VEL = 5
COOKIE_WIDTH = 30
COOKIE_HEIGHT = 20
COOKIE_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30) #create the font object


def draw(player, elapsed_time, cookies): 
    WIN.blit(BG, (0, 0))  #blit is used when wanting to draw something on the screen 

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")  #rounding elapside time to a minute and f string to  have string and s to have seconds
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "white", player)

    for cookie in cookies:
        pygame.draw.rect(WIN, "tan", cookie)

    pygame.display.update() #will take all the updates and edits and apply to the screen 


def main():
    run = True

    player = pygame.Rect(600, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT) #is our player with dimensions 
    clock = pygame.time.Clock()
    start_time = time.time() 
    elapsed_time = 0

    cookie_add_increment = 2000
    cookie_count = 0

    cookies = []
    hit = False

    while run:
        cookie_count += clock.tick(60)
        elapsed_time = time.time() - start_time #subtracting the time we started with time to see how much time has elapsed since the game has started

        if cookie_count > cookie_add_increment:
            for _ in range(3):
                cookie_x = random.randint(0, WIDTH - COOKIE_WIDTH)
                cookie = pygame.Rect(cookie_x, -COOKIE_HEIGHT,
                                   COOKIE_WIDTH, COOKIE_HEIGHT)
                cookies.append(cookie)

            cookie_add_increment = max(200, cookie_add_increment - 50)
            cookie_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break #will allow the game when user QUIT, end the game 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:  #code for left arrow key
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for cookie in cookies[:]:
            cookie.y += COOKIE_VEL
            if cookie.y > HEIGHT:
                cookies.remove(cookie)
            elif cookie.y + cookie.height >= player.y and cookie.colliderect(player):
                cookies.remove(cookie)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost Your Cookies!", 1, "white") #generate text
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2)) #draw on screnn
            pygame.display.update() 
            pygame.time.delay(4000) #freeze game
            break   #break and game ends

        draw(player, elapsed_time, cookies)    #calling the draw function

    pygame.quit()  #closes the pygame 


if __name__ == "__main__":
    main()  #calling the name function