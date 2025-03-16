import pygame
import sys
import os
import random
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Card Game")
clock = pygame.time.Clock()

def load_image(name):
    path = os.path.join('assets/images', name)
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (100, 150))

# Load images
card_back = load_image('card_back.png')
card_faces = [load_image(f'card{i}.png') for i in range(1, 7)]

# Duplicate and shuffle cards
cards = card_faces * 2
random.shuffle(cards)

# Card setup
def create_card_grid():
    grid = []
    for row in range(ROWS):
        grid_row = []
        for col in range(COLUMNS):
            x = MARGIN + col * (CARD_WIDTH + SPACING)
            y = MARGIN + row * (CARD_HEIGHT + SPACING)
            rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
            grid_row.append({'rect': rect, 'image': cards.pop(), 'flipped': False, 'matched': False})
        grid.append(grid_row)
    return grid

grid = create_card_grid()
first_card = None
second_card = None
delay = 1000  # milliseconds
delay_start = None

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for row in grid:
                for card in row:
                    if card['rect'].collidepoint(pos) and not card['flipped'] and not card['matched']:
                        card['flipped'] = True
                        if not first_card:
                            first_card = card
                        elif not second_card and card != first_card:
                            second_card = card
                            delay_start = pygame.time.get_ticks()

    # Check for matching
    if first_card and second_card and delay_start:
        current_time = pygame.time.get_ticks()
        if current_time - delay_start > delay:
            if first_card['image'] == second_card['image']:
                first_card['matched'] = True
                second_card['matched'] = True
            else:
                first_card['flipped'] = False
                second_card['flipped'] = False
            first_card = None
            second_card = None
            delay_start = None

    # Draw cards
    for row in grid:
        for card in row:
            image = card['image'] if card['flipped'] or card['matched'] else card_back
            screen.blit(image, card['rect'])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
