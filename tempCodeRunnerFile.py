    current_time = pygame.time.get_ticks()
        if current_time - delay_start > delay:
            if first_card['id'] == second_card['id']:
                first_card['matched'] = True
                second_card['matched'] = True
            else:
                first_card['flipped'] = False
                second_card['flipped'] = False
            first_card = None
            second_card = None
            delay_start = None