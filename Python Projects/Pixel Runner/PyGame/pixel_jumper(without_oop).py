# Running 2D game (Pixel Jumper) using PyGame
# Without advanced features like OOP, classes, etc.

import pygame
from sys import exit
from  random import randint, choices

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surface = game_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center= (400,57))
    wn.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300:
                wn.blit(snail_surface, obstacle_rect)
            else:
                wn.blit(fly_surface, obstacle_rect)
                        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surface, player_index
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)] 

#Game Window
pygame.init()
wn= pygame.display.set_mode((800,400))
pygame.display.set_caption("PIXEL JUMPER")
clock = pygame.time.Clock()
game_active = False
game_font = pygame.font.Font('E:\Game development with Python\Pixeltype.ttf', 60)
start_time = 0
score = 0

# Game background surface
sky_surface = pygame.image.load('E:\Game development with Python\PyGame\graphics\Sky.png').convert()
ground_surface = pygame.image.load('E:\Game development with Python\PyGame\graphics\ground.png').convert()

# Enemy surface (snail and fly)
snail_frame1 = pygame.image.load('E:\Game development with Python\PyGame\graphics\snail\snail1.png').convert_alpha()
snail_framw2 = pygame.image.load('E:\Game development with Python\PyGame\graphics\snail\snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_framw2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load('E:\Game development with Python\PyGame\graphics\Fly\Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('E:\Game development with Python\PyGame\graphics\Fly\Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

# Player surface
player_walk_1 = pygame.image.load('E:\Game development with Python\PyGame\graphics\Player\player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('E:\Game development with Python\PyGame\graphics\Player\player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('E:\Game development with Python\PyGame\graphics\Player\jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(topleft= (60,220))
player_gravity = 0



# Intro screen
intro_screen_surface = pygame.image.load('E:\Game development with Python\PyGame\graphics\intro_screen.png').convert_alpha()
intro_screen_rect = intro_screen_surface.get_rect(center = (400,200))

# Game over screen
game_over_surface = pygame.image.load('E:\Game development with Python\PyGame\graphics\game_over.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center = (400,200))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)




# Game Mainloop
while True:
    
    # Event loop to close the game
    for event in pygame.event.get():
        
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:
            
            if player_rect.bottom == 300:
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20  
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RETURN:
                        player_gravity = -20
        else:
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                start_time = pygame.time.get_ticks()
                
        if game_active:   
                 
            if event.type == obstacle_timer:
                
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright= (randint(900, 1100),300)))
                    
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright= (randint(900, 1100),210)))   
                    
            if event.type == snail_animation_timer:
                
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                    
                snail_surface = snail_frames[snail_frame_index]
                
            if event.type == fly_animation_timer:
                
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                    
                fly_surface = fly_frames[fly_frame_index]
                
                     
    if game_active:
        
        # Surafce drawing            
        wn.blit(sky_surface, (0,0))
        wn.blit(ground_surface, (0,300))
        
        score = display_score()
        
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        elif player_rect.top <= 0:
            player_rect.top= 0
            
        player_animation()
        wn.blit(player_surface, player_rect)
        
        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)
        
        
    else:
        
        score_surface = game_font.render(f'{score}', False, (120, 67, 230))
        score_rect = score_surface.get_rect(center= (537, 343))
        obstacle_rect_list.clear()
        
        if score == 0:
            
            # Intro screen display
            wn.blit(intro_screen_surface, intro_screen_rect)
            
        else:
            
            # Game over screen display
            wn.blit(game_over_surface, game_over_rect)
            wn.blit(score_surface, score_rect)
           
            
        player_rect.midbottom = (80, 300)
        player_gravity = 0
                    
    # Updates every frame 
    pygame.display.update()
    clock.tick(60) # set the max frame-rate to 60fps.