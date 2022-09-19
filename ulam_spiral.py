import pygame
import os

pygame.init()

RED = (241, 48, 48)
JET = (57, 57, 58)

os.system('color 70')

def get_factors(num):
    all_factors = []
    for i in range(2, round(num / 2)):
        if num % i == 0:
            all_factors.append(i)
            break
    return all_factors

# find primes
all_primes = [2] # add 2 to list of primes manually
max = int(input('Enter the maximum value of prime number\n>>'))
for i in range(3, max, 2): # step by 2 removes all even integers
    i_factors = get_factors(i)
    if len(i_factors) == 0:
        all_primes.append(i)
        print(f'Finding Primes | {round(100 * all_primes[-1] / max)}%')

running = True

# find all coordinates
all_coords = []

# set start position to screen center
x = pygame.display.Info().current_w / 2
y = pygame.display.Info().current_h / 2
ORIGIN = [x, y]
dot_dimensions = 1
step = dot_dimensions * 2 # distance between dots
direction = 'right'
turn = False
turn_distance = 1
num_of_turns = 0
spiral_pos = 0

# find spiral coordinates for all integers < max
for i in range(1, all_primes[-1] + 1):
    all_coords.append((x, y))
    print(f'Finding coordinates for all integers less than or equal to {max} | {round(100 * (i / all_primes[-1]))}%')
    # handle change in coords
    if direction == 'right':
        x += step
        spiral_pos += 1
    elif direction == 'down':
        y += step
        spiral_pos += 1
    elif direction == 'left':
        x -= step
        spiral_pos += 1
    elif direction == 'up':
        y -= step
        spiral_pos += 1
    if spiral_pos == turn_distance: # handle when to turn
        turn = True
    if turn: # handle change in direction
        if direction == 'right':
            direction = 'up'
            num_of_turns += 1
        elif direction == 'down':
            direction = 'right'
            num_of_turns += 1
        elif direction == 'left':
            direction = 'down'
            num_of_turns += 1
        elif direction == 'up':
            direction = 'left'
            num_of_turns += 1
        spiral_pos = 0
        turn = False
    if num_of_turns == 2: # handle when to increase side length
        turn_distance += 1
        num_of_turns = 0

# find prime coordinates on spiral
prime_coords = []
for i in range(len(all_primes)):
    prime_coords.append(all_coords[all_primes[i] - 1])
    print(f'Finding coordinates for prime numbers | {round(100 * (i / len(all_primes)))}%')

# open pygame window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # full screen for users
pygame.display.set_caption("Ulam Spiral")

# drawing functions and vars

def drawDots():
    screen.fill(JET)
    print('drawing dots')
    for dot in range(len(prime_coords)):
        pygame.draw.circle(screen, RED, prime_coords[dot], dot_dimensions)
        screen.blit(numOfPrimesText, numOfPrimesTextRect)
        screen.blit(highestPrimeText, highestPrimeTextRect)
        pygame.display.flip()

def drawLines():
    screen.fill(JET)
    print('drawing lines')
    for line in range(2, len(prime_coords)):
        pygame.draw.line(screen, RED, prime_coords[line - 1], prime_coords[line])
        screen.blit(numOfPrimesText, numOfPrimesTextRect)
        screen.blit(highestPrimeText, highestPrimeTextRect)
        pygame.display.flip()

font = pygame.font.Font('StoehrNumbers.ttf', 42)
numOfPrimesText = font.render(f'Number of primes: {len(all_primes)}', True, JET, (246, 232, 234))
numOfPrimesTextRect = numOfPrimesText.get_rect()
numOfPrimesTextRect_h = numOfPrimesTextRect.height
numOfPrimesTextRect.center = (pygame.display.Info().current_w / 2, pygame.display.Info().current_h - numOfPrimesTextRect_h / 2) # horizontally and vertically centered

highestPrimeText = font.render(f'Highest prime found: {all_primes[-1]}', True, JET, (246, 232, 234))
highestPrimeTextRect = highestPrimeText.get_rect()
highestPrimeTextRect_h = highestPrimeTextRect.height
highestPrimeTextRect.center = (pygame.display.Info().current_w / 2, pygame.display.Info().current_h - highestPrimeTextRect_h / 2 - numOfPrimesTextRect_h) # horizontally and vertically centered with compensation for num of primes text

drawing_dots = True
drawing_lines = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                drawing_lines = True
            if event.key == pygame.K_q:
                drawing_dots = True
    pygame.display.flip()
    while drawing_lines:
        drawLines()
        drawing_lines = False
    while drawing_dots:
        drawDots()
        drawing_dots = False

pygame.quit()
