import pygame
import sys
import energysources

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TILE_SIZE = 50

BOARD_WIDTH = 6
BOARD_HEIGHT = 7
BOARD_OFFSET_X = 50  # Offset from the left side
BOARD_OFFSET_Y = (SCREEN_HEIGHT - (BOARD_HEIGHT * TILE_SIZE)) // 2 + 50

BAR_WIDTH = 500
BAR_HEIGHT = 30
BAR_COLOR = (0, 255, 0)  # Green

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

FPS = 60 

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Energy Board")

def draw_status_bar(happiness): 
    if happiness > 0.35:
        BAR_COLOR = (0, 255, 0) # Green
    elif (happiness < 0.35 and happiness > 0.15): 
        BAR_COLOR = (255, 255, 0)  # Yellow
    else:
        BAR_COLOR = (255, 0, 0)  # Red  
        
    
    # Draw outline of progress bar
    pygame.draw.rect(screen, BAR_COLOR, ((SCREEN_WIDTH //2)-(BAR_WIDTH//2), 80, BAR_WIDTH, BAR_HEIGHT), 2).center 

    # Calculate the width of the filled portion of the progress bar
    filled_width = BAR_WIDTH * happiness

    # Draw filled portion of progress bar
    pygame.draw.rect(screen, BAR_COLOR, ((SCREEN_WIDTH //2)-(BAR_WIDTH//2), 80, filled_width, BAR_HEIGHT)).center

    # Add title
    font = pygame.font.Font(None, 24)
    title_text = font.render("Customer Satisfaction", True, BLACK)
    title_rect = title_text.get_rect(center=((SCREEN_WIDTH //2) , 60))
    screen.blit(title_text, title_rect)

def draw_climate_balance(sun_level, wind_speed, balance): 
        font_title = pygame.font.Font(None, 40)   
        font = pygame.font.Font(None, 24) 
        climate_title_text = font_title.render("CLIMATE", True, BLACK) 
        climate_sun_text = font.render("Sun level: " + str(sun_level), True, BLACK) 
        climate_wind_text = font.render("Wind speed: " + str(wind_speed), True, BLACK) 

        balance_text = font_title.render("BALANCE (in millions): ", True, BLACK) 
        money_text = font.render("$" + str(balance), True, BLACK)

        climate_title_text_rect = climate_title_text.get_rect() 
        climate_title_text_rect.center = (SCREEN_WIDTH // 4, 170) 

        climate_sun_text_rect = climate_sun_text.get_rect() 
        climate_sun_text_rect.center = (SCREEN_WIDTH // 4, 190)  

        climate_wind_text_rect = climate_wind_text.get_rect() 
        climate_wind_text_rect.center = (SCREEN_WIDTH // 4, 210) 

        balance_text_rect = balance_text.get_rect() 
        balance_text_rect.center = (SCREEN_WIDTH // 4 + SCREEN_WIDTH //2, 170)

        money_text_rect = balance_text.get_rect() 
        money_text_rect.center = (3* SCREEN_WIDTH // 4, 200)

        screen.blit(climate_title_text, climate_title_text_rect)
        screen.blit(climate_sun_text, climate_sun_text_rect)
        screen.blit(climate_wind_text, climate_wind_text_rect) 
        screen.blit(balance_text, balance_text_rect) 
        screen.blit(money_text, money_text_rect) 



# Function to draw the board
def draw_board(board):
    # Add title to board
    font = pygame.font.Font(None, 24)
    title_text = font.render("Energy Board", True, BLACK)
    title_rect = title_text.get_rect(center=(BOARD_OFFSET_X + TILE_SIZE * board.width / 2, BOARD_OFFSET_Y - 20))
    screen.blit(title_text, title_rect)


    for y, row in enumerate(board.board):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE + BOARD_OFFSET_X, 
                y * TILE_SIZE + BOARD_OFFSET_Y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, GRAY, rect)
            if tile.terrain == "plateau":
                pygame.draw.rect(screen, GREEN, rect.inflate(-5, -5))
            elif tile.terrain == "ocean":
                pygame.draw.rect(screen, BLUE, rect.inflate(-5, -5))
            elif tile.terrain == "swamp":
                pygame.draw.rect(screen, BROWN, rect.inflate(-5, -5))
            if tile.energy_source:
                pygame.draw.circle(screen, BLACK, rect.center, 5)
def key(): 
    #defining the rectangle 

    font_title = pygame.font.Font(None, 40)   
    font = pygame.font.Font(None, 24)  

    key_text = font_title.render("KEY: ", True, BLACK) 
    key_text_rect = key_text.get_rect() 
    key_text_rect.center = ((SCREEN_WIDTH) // 4, 600) 

    #drawing the rectangles 
    plateau_rect = pygame.draw.rect(screen, GREEN, 
        pygame.Rect(150, 660, 20, 20))

    ocean_rect = pygame.draw.rect(screen, BLUE, 
        pygame.Rect(150, 700, 20, 20))    

    swamp_rect = pygame.draw.rect(screen, BROWN, 
        pygame.Rect(150, 740, 20, 20))  

    plateau_text = font.render("Plateau", True, BLACK) 
    ocean_text = font.render("Ocean", True, BLACK) 
    swamp_text = font.render("Swamp", True, BLACK)   

    plateau_text_rect = plateau_text.get_rect() 
    ocean_text_rect = ocean_text.get_rect() 
    swamp_text_rect = swamp_text.get_rect()

    plateau_text_rect.center = (SCREEN_WIDTH // 4 + 10, 670)
    ocean_text_rect.center = (SCREEN_WIDTH // 4 + 10, 710)
    swamp_text_rect.center = (SCREEN_WIDTH // 4 + 10, 750)

    screen.blit(plateau_text, plateau_text_rect)
    screen.blit(ocean_text, ocean_text_rect)
    screen.blit(swamp_text, swamp_text_rect) 




# Main function
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        draw_status_bar(energysources.customer.happiness)
        draw_climate_balance(energysources.c.sunlight, energysources.c.wind_speed, energysources.balance)
        draw_board(energysources.starting_board_1)  # Draw your starting board
        key()
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()