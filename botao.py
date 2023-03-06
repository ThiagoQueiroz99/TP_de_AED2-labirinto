import pygame

class Botao(pygame.Rect):
    def __init__(self, x, y, lar, alt, cor, tex):
        super().__init__(x, y, lar, alt)
        self.x = x
        self.y = y
        self.lar = lar
        self.alt = alt
        self.cor = cor
        self.tex = tex
        self.font = pygame.font.Font(None, 30)

    def cria(self, surface):
        pygame.draw.rect(surface, self.cor, self)
        text_surface = self.font.render(self.tex, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.center)
        surface.blit(text_surface, text_rect)

    def click(self, mouse_pos,mouse_click): # Verifica se o botão foi clickado
        if mouse_click[0] == 1 and self.x < mouse_pos[0] < self.x + self.lar and self.y < mouse_pos[1] < self.y + self.alt:
           return True
        else:
            return False