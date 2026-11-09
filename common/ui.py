import pygame
from common.colors import white
from common.constants import width, height

_font = None

def get_font(size=30):
    global _font
    if _font is None or _font.get_height() != size:
        _font = pygame.font.SysFont("calibri", size)
    return _font

def draw_score(screen, score, font=None):
    """Renderiza 'Pontos: X' no canto superior direito."""
    pass

def draw_paused(screen, font=None):
    """Renderiza 'PAUSADO' no centro da tela."""
    f = font or get_font()
    msg = f.render("PAUSADO", True, white)
    rect = msg.get_rect(center=(width // 2, height // 2))
    screen.blit(msg, rect)

def draw_start_msg(screen, font=None):
    """Renderiza mensagem de início centralizada."""
    f = font or get_font()
    msg = f.render("Pressione qualquer tecla para iniciar", True, white)
    rect = msg.get_rect(center=(width // 2, 180))
    screen.blit(msg, rect)