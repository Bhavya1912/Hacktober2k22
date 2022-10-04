import pygame, math

pygame.init()

window_height = 350
window_width = 350
window  = pygame.display.set_mode((window_height,window_width))

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False

    def draw(self,window,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                    
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
                
        if self.text != '':
            font = pygame.font.SysFont('OpenSans-Regular', 60)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):            
            if not self.over:
                # beepsound.play()
                self.over = True
        else:
            self.over = False
                    
white = (255,255,255)
# the numbers for the calcaltor
n_1s = button((200,199,205),10,270,40,40, '1')
n_2s = button((200,199,205),80,270,40,40, '2')
n_3s = button((200,199,205),140,270,40,40, '3')
n_4s = button((200,199,205),10,200,40,40, '4')
n_5s = button((200,199,205),80,200,40,40, '5')
n_6s = button((200,199,205),140,200,40,40, '6')
n_7s = button((200,199,205),10,130,40,40, '7')
n_8s = button((200,199,205),80,130,40,40, '8')
n_9s = button((200,199,205),140,130,40,40, '9')
n_0s = button((200,199,205),200,130,40,40, '0')

numbers = [n_1s,n_2s,n_3s,n_4s,n_5s,n_6s,n_7s,n_8s,n_9s,n_0s]

# the symbols!
o_1s = button((200,199,205),260,270,40,40, '+')
o_2s = button((200,199,205),260,200,40,40, '-')
o_3s = button((200,199,205),260,130,40,40, 'x')
o_4s = button((200,199,205),200,200,40,40, '÷')
o_5s = button((200,199,205),200,270,40,40, '=')
o_6s = button((200,199,205),260,500,40,40, 'C')

symbols = [o_1s,o_2s,o_3s,o_4s,o_5s,o_6s]


# redraw window
def redraw(inputtap):
    # draw all the numbers
    for button in numbers:
        button.draw(window)

    # the symbols
    for button in symbols:
        button.draw(window)

    inputtap.draw(window)

def Symbols():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        try:
            if is_finished or user_input[-1] in ["+", "-", "x", "÷", "="]:
                # User shouldn't type two symbols continuously
                # User shouldn't input any symbols when game finished because there is no number
                return
        except IndexError:
            # User shouldn't input any symbols if there is no number
            return


        if o_1s.isOver(pos):
            print("+")
            user_input += "+"
            python_input += "+"

        if o_2s.isOver(pos):
            print("-")
            user_input += "-"
            python_input += "-"

        if o_3s.isOver(pos):
            print("x")
            user_input += "x"
            python_input += "*"

        if o_4s.isOver(pos):
            print("÷")
            user_input += "÷"
            python_input += "/"

        if o_5s.isOver(pos):
            print("=")
            result = eval(python_input)
            python_input = ""
            user_input += f"={result:.2f}"
            is_finished = True

        if o_6s.isOver(pos):
            print("C")
            python_input = ""
            user_input = ""

def MOUSEOVERnumbers():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        if is_finished:
            user_input = ""
            python_input = ""
            is_finished = False
        pos = pygame.mouse.get_pos()          
        if n_1s.isOver(pos):
            print("1")
            user_input += "1"
            python_input += "1"
        if n_2s.isOver(pos):
            print("2")
            user_input += "2"
            python_input += "2"
        if n_3s.isOver(pos):
            print("3")
            user_input += "3"
            python_input += "3"
        if n_4s.isOver(pos):
            print("4")
            user_input += "4"
            python_input += "4"
        if n_5s.isOver(pos):
            print("5")
            user_input += "5"
            python_input += "5"
        if n_6s.isOver(pos):
            print("6")
            user_input += "6"
            python_input += "6"
        if n_7s.isOver(pos):
            print("7")
            user_input += "7"
            python_input += "7"
        if n_8s.isOver(pos):
            print("8")
            user_input += "8"
            python_input += "8"
        if n_9s.isOver(pos):
            print("9")
            user_input += "9"
            python_input += "9"
        if n_0s.isOver(pos):
            print("0")
            user_input += "0"
            python_input += "0"

# the main loop
run = True
user_input = ""
python_input = ""
is_finished = True

while run:
    # input tap
    inputtap = button((152,162,158),10,50,350,60,f"{user_input}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        MOUSEOVERnumbers()

        Symbols()

    redraw(inputtap)
    pygame.display.update()

pygame.quit()