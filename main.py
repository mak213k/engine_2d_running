import pygame
import random

# Inicialização
pygame.init()

# Tamanho da janela
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quadrado Runner")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
RED = (220, 20, 60)

# Relógio e fonte
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Jogador (quadrado)
player = pygame.Rect(100, HEIGHT - 60, 40, 40)
velocity_y = 0
gravity = 1
jump_force = -18
is_jumping = False

speed = 5
acceleration = 0.5
max_speed = 12
min_speed = 3

# Obstáculos
obstacles = []
obstacle_timer = 0
obstacle_interval = 1500  # em milissegundos

# Função para criar um obstáculo
def create_obstacle():
    return pygame.Rect(WIDTH, HEIGHT - 60, 40, 40)

# Pontuação
score = 0

# Loop principal
running = True
while running:
    dt = clock.tick(60)  # Delta time para controlar obstáculos
    win.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        speed = min(speed + acceleration, max_speed)
    else:
        speed = max(speed - acceleration, min_speed)

    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = jump_force
        is_jumping = True

    # Atualiza o jogador (pulo)
    player.y += velocity_y
    velocity_y += gravity

    if player.y >= HEIGHT - 60:
        player.y = HEIGHT - 60
        is_jumping = False

    # Criação de obstáculos
    obstacle_timer += dt
    if obstacle_timer >= obstacle_interval:
        obstacles.append(create_obstacle())
        obstacle_timer = 0

    # Movimenta e desenha obstáculos
    for obstacle in obstacles[:]:
        obstacle.x -= int(speed)
        pygame.draw.rect(win, RED, obstacle)

        # Colisão
        if player.colliderect(obstacle):
            print("💥 GAME OVER! Pontuação:", score)
            running = False

        # Remove obstáculos que saíram da tela
        if obstacle.right < 0:
            obstacles.remove(obstacle)
            score += 1

    # Desenha o jogador
    pygame.draw.rect(win, BLUE, player)

    # Linha do chão
    pygame.draw.line(win, BLACK, (0, HEIGHT - 20), (WIDTH, HEIGHT - 20), 2)

    # Pontuação
    score_text = font.render(f"Pontos: {score}", True, BLACK)
    win.blit(score_text, (10, 10))
     
    # Atualiza a tela
    pygame.display.update()       

pygame.quit()
