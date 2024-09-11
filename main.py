import pygame
import sys
import subprocess

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Tic Tac Toe Menu")

button_width, button_height = 200, 50
button_font = pygame.font.SysFont(None, 30)

ai_button_rect = pygame.Rect(200, 100, button_width, button_height)
player_button_rect = pygame.Rect(200, 200, button_width, button_height)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def draw_button(screen, rect, text, color):
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, BLACK)
    screen.blit(text_surface, (rect.x + 20, rect.y + 10))

def run_file(file_name):
    subprocess.run(['python', file_name])

running = True
while running:
    screen.fill(WHITE)

    # Draw the buttons
    draw_button(screen, ai_button_rect, "Play vs AI", GRAY)
    draw_button(screen, player_button_rect, "Multiplayer", GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Check if the AI button was clicked
            if ai_button_rect.collidepoint(mouse_pos):
                print("AI Mode Selected")
                run_file('ai.py')  # Run the AI version of the game

            # Check if the Multiplayer button was clicked
            if player_button_rect.collidepoint(mouse_pos):
                print("Multiplayer Mode Selected")
                run_file('multiplayer.py')  # Run the multiplayer version of the game

    pygame.display.flip()

pygame.quit()
sys.exit()
