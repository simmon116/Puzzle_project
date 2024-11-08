import pygame
import random

# Configuración de pantalla y colores
WIDTH, HEIGHT = 400, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Rompecabezas")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PIECE_COLOR = (0, 255, 0)

# Configuración de pieza
PIECE_SIZE = 20
piece_x, piece_y = WIDTH // 2, 0

# Inicialización de Pygame
pygame.init()
clock = pygame.time.Clock()

def draw_piece(x, y):
    """Función para dibujar la pieza en pantalla."""
    pygame.draw.rect(SCREEN, PIECE_COLOR, (x, y, PIECE_SIZE, PIECE_SIZE))

def move_piece():
    """Función que controla el movimiento de la pieza."""
    global piece_y
    piece_y += PIECE_SIZE

# Ciclo principal del juego
running = True
while running:
    SCREEN.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movimiento horizontal con teclas
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                piece_x -= PIECE_SIZE
            elif event.key == pygame.K_RIGHT:
                piece_x += PIECE_SIZE

    move_piece()  # Caída de la pieza
    draw_piece(piece_x, piece_y)  # Dibuja la pieza en su nueva posición
    
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
