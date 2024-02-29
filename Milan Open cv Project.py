import cv2 as cv
import numpy as np

# Global variable to store the clicked image
clicked_image = None

def on_click(event, x, y, flags, param):
    global clicked_image

    if event == cv.EVENT_LBUTTONDOWN:
        clicked_image = final_image[y:y + final_image.shape[0] // 2, x:x + final_image.shape[1] // 2]
        cv.imshow("Clicked Image", clicked_image)

def process_and_concatenate(image, label, position, font_size, images_stack):
    bgrgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    bgrhsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    brightLAB = cv.cvtColor(image, cv.COLOR_BGR2LAB)

    height, width = image.shape[:2]
    resized_img = cv.resize(image, (width // 5, height // 5))
    resized_gray = cv.resize(bgrgray, (width // 5, height // 5))
    resized_hsv = cv.resize(bgrhsv, (width // 5, height // 5))
    resized_lab = cv.resize(brightLAB, (width // 5, height // 5))

    resized_gray_3d = cv.cvtColor(resized_gray, cv.COLOR_GRAY2BGR)

    horizontal_stack = np.hstack((resized_img, resized_gray_3d, resized_hsv, resized_lab))

    cv.putText(horizontal_stack, label, position, cv.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 255), 1, cv.LINE_AA)
    cv.putText(horizontal_stack, 'Original', (10, 30), cv.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 255), 1, cv.LINE_AA)
    cv.putText(horizontal_stack, 'Gray', (width // 5 + 10, 30), cv.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 255), 1, cv.LINE_AA)
    cv.putText(horizontal_stack, 'HSV', (2 * width // 5 + 10, 30), cv.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 255), 1, cv.LINE_AA)
    cv.putText(horizontal_stack, 'LAB', (3 * width // 5 + 10, 30), cv.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 255), 1, cv.LINE_AA)

    images_stack.append(horizontal_stack)

def show_introduction():
    # Create a black image for the introduction
    black_intro = np.zeros((600, 800, 3), dtype=np.uint8)

    # Add the group information to the introduction text
    intro_text1 = "Welcome to our Color Space Project!"
    intro_text2 = "Group by:\nNicko Lander R. Milan"

    # Calculate the position to center the text
    text_size1 = cv.getTextSize(intro_text1, cv.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    text_x1 = (black_intro.shape[1] - text_size1[0]) // 2
    text_y1 = 100

    text_size2 = cv.getTextSize(intro_text2, cv.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
    text_x2 = (black_intro.shape[1] - text_size2[0]) // 2
    text_y2 = text_y1 + text_size1[1] + 30

    cv.putText(black_intro, intro_text1, (text_x1, text_y1), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
    cv.putText(black_intro, intro_text2, (text_x2, text_y2), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv.LINE_AA)

    # Display the introduction in the console
    print(intro_text1)
    print(intro_text2)
    print()

    # Create a window to display the introduction text
    cv.namedWindow("Introduction", cv.WINDOW_NORMAL)
    cv.imshow("Introduction", black_intro)
    cv.resizeWindow("Introduction", window_width, window_height)
    cv.waitKey(3000)  # Wait for 3 seconds (3000 milliseconds)
    cv.destroyWindow("Introduction")


# Read the images
Nickoimg = cv.imread("C:/Users/nicko/Downloads/mypic.jpg")
Nickoimg = cv.imread("C:/Users/nicko/Downloads/mypic.jpg")

Nickoimg = cv.resize(Nickoimg, (Nickoimg.shape[1], Nickoimg.shape[0]))

# Create an empty list to store concatenated images
images_stack = []

# Process and concatenate the first image
process_and_concatenate(Nickoimg, 'Original', (10, 30), 0.5, images_stack)

# Process and concatenate the second image
process_and_concatenate(Nickoimg, 'Other', (4 * Nickoimg.shape[1] // 5 + 10, 30), 0.5, images_stack)

# Concatenate all images in the images_stack vertically
final_image = np.vstack(images_stack)

# Calculate the aspect ratio of the final image
aspect_ratio = final_image.shape[1] / final_image.shape[0]

# Set the fixed window height
window_height = 600

# Calculate the corresponding window width
window_width = int(window_height * aspect_ratio)

# Show the introduction
show_introduction()

# Create a window to display the images
cv.namedWindow("Image Conversions", cv.WINDOW_NORMAL)

# Display the concatenated image in the window
cv.imshow("Image Conversions", final_image)

# Set the mouse callback function
cv.setMouseCallback("Image Conversions", on_click)

# Resize the window to the desired dimensions
cv.resizeWindow("Image Conversions", window_width, window_height)

# Wait for a key event and close the window
cv.waitKey(0)
cv.destroyAllWindows()
f
