import pygame
import os

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Memory Card Game")

# Load and resize images
def load_image(name):
    path = os.path.join('assets/images', name)
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (100, 150))

card_back = load_image('card_back.png')
card_faces = [load_image(f'card{i}.png') for i in range(1, 9)]

# Layout parameters
rows, cols = 4, 4
card_width, card_height = 100, 150
padding = 20
grid_width = cols * card_width + (cols - 1) * padding
grid_height = rows * card_height + (rows - 1) * padding

start_x = (800 - grid_width) // 2
start_y = (600 - grid_height) // 2

# Draw grid
for row in range(rows):
    for col in range(cols):
        x = start_x + col * (card_width + padding)
        y = start_y + row * (card_height + padding)
        screen.blit(card_back, (x, y))

pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
