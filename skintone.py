import cv2
import numpy as np

def classify_skin_tone(h, s, v):
    """
    Classifies skin tone based on HSV values.
    """
    if v < 60:
        return "Deep"
    elif v > 180:
        return "Fair"
    else:
        return "Medium"

def recommend_shirt_colors(skin_tone):
    """
    Suggests the best shirt colors based on skin tone.
    """
    recommendations = {
        "Deep": ["White", "Light Blue", "Olive Green", "Burgundy", "Mustard Yellow", "Deep Purple"],
        "Medium": ["Teal", "Rich Green", "Orange", "Warm Grey", "Royal Blue", "Maroon"],
        "Fair": ["Navy Blue", "Deep Green", "Charcoal Grey", "Burgundy", "Earthy Tones"]
    }
    return recommendations.get(skin_tone, ["No recommendation available"])

def detect_skin_tone(frame):
    """
    Detects and classifies the skin tone in an image.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define skin color range in HSV
    lower_skin = np.array([0, 20, 50], dtype=np.uint8)
    upper_skin = np.array([50, 255, 255], dtype=np.uint8)

    # Create a skin mask
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Extract skin pixels
    skin_pixels = hsv[mask > 0]

    if len(skin_pixels) == 0:
        return "No skin detected", []

    # Compute average skin tone
    avg_hsv = np.mean(skin_pixels, axis=0)

    non_zero_y = skin_pixels[:, 2]
    if len(non_zero_y) > 0:
        average_brightness = np.mean(non_zero_y)
        if average_brightness > 150:
            skin_tone = "Fair"
        elif 100 <= average_brightness <= 150:
            skin_tone = "Medium"
        else:
            skin_tone = "Deep"
    else:
        skin_tone = "No skin detected"

    # Recommend shirt colors
    shirt_colors = recommend_shirt_colors(skin_tone)

    return skin_tone, shirt_colors

print("Choose an option:")
print("1. Detect skin and tone in an image")
print("2. Detect skin and tone in live video")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    image_path = input("Enter the image file path: ")
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
    else:
        skin_tone, shirt_colors = detect_skin_tone(image)
        print(f"\nYour skin tone is *{skin_tone}*")
        print("The best suitable colors are:")
        for color in shirt_colors:
            print(f"✅ {color}")
        cv2.imshow("Selected Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

elif choice == 2:
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture and detect skin tone...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to access the webcam.")
            break

        # Flip frame for better user experience
        frame = cv2.flip(frame, 1)
        cv2.imshow("Press 'Q' to Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            skin_tone, shirt_colors = detect_skin_tone(frame)
            print(f"\nYour skin tone is *{skin_tone}*")
            print("The best suitable colors are:")
            for color in shirt_colors:
                print(f"✅ {color}")
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    print("Invalid choice! Please enter 1 or 2.")

# import cv2
# import numpy as np

# def classify_skin_tone(h, s, v):
#     """
#     Classifies skin tone based on HSV values.
#     """
#     if v < 50:
#         return "Deep"
#     elif v > 200:
#         return "Fair"
#     else:
#         return "Medium"

# def recommend_shirt_colors(skin_tone):
#     """
#     Suggests the best shirt colors based on skin tone.
#     """
#     recommendations = {
#         "Deep": ["White", "Light Blue", "Olive Green", "Burgundy", "Mustard Yellow", "Deep Purple"],
#         "Medium": ["Teal", "Rich Green", "Orange", "Warm Grey", "Royal Blue", "Maroon"],
#         "Fair": ["Navy Blue", "Deep Green", "Charcoal Grey", "Burgundy", "Earthy Tones"]
#     }
#     return recommendations.get(skin_tone, ["No recommendation available"])

# def detect_skin_tone(frame):
#     """
#     Detects and classifies the skin tone in a video frame.
#     """
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Define skin color range in HSV
#     lower_skin = np.array([0, 20, 50], dtype=np.uint8)
#     upper_skin = np.array([50, 255, 255], dtype=np.uint8)

#     # Create a skin mask
#     mask = cv2.inRange(hsv, lower_skin, upper_skin)

#     # Extract skin pixels
#     skin_pixels = hsv[mask > 0]

#     if len(skin_pixels) == 0:
#         return "No skin detected", []

#     # Compute average skin tone
#     avg_hsv = np.mean(skin_pixels, axis=0)

#     # Classify skin tone
#     skin_tone = classify_skin_tone(avg_hsv[0], avg_hsv[1], avg_hsv[2])

#     # Recommend shirt colors
#     shirt_colors = recommend_shirt_colors(skin_tone)

#     return skin_tone, shirt_colors

# # Open webcam
# cap = cv2.VideoCapture(0)

# print("Press 'q' to capture and detect skin tone...")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Unable to access the webcam.")
#         break

#     # Flip frame for better user experience
#     frame = cv2.flip(frame, 1)

#     # Show a basic live feed
#     cv2.imshow("Press 'Q' to Capture", frame)

#     # Press 'q' to capture and process skin tone
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         skin_tone, shirt_colors = detect_skin_tone(frame)
#         print(f"\nYour skin tone is *{skin_tone}*")
#         print("The best suitable colors are:")
#         for color in shirt_colors:
#             print(f"✅ {color}")
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()