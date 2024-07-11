# Pygame Util
A package that simplifies repetitive pygame code.

## Window

Here's how you would do it in pygame:
```
window = pygame.display.set_mode((600, 400))
window.set_caption("example caption")
window.set_icon(example_icon)

background_color = (255, 255, 255)

clock = pygame.time.Clock()
fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(fps)
    window.fill(background_color)

    # render the images you want to show on the screen

    pygame.display.flip()
```


Here's how you would do it in pygame_util:
```
window = Window((600, 400), icon=icon, caption="example_caption", force_quit=True)

while True:
    # render images you want to show on the screen
    window.update()
```
## Text

## Images

## Colors

## Timers

## Positioning


