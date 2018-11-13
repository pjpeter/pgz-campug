WIDTH = 1024
HEIGHT = 384

cow = Actor('cow')
cow.pos = (100, 0)

def draw():
    screen.fill((100, 170, 240))
    cow.draw()

def update():
    if keyboard[keys.UP]:
        if cow.y > 200:
            cow.y -= 10
    elif cow.y < 320:
        cow.y += 3
    if keyboard[keys.LEFT] and cow.left > 0:
        cow.x -= 2
    if keyboard[keys.RIGHT] and cow.right < WIDTH:
        cow.x += 2
    