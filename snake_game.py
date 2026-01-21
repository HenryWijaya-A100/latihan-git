import pygame, random, sys
from enum import Enum

pygame.init()
W, H, GS = 800, 600, 20
COLORS = {BLACK: (0,0,0), WHITE: (255,255,255), RED: (255,0,0), GREEN: (0,255,0), YEL: (255,255,0), CYN: (0,255,255)}

class Dir(Enum):
    UP = (0, -1); DOWN = (0, 1); LEFT = (-1, 0); RIGHT = (1, 0)

class Game:
    def __init__(self):
        self.scr = pygame.display.set_mode((W, H))
        pygame.display.set_caption("🐍 GAME ULAR")
        self.clk = pygame.time.Clock()
        self.fnt, self.sfnt = pygame.font.Font(None, 36), pygame.font.Font(None, 24)
        self.prev_len, self.eat_t, self.mil_t = 3, 0, 0
        self.reset()
        
    def reset(self):
        sx, sy = W // 40, H // 40
        self.s = [(sx, sy), (sx-1, sy), (sx-2, sy)]
        self.d = self.nd = Dir.RIGHT
        self.f = self.rnd()
        self.sc, self.dead, self.msg, self.mil = 0, False, "", 0
        
    def rnd(self):
        while True:
            x, y = random.randint(0, W//GS-1), random.randint(0, H//GS-1)
            if (x, y) not in self.s: return (x, y)
    
    def inp(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return 0
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and self.d != Dir.DOWN: self.nd = Dir.UP
                elif e.key == pygame.K_DOWN and self.d != Dir.UP: self.nd = Dir.DOWN
                elif e.key == pygame.K_LEFT and self.d != Dir.RIGHT: self.nd = Dir.LEFT
                elif e.key == pygame.K_RIGHT and self.d != Dir.LEFT: self.nd = Dir.RIGHT
                elif e.key == pygame.K_SPACE and self.dead: self.reset()
                elif e.key == pygame.K_ESCAPE: return 0
        return 1
    
    def upd(self):
        if self.dead: return
        self.d = self.nd
        hx, hy = self.s[0]
        dx, dy = self.d.value
        nh = (hx+dx, hy+dy)
        
        if nh[0]<0 or nh[0]>=W//GS or nh[1]<0 or nh[1]>=H//GS:
            self.dead, self.msg = True, "Dinding! 😭"
            return
        if nh in self.s: self.dead, self.msg = True, "Tubuh! 😭"
        
        self.s.insert(0, nh)
        if nh == self.f:
            self.sc += 10
            self.eat_t = pygame.time.get_ticks()
            if self.sc // 1000000 > self.mil:
                self.mil = self.sc // 1000000
                self.sc += 100000
                self.mil_t = pygame.time.get_ticks()
            self.f = self.rnd()
        else: self.s.pop()
    
    def draw(self):
        self.scr.fill(COLORS[BLACK])
        fx, fy = self.f[0]*GS, self.f[1]*GS
        pygame.draw.rect(self.scr, COLORS[RED], (fx, fy, GS, GS))
        pygame.draw.circle(self.scr, COLORS[YEL], (fx+GS//2, fy+GS//2), GS//4)
        
        for i, (sx, sy) in enumerate(self.s):
            x, y = sx*GS, sy*GS
            c = COLORS[GREEN] if i==0 else (0, 200, 0)
            pygame.draw.rect(self.scr, c, (x, y, GS, GS))
            pygame.draw.rect(self.scr, COLORS[WHITE], (x, y, GS, GS), 2 if i==0 else 1)
        
        if pygame.time.get_ticks()-self.eat_t<300:
            self.scr.blit(self.fnt.render("😊", 1, COLORS[WHITE]), (W//2-20, H//2-20))
        
        if len(self.s) > self.prev_len:
            self.scr.blit(self.fnt.render("😄", 1, COLORS[GREEN]), (W//2+50, 20))
            self.prev_len = len(self.s)
        
        if pygame.time.get_ticks()-self.mil_t<2000:
            self.scr.blit(self.fnt.render(f"🎁 +{self.mil}JT!", 1, COLORS[YEL]), (W//2-80, 60))
        
        tx = self.fnt.render(f"S:{self.sc} L:{len(self.s)}", 1, COLORS[WHITE])
        self.scr.blit(tx, (10, 10))
        
        if self.dead:
            o = pygame.Surface((W, H))
            o.set_alpha(200)
            o.fill(COLORS[BLACK])
            self.scr.blit(o, (0, 0))
            for t, y in [(self.fnt.render("GAME OVER 😭", 1, COLORS[RED]), H//2-80),
                         (self.fnt.render(self.msg, 1, COLORS[YEL]), H//2-20),
                         (self.sfnt.render(f"S:{self.sc}|L:{len(self.s)}", 1, COLORS[WHITE]), H//2+30),
                         (self.sfnt.render("SPACE: Main Ulang | ESC: Keluar", 1, COLORS[CYN]), H//2+80)]:
                self.scr.blit(t, (W//2-t.get_width()//2, y))
        
        pygame.display.flip()
    
    def run(self):
        while self.inp():
            self.upd()
            self.draw()
            self.clk.tick(10)
        pygame.quit()

if __name__ == "__main__": Game().run()
