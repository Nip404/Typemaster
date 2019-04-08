import pygame
import random

pygame.init()
s = [800,200]
font = pygame.font.SysFont("Garamond MS",s[0]//20)
screen = pygame.display.set_mode(s,0,32)

with open("words.txt","r+") as f:
    words = [i.split(" ")[0] for i in f.read().split("\n") if not i[0] == "-"]

class WordQueue:
    def __init__(self,words,amount):
        self.words = words
        self.queue = [self._new() for _ in range(amount)]

    @property
    def current(self):
        return self.queue[0]

    def _new(self):
        return random.choice(self.words)

    def generateNext(self):
        self.queue = self.queue[1:] + [self._new()]

def main():
    while True:
        queue = WordQueue(words,2)
        user = ""
        
        while True:      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if user == queue.current:
                            queue.generateNext()
                            user = ""
                        else:
                            user += " "
                    elif event.key == pygame.K_BACKSPACE:
                        if len(user):
                            user = user[:-1]
                    elif 97 <= event.key <= 122:
                        user += chr(event.key)

                    print(user,queue.current)
                    
            tmpg = ""
            for i in range(len(user)):
                if len(user) > len(queue.current) or not user[i] == queue.current[i]:
                    break
                tmpg += user[i]
                
            green = font.render(tmpg,True,(0,255,0))
            red = font.render("".join(" ".join(queue.queue)[i+len(tmpg)] for i in range(len(user)-len(tmpg))),True,(255,0,0))
            black = font.render(" ".join(queue.queue)[len(user):],True,(0,0,0))
            usertxt = font.render(user,True,(0,0,0))
            
            screen.fill((255,255,255))
            screen.blit(green,green.get_rect(center=[(s[0]/2)-((green.get_width()+red.get_width()+black.get_width())/2)+(green.get_width()/2),s[1]/3]))
            screen.blit(red,red.get_rect(center=[(s[0]/2)-((green.get_width()+red.get_width()+black.get_width())/2)+green.get_width()+(red.get_width()/2),s[1]/3]))
            screen.blit(black,black.get_rect(center=[(s[0]/2)+((green.get_width()+red.get_width()+black.get_width())/2)-(black.get_width()/2),s[1]/3]))
            screen.blit(usertxt,usertxt.get_rect(center=[s[0]/2,s[1]*(2/3)]))

            pygame.display.flip()

if __name__ == "__main__":
    main()
