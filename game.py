import pygame
import sys
import energysources
import random

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
 

button_width = 300
button_height = 60

button_1_location_x = 5/9 * SCREEN_WIDTH
button_1_location_y = SCREEN_HEIGHT // 2 - 25 #windmill btn 

button_2_location_y = SCREEN_HEIGHT // 2 + 75 #turbine btn
button_3_location_y = SCREEN_HEIGHT // 2 + 175 #solar panel btn 

button_buy_location_y = SCREEN_HEIGHT // 2 - 125
button_sell_location_x = 5/9 * SCREEN_WIDTH + 165



# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Terrawatts")

def draw_button(x, y, width, height, color, text):
    font = pygame.font.Font(None, 24)
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

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
        climate_sun_text_rect.center = (SCREEN_WIDTH // 4, 200)  

        climate_wind_text_rect = climate_wind_text.get_rect() 
        climate_wind_text_rect.center = (SCREEN_WIDTH // 4, 220) 

        balance_text_rect = balance_text.get_rect() 
        balance_text_rect.center = (SCREEN_WIDTH // 4 + SCREEN_WIDTH //2, 190)

        money_text_rect = balance_text.get_rect() 
        money_text_rect.center = (SCREEN_WIDTH - SCREEN_WIDTH //12 , 230)

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
                screen.blit(tile.image, (x * TILE_SIZE + BOARD_OFFSET_X, y * TILE_SIZE + BOARD_OFFSET_Y))
def key(): 
    #defining the rectangle 

    font_title = pygame.font.Font(None, 40)   
    font = pygame.font.Font(None, 24)  

    key_text = font_title.render("KEY: ", True, BLACK) 
    key_text_rect = key_text.get_rect() 
    key_text_rect.center = ((SCREEN_WIDTH) // 4, 600) 

    #drawing the rectangles 
    pygame.draw.rect(screen, GREEN, 
        pygame.Rect(150, 660, 20, 20))

    pygame.draw.rect(screen, BLUE, 
        pygame.Rect(150, 700, 20, 20))  

    pygame.draw.rect(screen, BROWN, 
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

def revenue(saved): 
    font_title = pygame.font.Font(None, 40)   
    font = pygame.font.Font(None, 24) 

    energy_title_text = font_title.render("ENERGY SAVED: ", True, BLACK) 
    energy_text = font.render(str(saved), True, BLACK) 

    energy_title_text_rect = energy_title_text.get_rect() 
    energy_title_text_rect.center = (SCREEN_WIDTH // 4 + SCREEN_WIDTH //2, 700) 


    energy_text_rect = energy_text.get_rect() 
    energy_text_rect.center = (SCREEN_WIDTH - SCREEN_WIDTH // 4, 740) 

    screen.blit(energy_title_text, energy_title_text_rect) 
    screen.blit(energy_text, energy_text_rect) 

# Function to display a simple popup
def display_popup(message):
    popup_width = 300
    popup_height = 200
    popup = pygame.Surface((popup_width, popup_height))
    popup.fill(WHITE)
    pygame.draw.rect(popup, BLACK, (0, 0, popup_width, popup_height), 2)

    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(popup_width//2, popup_height//2))
    popup.blit(text, text_rect)

    # Center the popup on the screen
    popup_rect = popup.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

    # Blit the popup onto the screen
    screen.blit(popup, popup_rect.topleft)

    pygame.display.update()

    # Wait for user response
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def multiplier(type, val) -> int:
    if type == "Windmill":
        return val
    elif type == "SolarPanel":
        return val * energysources.c.sunlight
    else:
        return val

# Main function
def main():
    running = True

    windmillPic = pygame.image.load('windmill.png')
    windmillPic = pygame.transform.scale(windmillPic, (TILE_SIZE, TILE_SIZE)) 
    solarPic = pygame.image.load('solarPanel.png') 
    solarPic = pygame.transform.scale(solarPic, (TILE_SIZE, TILE_SIZE))
    turbinePic = pygame.image.load('turbine.png')
    turbinePic = pygame.transform.scale(turbinePic, (TILE_SIZE, TILE_SIZE))
    

    buy_sell_or_none = "none"
    tile_selected  = (-1,-1)
    energy_source_button_selected = "none"

    current_board = energysources.starting_board_1
    energy_source_num = 0
    current_balance = energysources.balance
    
    font = pygame.font.Font(None, 24) 

    while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    scaled_mouse_pos = ((mouse_pos[0] - BOARD_OFFSET_X) // TILE_SIZE, (mouse_pos[1] - BOARD_OFFSET_Y) // TILE_SIZE)
                    print(mouse_pos)
                    #windmill button 
                    if button_1_location_x <= mouse_pos[0] <= button_1_location_x + button_width and \
                    button_1_location_y <= mouse_pos[1] <= button_1_location_y + button_height:
                        print("windmill Clicked!")  
                        energy_source_button_selected = "Windmill"
                    #turbine button 
                    elif button_1_location_x <= mouse_pos[0] <= button_1_location_x + button_width and \
                    button_2_location_y <= mouse_pos[1] <= button_2_location_y + button_height:
                        print("turbine Clicked!")
                        energy_source_button_selected = "Turbine"
                    #solar panel button 
                    elif button_1_location_x <= mouse_pos[0] <= button_1_location_x + button_width and \
                    button_3_location_y <= mouse_pos[1] <= button_3_location_y + button_height:
                        print("solar panel Clicked!")
                        energy_source_button_selected = "SolarPanel"
                    #buy button 
                    elif button_1_location_x <= mouse_pos[0] <= button_1_location_x + 4/9 * button_width and \
                    button_buy_location_y <= mouse_pos[1] <= button_buy_location_y + button_height:
                        print("buy Clicked!")
                        buy_sell_or_none = "buy"
                    #sell button
                    elif button_sell_location_x <= mouse_pos[0] <= button_sell_location_x + 4/9 * button_width and \
                    button_buy_location_y <= mouse_pos[1] <= button_buy_location_y + button_height:
                        print("sell Clicked!")
                        buy_sell_or_none = "sell"

                    elif buy_sell_or_none == "buy":
                        tile_selected = scaled_mouse_pos
                        # if we have enough money
                        curr_tile = current_board.get_at_location(tile_selected)

                        if curr_tile.terrain == "swamp": #if swamp, skip
                            pass
                        elif curr_tile.terrain == "ocean" and (energy_source_button_selected == "SolarPanel" or energy_source_button_selected == "Windmill"):
                            pass
                        elif curr_tile.terrain == "plateau" and energy_source_button_selected == "Turbine":
                            pass
                        elif energysources.balance - energysources.energy_source_prices[energy_source_button_selected] > 0:
                            # set board at selected tile to le funny 
                            if energy_source_button_selected == "Windmill":
                                
                                curr_tile = current_board.get_at_location(tile_selected)
                                energy_source_num = energy_source_num + 1
                                current_board.set_at_location(energysources.Tile(curr_tile.terrain, energysources.Windmill(str(energy_source_num),
                                energysources.energy_source_prices[energy_source_button_selected],
                                1), windmillPic), tile_selected)
                                print(tile_selected)
                                current_balance = current_balance - energysources.energy_source_prices[energy_source_button_selected]
                                print(current_balance)
                                buy_sell_or_none = "none"
                                energy_source_button_selected = "none"
                                print(current_board.width)
                            elif energy_source_button_selected == "SolarPanel":
                                curr_tile = current_board.get_at_location(tile_selected)
                                energy_source_num = energy_source_num + 1
                                current_board.set_at_location(energysources.Tile(curr_tile.terrain, energysources.SolarPanel(str(energy_source_num),
                                energysources.energy_source_prices[energy_source_button_selected],
                                1), solarPic), tile_selected)
                                current_balance = current_balance - energysources.energy_source_prices[energy_source_button_selected]
                                buy_sell_or_none = "none"
                                energy_source_button_selected = "none"
                            elif energy_source_button_selected == "Turbine":
                                curr_tile = current_board.get_at_location(tile_selected)
                                energy_source_num = energy_source_num + 1
                                current_board.set_at_location(energysources.Tile(curr_tile.terrain, energysources.Turbine(str(energy_source_num),
                                energysources.energy_source_prices[energy_source_button_selected],
                                1), turbinePic), tile_selected)
                                current_balance = current_balance - energysources.energy_source_prices[energy_source_button_selected] 
                                buy_sell_or_none = "none"
                                energy_source_button_selected = "none" 

                            else:
                                pass
                    elif buy_sell_or_none == "sell":
                        tile_selected = scaled_mouse_pos
                        curr_tile = current_board.get_at_location(tile_selected)
                        
                        current_balance = round(current_balance + current_board.get_at_location(tile_selected).energy_source.cost * .7, 2)
                        current_board.set_at_location(energysources.Tile(curr_tile.terrain, None, 0), tile_selected)
                        buy_sell_or_none = "none"
                        energy_source_button_selected = "none"
                            
                    elif 0 <= scaled_mouse_pos[0] <= energysources.starting_board_1.width and 0 <= scaled_mouse_pos[0] <= energysources.starting_board_1.height:
                        tile_selected = scaled_mouse_pos
                        print(tile_selected)
                        
                    else:
                        buy_sell_or_none = "none"
                        tile_selected  = (-1,-1)
                        energy_source_button_selected = "none"
                    draw_climate_balance(energysources.c.sunlight, energysources.c.wind_speed, current_balance) # draw balance


            screen.fill(WHITE)

           
        
            

            outputs = []
            for row in current_board.board:
                
                outputs = outputs + [multiplier(x.energy_source.whatType(),
                    energysources.energy_source_outputs[x.energy_source.whatType()]) for x in row if x.energy_source != None]
            # outputs = [multiplier(x.energy_source.whatType(), x) for x in outputs]
            output_sum = sum(outputs)
            print(output_sum)
            energysources.customer.happiness = output_sum / energysources.customer.annual_kwh

            draw_status_bar(energysources.customer.happiness) # Draw status bar
            
            draw_climate_balance(energysources.c.sunlight, energysources.c.wind_speed, current_balance) # draw balance
            

            draw_board(current_board)  # Draw your starting board
            
            buy_color, sell_color, windmill_color, turbine_color, solarpanel_color = GRAY, GRAY, GRAY, GRAY, GRAY
            if buy_sell_or_none == "buy":
                buy_color = (255, 255, 0)
                sell_color = GRAY
            elif buy_sell_or_none == "sell":
                buy_color = GRAY
                sell_color = (255, 255, 0)
            
            if energy_source_button_selected == "Windmill":
                windmill_color = (255, 255, 0)
            elif energy_source_button_selected == "SolarPanel":
                solarpanel_color = (255, 255, 0)
            elif energy_source_button_selected == "Turbine":
                turbine_color = (255, 255, 0)

              




            draw_button(button_1_location_x, button_buy_location_y ,  5 * button_width // 11, button_height, buy_color, "Buy") # Draw Buy button
            draw_button(button_sell_location_x, button_buy_location_y , 5 * button_width // 11, button_height, sell_color, "Sell") # Draw Sell button
            draw_button(button_1_location_x, button_1_location_y , button_width, button_height, windmill_color, "Windmill") # Draw windmill button
            draw_button(button_1_location_x, button_2_location_y , button_width, button_height, turbine_color, "Turbine") # Draw turbine button
            draw_button(button_1_location_x, button_3_location_y , button_width, button_height, solarpanel_color, "Solar Panel") # Draw Solar Panel button
            
            key()
            
            rev = output_sum * 50000 #rev is not money
            decade_output_sum = [] # stores the amount of energy you have got so far
            decade_output_sum.append(output_sum)
            revenue(sum(decade_output_sum)) # the amount of energy you have collected
            
            
            print(pygame.time.get_ticks())

            if pygame.time.get_ticks()%30000 >= 0 and pygame.time.get_ticks()%30000 <= 50:
                screen.fill(WHITE) 
                # Display popup
                text_surface = font.render("A new year has passed!", True, BLACK)
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)) 

                money_made_text = font.render("Money made: $" + str(rev), True, BLACK)
                money_made_rect = money_made_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+30)) 
                
                screen.blit(text_surface, text_rect)
                screen.blit(money_made_text, money_made_rect) 
                
                pygame.display.flip()
                energysources.c.sunlight = round(random.random(), 2) 
                energysources.c.wind_speed = random.randrange(0,55,1)


                # Wait for a moment
                pygame.time.delay(6000)
                current_balance = current_balance + rev / 1000000
                energysources.customer.annual_kwh = energysources.customer.annual_kwh + (0.25 * energysources.customer.annual_kwh)
            


            pygame.display.flip()
            pygame.display.update()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    #Starting board configuration

    main()