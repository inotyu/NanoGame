import math
import random
import pgzrun
from pygame import Rect

# Game Constants
WIDTH = 800
HEIGHT = 480
TITLE = "NanoVirus Outbreak"
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLAYER_SPEED = 4

# Game States
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"
STATE_VICTORY = "victory"

# Global Variables
game_state = STATE_MENU
sound_enabled = True
score = 0
total_fruits = 0


class Player:
    """Player character - micro robot with sprite animation"""
    
    def __init__(self, x, y):
        self.actor = Actor('player/idle/idle_1')
        self.x = x
        self.y = y
        self.width = self.actor.width
        self.height = self.actor.height
        self.actor.pos = (self.x + self.width // 2, self.y + self.height // 2)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.hp = 3
        self.max_hp = 3
        self.hit_timer = 0
        self.state = "idle"
        self.facing_right = True
        self.animation_frame = 0
        self.animation_timer = 0
        self.idle_frames = 11
        self.run_frames = 12
        self.fall_frames = 1
        self.jump_frames = 5
        self.hit_frames = 5
        
        # Animation images (right-facing)
        self.idle_images_right = [f'player/idle/idle_{i}' for i in range(1, 12)]
        self.run_images_right = [f'player/run/run_{i}' for i in range(1, 13)]
        self.jump_images_right = [f'player/wall_jump/wall_jump{i}_left' for i in range(5, 0, -1)]
        self.fall_image_right = 'player/fall/player_fall'
        self.hit_images_right = [f'player/hit/hit_{i}' for i in range(1, 6)]
        
        # Animation images (left-facing)
        self.idle_images_left = [f'player/idle/idle_{i}_left' for i in range(1, 12)]
        self.run_images_left = [f'player/run/run_{i}_left' for i in range(1, 13)]
        self.jump_images_left = [f'player/wall_jump/wall_jump{i}' for i in range(5, 0, -1)]
        self.fall_image_left = 'player/fall/player_fall_left'
        self.hit_images_left = [f'player/hit/hit_{i}_left' for i in range(1, 6)]
        
    def update(self, platforms):
        """Update player physics and animation"""
        if not self.on_ground:
            self.vel_y += GRAVITY
            
        self.x += self.vel_x
        self.y += self.vel_y
        
        self.on_ground = False
        
        # Ground collision
        if self.y >= HEIGHT - 80:
            self.y = HEIGHT - 80
            self.vel_y = 0
            self.on_ground = True
        
        # Platform collision
        player_rect = self.get_rect()
        
        for platform in platforms:
            if (player_rect.bottom > platform.rect.top and 
                player_rect.top < platform.rect.bottom):
                
                # Landing on platform
                if (self.vel_y >= 0 and
                    player_rect.bottom <= platform.rect.centery and
                    player_rect.bottom > platform.rect.top - 10):
                    
                    if (player_rect.right > platform.rect.left + 5 and
                        player_rect.left < platform.rect.right - 5):
                        
                        self.y = platform.rect.top - self.height + 1
                        self.vel_y = 0
                        self.on_ground = True
                        break
                
                # Hitting bottom of platform
                elif (self.vel_y < 0 and
                      player_rect.top >= platform.rect.bottom - 5 and
                      player_rect.right > platform.rect.left + 10 and
                      player_rect.left < platform.rect.right - 10):
                    
                    self.y = platform.rect.bottom
                    self.vel_y = 0
            
        # Screen boundaries
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width
            
        # Update hit timer
        if self.hit_timer > 0:
            self.hit_timer -= 1
            
        # Update state based on velocity
        if self.state != "hit":
            if not self.on_ground:
                if self.vel_y < -1:
                    self.state = "jump"
                elif self.vel_y > 1:
                    self.state = "fall"
            else:
                if abs(self.vel_x) > 0.1:
                    self.state = "walk"
                else:
                    self.state = "idle"
        
        self.actor.pos = (self.x + self.width // 2, self.y + self.height // 2)
        
        # Update animation
        self.animation_timer += 1
        if self.state == "walk":
            anim_speed = 5
        elif self.state == "jump":
            anim_speed = 3
        elif self.state == "hit":
            anim_speed = 6
        else:
            anim_speed = 4
        
        if self.animation_timer >= anim_speed:
            self.animation_timer = 0
            if self.state == "walk":
                self.animation_frame = (self.animation_frame + 1) % self.run_frames
                if self.facing_right:
                    self.actor.image = self.run_images_right[self.animation_frame]
                else:
                    self.actor.image = self.run_images_left[self.animation_frame]
            elif self.state == "fall":
                self.animation_frame = 0
                if self.facing_right:
                    self.actor.image = self.fall_image_right
                else:
                    self.actor.image = self.fall_image_left
            elif self.state == "jump":
                self.animation_frame = (self.animation_frame + 1) % self.jump_frames
                if self.facing_right:
                    self.actor.image = self.jump_images_right[self.animation_frame]
                else:
                    self.actor.image = self.jump_images_left[self.animation_frame]
            elif self.state == "hit":
                if self.animation_frame < self.hit_frames - 1:
                    self.animation_frame += 1
                else:
                    self.state = "idle"
                    self.animation_frame = 0
                if self.facing_right:
                    self.actor.image = self.hit_images_right[self.animation_frame]
                else:
                    self.actor.image = self.hit_images_left[self.animation_frame]
            else:
                self.animation_frame = (self.animation_frame + 1) % self.idle_frames
                if self.facing_right:
                    self.actor.image = self.idle_images_right[self.animation_frame]
                else:
                    self.actor.image = self.idle_images_left[self.animation_frame]
            
    def move_left(self):
        """Move player left"""
        self.vel_x = -PLAYER_SPEED
        self.facing_right = False
            
    def move_right(self):
        """Move player right"""
        self.vel_x = PLAYER_SPEED
        self.facing_right = True
            
    def stop(self):
        """Stop horizontal movement"""
        self.vel_x = 0
            
    def jump(self):
        """Make player jump"""
        if self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False
            self.state = "jump"
            self.animation_frame = 0
            if sound_enabled:
                try:
                    sounds.jump.play()
                except:
                    pass
                
    def take_damage(self):
        """Player takes damage"""
        if self.hit_timer == 0:
            self.hp -= 1
            self.hit_timer = 60
            self.state = "hit"
            self.animation_frame = 0
            if sound_enabled:
                try:
                    sounds.hit.play()
                except:
                    pass
                
    def get_rect(self):
        """Get player collision rectangle"""
        return Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        """Draw player with hit effect"""
        if self.hit_timer > 0 and (self.hit_timer // 2) % 2 == 0:
            self.actor.draw()
            screen.draw.rect(
                Rect(self.x-2, self.y-2, self.width+4, self.height+4),
                (255, 0, 0)
            )
        else:
            self.actor.draw()


class Virus:
    """Enemy virus with animated movement"""
    
    def __init__(self, x, y, left_bound, right_bound):
        self.x = x
        self.y = y
        # Carrega os frames de animação
        self.idle_frames = [f'virus/corona_idle{i}' for i in range(1, 5)]
        self.hit_frames = [f'virus/corona_hit{i}' for i in range(1, 5)]
        
        self.actor = Actor(self.idle_frames[0])
        self.width = self.actor.width
        self.height = self.actor.height
        self.actor.pos = (self.x + self.width//2, self.y + self.height//2)
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.speed = 1.5
        self.direction = 1
        self.animation_frame = 0
        self.animation_timer = 0
        self.hit_timer = 0
        self.hit = False
        
    def update(self):
        """Atualiza o movimento e animação do vírus"""
        self.x += self.speed * self.direction
        
        if self.x <= self.left_bound or self.x >= self.right_bound:
            self.direction *= -1
            
        # Atualiza a posição
        self.actor.pos = (self.x + self.width//2, self.y + self.height//2)
        
        # Atualiza a animação
        self.animation_timer += 1
        if self.animation_timer >= 8:  # Muda o frame a cada 8 atualizações
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % 4  # 4 frames de animação
            
            # Define qual frame mostrar com base no estado (hit ou idle)
            if self.hit:
                self.actor.image = self.hit_frames[self.animation_frame]
                self.hit_timer += 1
                if self.hit_timer > 10:  # Mostra animação de hit por 10 frames
                    self.hit = False
                    self.hit_timer = 0
            else:
                self.actor.image = self.idle_frames[self.animation_frame]
        
        # Inverte o sprite baseado na direção
        self.actor.flip_x = self.direction < 0
            
    def get_rect(self):
        """Get virus collision rectangle"""
        return Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        """Draw virus with animation"""
        self.actor.draw()


class Fruit:
    """Collectible fruit with floating and rotating animation"""
    
    def __init__(self, x, y, fruit_type='banana'):
        self.x = x
        self.y = y
        self.fruit_type = fruit_type
        self.collected = False
        
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 6
        
        self.images = [f'fruits/banana/banana_{i}' for i in range(1, 5)]
        
        if self.images:
            self.actor = Actor(self.images[0])
            self.width = self.actor.width
            self.height = self.actor.height
            self.actor.pos = (x + self.width//2, y + self.height//2)
        
        self.float_offset = 0
        self.float_speed = 0.1
        self.float_distance = 3
        self.float_phase = random.uniform(0, 6.28)
        
    def update(self):
        """Update fruit animation"""
        if self.collected:
            return
            
        self.float_phase += self.float_speed
        self.float_offset = math.sin(self.float_phase) * self.float_distance
        
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % len(self.images)
        
        if hasattr(self, 'actor'):
            self.actor.y = self.y + self.float_offset
            self.actor.image = self.images[self.animation_frame]
        
    def get_rect(self):
        """Get fruit collision rectangle"""
        hitbox_padding = 4
        return Rect(
            self.x + hitbox_padding, 
            self.y + hitbox_padding + self.float_offset,
            self.width - 2 * hitbox_padding, 
            self.height - 2 * hitbox_padding
        )
        
    def draw(self):
        """Draw fruit with animation"""
        if self.collected:
            return
            
        if hasattr(self, 'actor'):
            self.actor.draw()
        else:
            y_pos = self.y + self.float_offset
            screen.draw.filled_circle(
                (self.x + self.width//2, y_pos + self.height//2), 
                self.width//2, 
                (255, 255, 0)
            )
            screen.draw.filled_rect(
                Rect(
                    self.x + self.width//2 - 2, 
                    y_pos + 2, 
                    4, 
                    8
                ), 
                (139, 69, 19)
            )


class Platform:
    """Platform for player to stand on"""
    
    def __init__(self, x, y, width, height, color="brown"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = Rect(x, y, width, height)
        
        try:
            self.actor = Actor('plataforms/plataform_on')
            self.actor.pos = (x + width//2, y + height//2)
            self.has_image = True
        except:
            self.has_image = False
        
    def draw(self):
        """Draw platform"""
        if hasattr(self, 'actor') and self.actor:
            self.actor.draw()
        else:
            screen.draw.filled_rect(self.rect, self.color)
            screen.draw.rect(self.rect, "black")


class Button:
    """Menu button"""
    
    def __init__(self, x, y, width, height, text):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.hovered = False
        
    def update(self, mouse_pos):
        """Check if button is hovered"""
        self.hovered = self.rect.collidepoint(mouse_pos)
        
    def draw(self):
        """Draw button"""
        color = (80, 80, 100) if self.hovered else (50, 50, 70)
        screen.draw.filled_rect(self.rect, color)
        border_color = "#00ff88" if self.hovered else "#646478"
        screen.draw.rect(self.rect, border_color)
        screen.draw.text(self.text, center=(self.rect.centerx, self.rect.centery), 
                        color="white", fontsize=24)
        
    def is_clicked(self, mouse_pos):
        """Check if button is clicked"""
        return self.rect.collidepoint(mouse_pos)


# Game Objects
player = None
viruses = []
fruits = []
buttons = []
platforms = []


def init_menu():
    """Initialize menu"""
    global buttons
    buttons = [
        Button(WIDTH // 2 - 80, 280, 160, 50, "Start"),
        Button(WIDTH // 2 - 80, 350, 160, 50, "Sound"),
        Button(WIDTH // 2 - 80, 420, 160, 50, "Exit")
    ]


def init_game():
    """Initialize game level"""
    global player, viruses, fruits, score, total_fruits, platforms
    
    player = Player(50, HEIGHT - 300)
    
    platforms = [
        Platform(100, HEIGHT - 150, 100, 20, "brown"),
        Platform(300, HEIGHT - 200, 100, 20, "peru"),
        Platform(500, HEIGHT - 250, 100, 20, "chocolate"),
        Platform(200, HEIGHT - 300, 100, 20, "darkolivegreen"),
        Platform(400, HEIGHT - 350, 100, 20, "brown"),
        Platform(600, HEIGHT - 400, 100, 20, "peru"),
        Platform(150, HEIGHT - 450, 150, 20, "sienna"),
        Platform(400, HEIGHT - 500, 150, 20, "chocolate"),
    ]
    
    # Criando vírus em cima das plataformas
    # Ajustando a posição Y para que fiquem acima das plataformas
    virus_height = 55  # Aumentado para posicionar os vírus mais acima
    viruses = [
        # Vírus na primeira plataforma (y = HEIGHT - 150 - altura do vírus - ajuste fino)
        Virus(150, HEIGHT - 150 - virus_height, 100, 200),  # Plataforma 1
        # Vírus na segunda plataforma
        Virus(350, HEIGHT - 200 - virus_height, 300, 400),  # Plataforma 2
        # Vírus na terceira plataforma
        Virus(550, HEIGHT - 250 - virus_height, 500, 600),  # Plataforma 3
        # Vírus na quarta plataforma
        Virus(250, HEIGHT - 300 - virus_height, 200, 300),  # Plataforma 4
        # Vírus na quinta plataforma
        Virus(450, HEIGHT - 350 - virus_height, 400, 500)   # Plataforma 5
    ]
    
    fruits = [
        Fruit(140, HEIGHT - 80),
        Fruit(340, HEIGHT - 130),
        Fruit(540, HEIGHT - 180),
        Fruit(240, HEIGHT - 230),
        Fruit(440, HEIGHT - 280),
        Fruit(640, HEIGHT - 330),
        Fruit(225, HEIGHT - 380),
        Fruit(475, HEIGHT - 430)
    ]
    
    score = 0
    total_fruits = len(fruits)


def update():
    """Main update function"""
    global game_state, sound_enabled
    
    if game_state == STATE_MENU:
        mouse_pos = (0, 0)
        for button in buttons:
            button.update(mouse_pos)
            
    elif game_state == STATE_PLAYING:
        player.update(platforms)
        
        if keyboard.left:
            player.move_left()
        elif keyboard.right:
            player.move_right()
        else:
            player.stop()
            
        if keyboard.space or keyboard.up:
            player.jump()
            
        for virus in viruses:
            virus.update()
            if player.get_rect().colliderect(virus.get_rect()):
                player.take_damage()
                
        for fruit in fruits:
            if not fruit.collected:
                fruit.update()
                if player.get_rect().colliderect(fruit.get_rect()):
                    fruit.collected = True
                    global score
                    score += 1
                    if sound_enabled:
                        try:
                            sounds.collect.play()
                        except:
                            pass
                        
        if player.hp <= 0:
            game_state = STATE_GAME_OVER
            
        if score >= total_fruits:
            game_state = STATE_VICTORY


def on_music_end():
    """Called when music ends - restart it if sound is enabled"""
    if sound_enabled:
        try:
            music.play('back')
        except:
            pass


def draw():
    """Main draw function"""
    screen.clear()
    
    if game_state == STATE_MENU:
        draw_menu()
    elif game_state == STATE_PLAYING:
        draw_game()
    elif game_state == STATE_GAME_OVER:
        draw_game_over()
    elif game_state == STATE_VICTORY:
        draw_victory()


def draw_menu():
    """Draw menu screen"""
    screen.fill("#1a1a2e")
    
    title = "NanoVirus Outbreak"
    screen.draw.text(title, center=(WIDTH // 2 + 3, 83), color="black", fontsize=60)
    screen.draw.text(title, center=(WIDTH // 2, 80), color="#00ff88", fontsize=60)
    
    screen.draw.text("Escape viruses and collect bananas!", 
                    center=(WIDTH // 2, 160), color="#ffffff", fontsize=28)
    
    screen.draw.line((WIDTH // 2 - 200, 190), (WIDTH // 2 + 200, 190), "#00ff88")
    screen.draw.line((WIDTH // 2 - 200, 192), (WIDTH // 2 + 200, 192), "#00ff88")
    
    screen.draw.text("Use ARROWS to move", center=(WIDTH // 2, 220), 
                    color="#aaaaaa", fontsize=20)
    screen.draw.text("SPACE to jump", center=(WIDTH // 2, 245), 
                    color="#aaaaaa", fontsize=20)
    
    for button in buttons:
        button.draw()
        
    sound_status = "ON" if sound_enabled else "OFF"
    screen.draw.text(f"Sound: {sound_status}", bottomleft=(15, HEIGHT - 15), 
                    color="#00ff88", fontsize=22)


def draw_game():
    """Draw game screen"""
    screen.clear()
    
    # Draw background
    try:
        bg = Actor('other/fundinho')
        bg.pos = (WIDTH // 2, HEIGHT // 2)
        bg.draw()
    except:
        screen.fill("#1a1a2e")
    
    for platform in platforms:
        platform.draw()
    
    for fruit in fruits:
        fruit.draw()
        
    for virus in viruses:
        virus.draw()
        
    player.draw()
    
    screen.draw.text(f"HP: {player.hp}/{player.max_hp}", topleft=(10, 10), 
                    color="white", fontsize=30)
    screen.draw.text(f"Energy: {score}/{total_fruits}", topright=(WIDTH - 10, 10), 
                    color="white", fontsize=30)
    
    for i in range(player.max_hp):
        color = "red" if i < player.hp else "gray"
        screen.draw.filled_circle((30 + i * 40, 50), 12, color)


def draw_game_over():
    """Draw game over screen"""
    screen.fill("black")
    screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 50), 
                    color="red", fontsize=60)
    screen.draw.text("The infection has spread!", center=(WIDTH // 2, HEIGHT // 2 + 20), 
                    color="white", fontsize=30)
    screen.draw.text("Press SPACE to return to menu", 
                    center=(WIDTH // 2, HEIGHT // 2 + 80), color="white", fontsize=25)


def draw_victory():
    """Draw victory screen"""
    screen.fill("darkblue")
    screen.draw.text("VICTORY!", center=(WIDTH // 2, HEIGHT // 2 - 50), 
                    color="yellow", fontsize=60)
    screen.draw.text("All viruses eliminated!", center=(WIDTH // 2, HEIGHT // 2 + 20), 
                    color="white", fontsize=30)
    screen.draw.text(f"Energy collected: {score}/{total_fruits}", 
                    center=(WIDTH // 2, HEIGHT // 2 + 60), color="cyan", fontsize=25)
    screen.draw.text("Press SPACE to return to menu", 
                    center=(WIDTH // 2, HEIGHT // 2 + 100), color="white", fontsize=25)


def on_mouse_down(pos):
    """Handle mouse clicks"""
    global game_state, sound_enabled
    
    if game_state == STATE_MENU:
        if buttons[0].is_clicked(pos):
            game_state = STATE_PLAYING
            init_game()
            # Start music when game starts
            if sound_enabled:
                try:
                    music.play('back')
                except:
                    pass
        elif buttons[1].is_clicked(pos):
            sound_enabled = not sound_enabled
            if sound_enabled:
                try:
                    music.play('back')
                except:
                    pass
            else:
                try:
                    music.stop()
                except:
                    pass
        elif buttons[2].is_clicked(pos):
            exit()


def on_key_down(key):
    """Handle key presses"""
    global game_state
    
    if game_state in [STATE_GAME_OVER, STATE_VICTORY]:
        if key == keys.SPACE:
            game_state = STATE_MENU
            init_menu()


# Start background music at beginning
try:
    music.play('back')
except:
    pass

init_menu()
pgzrun.go()