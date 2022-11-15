import time
import pygame


def main():
    pygame.init()
    win = pygame.display.set_mode((500,500))
    x = 50
    y = 50
    
    run = True
    while run:
        pygame.time.delay(100)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 10
        if keys[pygame.K_DOWN]:
            y += 10
        if keys[pygame.K_RIGHT]:
            x += 10
        if keys[pygame.K_LEFT]:
            x -= 10

        win.fill((0,0,0))
        pygame.draw.rect(win,(255,0,0),(x,y,30,50))
        pygame.display.update()

    time.sleep(2)

    pygame.quit()
if __name__ == "__main__":
    main()