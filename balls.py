import pygame
from colorsys import hsv_to_rgb, rgb_to_hsv

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

N = 150
# create N hue, saturation, value tuples
HSV = []
for i in range(N):
    HSV.append((i / N, 0.9, 1))  # changing only the hue creates a spectrum

# convert HSV to RGB
unit_RGB = []
for color in HSV:
    unit_RGB.append(hsv_to_rgb(color[0], color[1], color[2]))

# convert the 0-1 valued unit_RGBs to RGBs from 0-255
RGB = []
for color in unit_RGB:
    RGB.append([color[0] * 255, color[1] * 255, color[2] * 255])


class Ball:
    def __init__(self, color, size, v):
        
        self.image = pygame.Surface([size[0], size[1]])
        
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        pygame.draw.ellipse(self.image, color, [0, 0, size[0], size[1]])
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        self.rect.center = [180, 330]
        self.bound = [360, 660]
        self.dx = v[0]
        self.dy = v[1]
        
    def color(self, color):
        self.image.fill(GREEN)
        pygame.draw.ellipse(self.image, color, [0, 0, self.rect.w, self.rect.h])
        
        
    def update(self):
        e = 1
        if self.rect.top <= 0 or self.rect.bottom >= self.bound[1]:
              self.dy *= -e
        if self.rect.left <= 0 or self.rect.right >= self.bound[0]:
              self.dx *= -e
              
        self.rect.x += self.dx
        self.rect.y += self.dy
    
        
size = 60
velocity = 50
balls = [Ball(BLUE, [size, size//2], [-velocity, -velocity]), Ball(BLUE, [size//2, size], [-velocity, -velocity]),
         Ball(BLUE, [size, size//2], [velocity, -velocity]), Ball(BLUE, [size//2, size], [velocity, -velocity])]

def main(screen):

    clock = pygame.time.Clock()
    done = False
    frame = 0
    while not done:
        frame += 1
        if frame >= len(RGB) - 1:  # loop frame counter back
            frame = 0
        
        for ball in balls:
            ball.color(RGB[frame])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                for ball in balls:
                    ball.bound = [event.w, event.h]
                    
                
            # if event.type == pygame.MOUSEMOTION:
                
                # print(pygame.mouse.get_rel())
                
                # b1.mouse_motion(pygame.mouse.get_rel())
                # b2.mouse_motion(pygame.mouse.get_rel())
                
                # offset = (b2.rect.x - b1.rect.x, b2.rect.y - b1.rect.y)
                # print(b1.mask.overlap_area(b2.mask, offset))
                
            if pygame.mouse.get_pressed()[1]:
                
                for ball in balls:
                    ball.rect.center = [screen.get_width()//2, screen.get_height()//2]
        
                
        for ball in balls:
            ball.update()
            screen.blit(ball.image, ball.rect)
            
        pygame.display.update()

        clock.tick(30)
        
if __name__ == "__main__":
    pygame.display.init()
    screen = pygame.display.set_mode([360, 660], pygame.RESIZABLE)
    pygame.display.set_caption("Balls")
    
    main(screen)
    pygame.quit()
    
