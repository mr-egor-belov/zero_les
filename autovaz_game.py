import pygame
import random

# Константы
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
CAR_SPEED = 5
SCROLL_SPEED = 5
SCROLL_SPEED_BOOST = 15
CAR_WIDTH = 50
CAR_HEIGHT = 100
MOTORCYCLE_SIZE = (30, 70)
OIL_SPILL_SPEED = 3
BOOST_DURATION = 300  # Frames
LEVEL_UP_SCORE = 1000  # Очки для повышения уровня
MAX_LEVEL = 10
SCORE_BOOST_OIL = 500  # Очки за наезд на масляное пятно

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

# Загрузка изображений
CAR_IMAGE = pygame.image.load("car.png")
CAR_IMAGE = pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT))
OBSTACLE_IMAGE = pygame.image.load("obstacle.png")
OBSTACLE_IMAGE = pygame.transform.scale(OBSTACLE_IMAGE, (CAR_WIDTH, CAR_HEIGHT))
MOTORCYCLE_IMAGE = pygame.image.load("motorcycle.png")
MOTORCYCLE_IMAGE = pygame.transform.scale(MOTORCYCLE_IMAGE, MOTORCYCLE_SIZE)
OIL_SPILL_IMAGE = pygame.image.load("oil_spill.png")
OIL_SPILL_IMAGE = pygame.transform.scale(OIL_SPILL_IMAGE, (CAR_WIDTH, CAR_HEIGHT // 2))

# Класс для машинки игрока
class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CAR_WIDTH, CAR_HEIGHT)
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

    def boost(self):
        global SCROLL_SPEED
        SCROLL_SPEED = SCROLL_SPEED_BOOST  # Увеличение скорости игры
        self.boost_timer = BOOST_DURATION

    def draw(self, surface):
        surface.blit(CAR_IMAGE, self.rect.topleft)

# Абстрактный класс для объектов на дороге
class RoadObject:
    def __init__(self, x, y, width, height, image, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# Класс для управления игрой
class Game:
    def __init__(self):
        self.car = Car(SCREEN_WIDTH // 2 - CAR_WIDTH // 2, SCREEN_HEIGHT - CAR_HEIGHT - 20)
        self.road_objects = []
        self.running = True
        self.score = 0
        self.level = 1
        self.game_over = False
        self.win = False
        self.displayed_score_boost = False
        self.score_boost_timer = 0

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
        self.update_road_objects()

        for road_object in self.road_objects[:]:
            if self.car.rect.colliderect(road_object.rect):
                if road_object.image == OIL_SPILL_IMAGE:
                    self.score += SCORE_BOOST_OIL
                    self.displayed_score_boost = True
                    self.score_boost_timer = 30  # Показываем +500 на 30 кадров
                    self.road_objects.remove(road_object)
                else:
                    self.game_over = True

        self.check_collisions()

        # Повышение уровня каждые 1000 очков
        if self.score // LEVEL_UP_SCORE + 1 > self.level:
            self.level = self.score // LEVEL_UP_SCORE + 1

        if self.score >= LEVEL_UP_SCORE * MAX_LEVEL:
            self.win = True

    def update_road_objects(self):
        for road_object in self.road_objects[:]:
            road_object.move()
            if road_object.rect.top > SCREEN_HEIGHT:
                self.road_objects.remove(road_object)

        if random.randint(1, 50 - self.level) == 1:
            x = random.randint(0, SCREEN_WIDTH - CAR_WIDTH)
            self.road_objects.append(RoadObject(x, -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT, OBSTACLE_IMAGE, random.randint(3, 7)))

        if random.randint(1, 100 - self.level * 5) == 1:
            x = random.randint(0, SCREEN_WIDTH - MOTORCYCLE_SIZE[0])
            self.road_objects.append(RoadObject(x, -MOTORCYCLE_SIZE[1], MOTORCYCLE_SIZE[0], MOTORCYCLE_SIZE[1], MOTORCYCLE_IMAGE, random.randint(6, 10)))

    def check_collisions(self):
        for i, obj1 in enumerate(self.road_objects):
            for j, obj2 in enumerate(self.road_objects):
                if i != j and obj1.rect.colliderect(obj2.rect):
                    # Создание масляного пятна на месте столкновения
                    center_x = (obj1.rect.centerx + obj2.rect.centerx) // 2
                    center_y = (obj1.rect.centery + obj2.rect.centery) // 2
                    self.road_objects.append(RoadObject(center_x - CAR_WIDTH // 2, center_y - CAR_HEIGHT // 4, CAR_WIDTH, CAR_HEIGHT // 2, OIL_SPILL_IMAGE, OIL_SPILL_SPEED))
                    self.road_objects.remove(obj1)
                    self.road_objects.remove(obj2)
                    break

    def draw(self):
        screen.fill(WHITE)
        self.car.draw(screen)
        for road_object in self.road_objects:
            road_object.draw(screen)

        font = pygame.font.SysFont(None, 36)
        level_text = font.render(f"Level: {self.level}", True, BLACK)
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(level_text, (10, 10))
        screen.blit(score_text, (10, 50))

        if self.displayed_score_boost:
            bonus_text = font.render("+500", True, GREEN)
            screen.blit(bonus_text, (self.car.rect.centerx - 20, self.car.rect.top - 30))
            self.score_boost_timer -= 1
            if self.score_boost_timer <= 0:
                self.displayed_score_boost = False

        pygame.display.flip()

    def reset_game(self):
        global SCROLL_SPEED
        SCROLL_SPEED = 5  # Сброс скорости игры
        self.__init__()

# Основной запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()