import pygame
import time

# Constants
GRID_SIZE = 5
CELL_SIZE = 100
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)

# Game Objects
HEALTH_CENTER = (2, 0)  # 🏥
PREGNANT_MOTHER = (4, 4)  # 👩‍🍼
OBSTACLES = [(1, 1), (1, 3), (2, 2), (3, 3)]  # 🚧

def draw_grid(screen, agent_pos):
    screen.fill(WHITE)
    
    # Draw Grid
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)
    
    # Draw Obstacles
    for (ox, oy) in OBSTACLES:
        pygame.draw.rect(screen, GRAY, (ox * CELL_SIZE, oy * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw Health Center (Start Position)
    pygame.draw.rect(screen, GREEN, (HEALTH_CENTER[0] * CELL_SIZE, HEALTH_CENTER[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw Pregnant Mother (Goal)
    pygame.draw.rect(screen, RED, (PREGNANT_MOTHER[0] * CELL_SIZE, PREGNANT_MOTHER[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw Agent (CHW/Drone)
    pygame.draw.circle(screen, BLUE, (agent_pos[0] * CELL_SIZE + CELL_SIZE // 2, agent_pos[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
    
    pygame.display.flip()

def animate_agent(path):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maternal Health Delivery Simulation")
    
    for position in path:
        draw_grid(screen, position)
        time.sleep(0.5)  # Delay for animation
    
    pygame.quit()

# Example of a path for testing (Agent moving from Health Center to Mother avoiding obstacles)
if __name__ == "__main__":
    sample_path = [(2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4)]
    animate_agent(sample_path)
