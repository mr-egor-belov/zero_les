# VAZAUTO GAME
# игра на выживание с постоянным передвижением,
# где на поле постоянно появляются “враги”,
# которых нельзя касаться

import pygame
import random

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CAR_SPEED = 5
SCROLL_SPEED = 5
OBSTACLE_SIZE = 50
MOTORCYCLE_SIZE = (30, 70)
OIL_SPILL_SPEED = 3
OIL_SPEED_BOOST = 15
BOOST_DURATION = 300  # Frames
SCROLL_SPEED_BOOST = 15

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Arcade")
clock = pygame.time.Clock()

# Класс для машинки игрока
class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 100)
        self.speed = CAR_SPEED
        self.boost_timer = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

        # Уменьшаем таймер ускорения, если он активен
        if self.boost_timer > 0:
            self.boost_timer -= 1
            if self.boost_timer == 0:
                global SCROLL_SPEED
                SCROLL_SPEED = 5  # Сброс скорости игры
                game.background_color = WHITE  # Сброс цвета фона

    def boost(self):
        global SCROLL_SPEED
        SCROLL_SPEED = SCROLL_SPEED_BOOST  # Увеличение скорости игры
        self.boost_timer = BOOST_DURATION

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

# Класс для препятствий
class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
        self.speed = random.randint(3, 7)

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

# Класс для мотоциклов
class Motorcycle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, *MOTORCYCLE_SIZE)
        self.speed = random.randint(6, 10)

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, self.rect)

# Класс для масляного пятна
class OilSpill:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE // 2)

    def move(self):
        self.rect.y += OIL_SPILL_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)

# Класс для управления игрой
class Game:
    def __init__(self):
        self.car = Car(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 120)
        self.obstacles = []
        self.motorcycles = []
        self.oil_spills = []
        self.running = True
        self.score = 0
        self.level = 1
        self.game_over = False
        self.background_color = WHITE
        self.win = False

    def show_start_screen(self):
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 72)
        title_text = font.render("VAZAUTO", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))

        font = pygame.font.SysFont(None, 36)
        start_text = font.render("Press SPACE to Start", True, BLACK)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def show_game_over_screen(self):
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Your Score: {self.score}", True, BLACK)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

        restart_text = font.render("Press SPACE to Restart", True, BLACK)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.reset_game()
                    waiting = False

    def show_win_screen(self):
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 72)
        win_text = font.render("YOU WIN", True, GREEN)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 3))

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Your Score: {self.score}", True, BLACK)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

        restart_text = font.render("Press SPACE to Restart", True, BLACK)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.reset_game()
                    waiting = False

    def run(self):
        self.show_start_screen()
        while self.running:
            self.handle_events()
            if self.win:
                self.show_win_screen()
            elif not self.game_over:
                self.update()
                self.draw()
            else:
                self.show_game_over_screen()
            clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.car.move()
        self.update_obstacles()
        self.update_motorcycles()
        self.update_oil_spills()

        for obstacle in self.obstacles[:]:
            if self.car.rect.colliderect(obstacle.rect):
                self.game_over = True

        for motorcycle in self.motorcycles[:]:
            if self.car.rect.colliderect(motorcycle.rect):
                self.game_over = True

        self.check_collisions()
        self.score += 1

        if self.score // 2000 + 1 > self.level:
            self.level = self.score // 2000 + 1

        if self.level >= 10:
            self.win = True

    def update_obstacles(self):
        for obstacle in self.obstacles[:]:
            obstacle.move()
            if obstacle.rect.top > SCREEN_HEIGHT:
                self.obstacles.remove(obstacle)

        if random.randint(1, 50) == 1:
            x = random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE)
            self.obstacles.append(Obstacle(x, -OBSTACLE_SIZE))

    def update_motorcycles(self):
        for motorcycle in self.motorcycles[:]:
            motorcycle.move()
            if motorcycle.rect.top > SCREEN_HEIGHT:
                self.motorcycles.remove(motorcycle)

        if random.randint(1, 100) == 1:
            x = random.randint(0, SCREEN_WIDTH - MOTORCYCLE_SIZE[0])
            self.motorcycles.append(Motorcycle(x, -MOTORCYCLE_SIZE[1]))

    def update_oil_spills(self):
        for oil_spill in self.oil_spills[:]:
            oil_spill.move()
            if oil_spill.rect.top > SCREEN_HEIGHT:
                self.oil_spills.remove(oil_spill)
            if self.car.rect.colliderect(oil_spill.rect):
                self.car.boost()
                self.background_color = GRAY  # Меняем фон на серый при наезде на пятно
                self.oil_spills.remove(oil_spill)

    def check_collisions(self):
        for obstacle in self.obstacles[:]:
            for motorcycle in self.motorcycles[:]:
                if obstacle.rect.colliderect(motorcycle.rect):
                    self.create_oil_spill(obstacle.rect.center)
                    self.obstacles.remove(obstacle)
                    self.motorcycles.remove(motorcycle)

        for i, obstacle in enumerate(self.obstacles):
            for other_obstacle in self.obstacles[i + 1:]:
                if obstacle.rect.colliderect(other_obstacle.rect):
                    self.create_oil_spill(obstacle.rect.center)
                    self.obstacles.remove(obstacle)
                    self.obstacles.remove(other_obstacle)
                    break

    def create_oil_spill(self, position):
        x, y = position
        self.oil_spills.append(OilSpill(x - OBSTACLE_SIZE // 2, y - OBSTACLE_SIZE // 4))

    def draw(self):
        screen.fill(self.background_color)  # Используем изменяемый фон
        self.car.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for motorcycle in self.motorcycles:
            motorcycle.draw(screen)
        for oil_spill in self.oil_spills:
            oil_spill.draw(screen)

        font = pygame.font.SysFont(None, 36)
        level_text = font.render(f"Level: {self.level}", True, BLACK)
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(level_text, (10, 10))
        screen.blit(score_text, (10, 50))

        pygame.display.flip()

    def reset_game(self):
        global SCROLL_SPEED
        SCROLL_SPEED = 5  # Сброс скорости игры
        self.background_color = WHITE  # Сброс цвета фона
        self.__init__()

# Основной запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
