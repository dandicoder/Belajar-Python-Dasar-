import pygame

# init
pygame.init()

isRun = True

# ukuran display
window_p = 500
window_l = 500

# garis x y
x = 250
y = 250

# ukuran kotak
panjang = 20
lebar = 20

speed = 10

# membuat window surface object
window = pygame.display.set_mode((window_p, window_l))
# user input/ database input
while isRun:
    pygame.time.delay(20)
    for events in pygame.event.get():
        if events.type == pygame.QUIT :
            isRun = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0 :
        x -= speed
    
    if keys[pygame.K_RIGHT] and x < window_l - lebar:
        x += speed

    if keys[pygame.K_UP] and y > 0 :
        y -= speed
    
    if keys[pygame.K_DOWN] and y < window_p - panjang:
        y += speed

    # update assets
    window.fill((255,255,255))

    pygame.draw.rect(window, (0,0,0) , (x, y, lebar, panjang))


    # render ke display
    pygame.display.update()


pygame.quit()