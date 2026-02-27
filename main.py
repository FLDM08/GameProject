import pygame

print('Setup started')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup finished')

print('Loop started')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # Close pygame
