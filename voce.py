import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen resolution
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

images = list()

numOfApple = 10
numOfBanana = 4
numOfKiwi = 3


# Set the maximum width and height of the images
max_width = 80

# Load images and scale
# image arrray [image, coordinates, name, inBasket]
for i in range(numOfApple):
    image = pygame.image.load("./image1.png")
    image = pygame.transform.scale(image, (max_width, int(max_width * image.get_height() / image.get_width())))
    images.append([image, (0, 0), "apple", False])
for i in range(numOfBanana):
    image = pygame.image.load("./image2.png")
    image = pygame.transform.scale(image, (max_width, int(max_width * image.get_height() / image.get_width())))
    images.append([image, (0, 0), "banana", False])
for i in range(numOfKiwi):
    image = pygame.image.load("./image3.png")
    image = pygame.transform.scale(image, (max_width, int(max_width * image.get_height() / image.get_width())))
    images.append([image, (0, 0), "kiwi", False])

# Find max height
max_height = 0
for image in images:
    if image[0].get_height() > max_height:
        max_height = image[0].get_height()

# Load and scale basket images
baksetImage1 = pygame.image.load("./basket.png")
baksetImage1 = pygame.transform.scale(baksetImage1, (150, int(150 * baksetImage1.get_height() / baksetImage1.get_width())))
baksetImage2 = pygame.image.load("./basket.png")
baksetImage2 = pygame.transform.scale(baksetImage2, (150, int(150 * baksetImage2.get_height() / baksetImage2.get_width())))
baksetImage3 = pygame.image.load("./basket.png")
baksetImage3 = pygame.transform.scale(baksetImage3, (150, int(150 * baksetImage3.get_height() / baksetImage3.get_width())))

basketsPositions = [(150, 80), (400, 80), (650, 80)]
screen.blit(baksetImage1, basketsPositions[0])
screen.blit(baksetImage2, basketsPositions[1])
screen.blit(baksetImage3, basketsPositions[2])

# Set the font and text to be displayed
font = pygame.font.Font(None, 50)
jabukeText = "Jabuke"
bananeText = "Banane"
kiwiText = "Kiwi"
# Render the text as an image
jabukeImage = font.render(jabukeText, True, (178,34,34))
bananeImage = font.render(bananeText, True, (253, 218, 13))
kiwiImage = font.render(kiwiText, True, (147, 197, 114))
newGameImage = font.render("Nova igra", True, (193, 150, 161))


# Generate ranodm positions of the fruits, but no overlapping
positions = []
for i in range(len(images)):
    # Generate a random position
    x = random.randint(0, SCREEN_WIDTH - max_width)
    y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT - max_height)
    position = (x, y)

    overlap = True
    while overlap:
        # Check if the position is unique
        overlapCounter = 0
        for otherPosition in positions:
            positionRect = pygame.Rect((position[0], position[1]), (max_width, max_height))
            otherPositionRect = pygame.Rect((otherPosition[0], otherPosition[1]), (max_width, max_height))

            if positionRect.colliderect(otherPositionRect):
                # Generate a new random position if it is not unique
                x = random.randint(0, SCREEN_WIDTH - max_width)
                y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT - max_height)
                position = (x, y)
                overlapCounter += 1

        if overlapCounter > 0:
            print(overlapCounter)
            overlap = True
        else:
            overlap = False

    # Add the unique position to the list
    positions.append(position)

print(positions)

for i in range(len(positions)):
    images[i][1] = positions[i]
    screen.blit(images[i][0], images[i][1])

# Update the display
pygame.display.flip()

def gameInit():
    global appleCnt, bananaCnt, kiwiCnt, running, gameCompleted, imagesCnt, ticks, numOfKiwi, numOfBanana, numOfApple, images, positions, jabukeImage, kiwiImage, bananeImage

    # Random number of fruits
    numOfBanana  = random.randint(3, 8)
    numOfApple  = random.randint(3, 8)
    numOfKiwi  = random.randint(3, 8)

    images = list()

    # Load images and scale
    # image arrray [image, coordinates, name, inBasket]
    for i in range(numOfApple):
        image = pygame.image.load("image1.png")
        image = pygame.transform.scale(image, (max_width, int(max_width * image.get_height() / image.get_width())))
        images.append([image, (0, 0), "apple", False])
    for i in range(numOfBanana):
        image = pygame.image.load("image2.png")
        image = pygame.transform.scale(image, (max_width, int(max_width * image.get_height() / image.get_width())))
        images.append([image, (0, 0), "banana", False])
    for i in range(numOfKiwi):
        image = pygame.image.load("image3.png")
        image = pygame.transform.scale(image, (max_width, int(max_width * image.get_height() / image.get_width())))
        images.append([image, (0, 0), "kiwi", False])

    # Generate ranodm positions of the fruits, but no overlapping
    positions = []
    for i in range(len(images)):
        # Generate a random position
        x = random.randint(0, SCREEN_WIDTH - max_width)
        y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT - max_height)
        position = (x, y)

        overlap = True
        while overlap:
            # Check if the position is unique
            overlapCounter = 0
            for otherPosition in positions:
                positionRect = pygame.Rect((position[0], position[1]), (max_width, max_height))
                otherPositionRect = pygame.Rect((otherPosition[0], otherPosition[1]), (max_width, max_height))

                if positionRect.colliderect(otherPositionRect):
                    # Generate a new random position if it is not unique
                    x = random.randint(0, SCREEN_WIDTH - max_width)
                    y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT - max_height)
                    position = (x, y)
                    overlapCounter += 1

            if overlapCounter > 0:
                print(overlapCounter)
                overlap = True
            else:
                overlap = False

        # Add the unique position to the list
        positions.append(position)

    print(positions)

    for i in range(len(positions)):
        images[i][1] = positions[i]
        screen.blit(images[i][0], images[i][1])

    jabukeImage = font.render("Jabuke 0", True, (178, 34, 34))
    bananeImage = font.render("Banane 0", True, (253, 218, 13))
    kiwiImage = font.render("Kiwi 0", True, (147, 197, 114))
    pygame.display.flip()

    appleCnt = 0
    bananaCnt = 0
    kiwiCnt = 0
    running = True
    gameCompleted = False
    imagesCnt = len(images)
    ticks = 0


appleCnt = 0
bananaCnt = 0
kiwiCnt = 0
running = True
gameCompleted = False
imagesCnt = len(images)
ticks = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouseX, mouseY = pygame.mouse.get_pos()

    # Check if the mouse is over any of the images
    imagePickedUp = False
    for i, image in enumerate(images):
        x, y = image[1]
        if mouseX > x and mouseX < x + max_width and mouseY > y and mouseY < y + max_height and image[3] == False:
            imagePickedUp = True
            # Scale the image up and follow the mouse
            image[0] = pygame.transform.scale(image[0], (int(max_width * 1.35), int(max_height * 1.35)))
            x, y = mouseX - max_width / 2, mouseY - max_height / 2
            image[1] = (x, y)

            if image[2] == "apple" and imagePickedUp == True:
                basketRect = pygame.Rect((basketsPositions[0][0], basketsPositions[0][1]), (baksetImage1.get_width(), baksetImage1.get_height()))
                if basketRect.collidepoint(mouseX, mouseY):
                    appleCnt += 1
                    imagePickedUp = False
                    image[1] = (basketsPositions[0][0] + appleCnt*10, basketsPositions[0][1] + 50)
                    image[3] = True
                    image[0] = pygame.transform.scale(image[0], (int(max_width * 0.9), int(max_height * 0.9)))
                    jabukeText = "Jabuke " + str(appleCnt)
                    jabukeImage = font.render(jabukeText, True, (178, 34, 34))

            elif image[2] == "kiwi" and imagePickedUp == True:
                basketRect = pygame.Rect((basketsPositions[1][0], basketsPositions[1][1]),
                                         (baksetImage1.get_width(), baksetImage1.get_height()))
                if basketRect.collidepoint(mouseX, mouseY):
                    bananaCnt += 1
                    imagePickedUp = False
                    image[1] = (basketsPositions[1][0] + bananaCnt * 10, basketsPositions[1][1]+ 50)
                    image[3] = True
                    image[0] = pygame.transform.scale(image[0], (int(max_width * 0.9), int(max_height * 0.9)))
                    bananeText = "Banane " + str(bananaCnt)
                    bananeImage = font.render(bananeText, True, (253, 218, 13))


            elif image[2] == "banana" and imagePickedUp == True:
                basketRect = pygame.Rect((basketsPositions[2][0], basketsPositions[2][1]),
                                         (baksetImage1.get_width(), baksetImage1.get_height()))
                if basketRect.collidepoint(mouseX, mouseY):
                    kiwiCnt += 1
                    imagePickedUp = False
                    image[1] = (basketsPositions[2][0] + kiwiCnt * 10, basketsPositions[2][1]+ 50)
                    image[3] = True
                    image[0] = pygame.transform.scale(image[0], (int(max_width * 0.9), int(max_height * 0.9)))
                    kiwiText = "Kiwi " + str(kiwiCnt)
                    kiwiImage = font.render(kiwiText, True, (147, 197, 114))

    cnt = 0
    for image in images:
        if image[3] == True:
            cnt += 1

    if cnt == imagesCnt:
        gameCompleted = True

    # Redraw the imaages
    screen.fill((255, 255, 255))
    for i in range(len(positions)):
        screen.blit(images[i][0], images[i][1])
    screen.blit(baksetImage1, basketsPositions[0])
    screen.blit(baksetImage2, basketsPositions[1])
    screen.blit(baksetImage3, basketsPositions[2])
    screen.blit(jabukeImage, (170, 35))
    screen.blit(bananeImage, (420, 35))
    screen.blit(kiwiImage, (670, 35))

    # Draw new game button
    if gameCompleted:
        button_rect = pygame.Rect(400, 600, 200, 50)
        pygame.draw.rect(screen, (193, 150, 161), button_rect)
        screen.blit(newGameImage, (425, 550))

    # Reinit the game
    if mouseX > 400 and mouseX < 400 + 200 and mouseY > 600 and mouseY < 600 + 50 and gameCompleted == True:
        ticks += 1
        if ticks == 500:
            gameInit()

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()