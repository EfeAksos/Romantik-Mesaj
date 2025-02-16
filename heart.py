import pygame
import random

# Pygame'i başlat
pygame.init()

# Renkler
dark_pink = (230, 0, 115)
light_pink = (255, 204, 204)
white = (255, 255, 255)
black = (0, 0, 0)

# Ekran ayarları
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Romantik Mesaj")

# Fontlar
font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 40)

# Mesaj listesi
messages = [
    "Sen benim için en güzel rüyasın... 🌙",
    "Kalbim sadece senin için atıyor... ❤️",
    "Gülüşün güneşi kıskandırıyor... ☀️",
    "Dünyadaki en değerli hazine sensin... 💎",
    "Seninle her an bir masal gibi... 📖",
    "Sonsuza kadar seninle olmak istiyorum... 💞"
]
current_message = "Sana Özel Bir Mesaj! 💖"

# Buton ayarları
button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50)

def draw_screen():
    screen.fill(light_pink)
    text_surface = big_font.render(current_message, True, dark_pink)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    screen.blit(text_surface, text_rect)
    
    pygame.draw.rect(screen, dark_pink, button_rect, border_radius=15)
    button_text = font.render("Yeni Mesaj", True, white)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)
    
    pygame.display.flip()

running = True
while running:
    draw_screen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            current_message = random.choice(messages)

pygame.quit()
