import cv2
import numpy as np

photo = np.full((256, 512, 3), (200, 210, 220), np.uint8)
cv2.circle(photo, (256, 150), 80, (40, 40, 200), -1)
cv2.ellipse(photo, (300, 58), (30, 14), -30, 0, 360, (60, 170, 60), -1)
cv2.rectangle(photo, (420, 30), (500, 110), (150, 110, 70), -1)

clicks = [(256, 150, 1), (460, 60, 0)]

guesses = np.full((3, 256, 256), -4.0, np.float32)
cv2.ellipse(guesses[0], (128, 150), (40, 80), 0, 0, 360, 4.0, -1)
cv2.ellipse(guesses[1], (128, 150), (10, 20), 0, 0, 360, 4.0, -1)
cv2.ellipse(guesses[2], (128, 150), (40, 80), 0, 0, 360, 4.0, -1)
cv2.ellipse(guesses[2], (150, 58), (15, 14), -30, 0, 360, 4.0, -1)

print("Photo", photo.shape, "guesses", guesses.shape)


# ---------- PART 1: clicks to prompts ----------
print("\nPART 1: Prompts for SAM")

# Extract x and y coordinates and scale them
points = np.array(
    [[x * 2, y * 2] for x, y, label in clicks],
    dtype=np.float32
)

# Extract labels
labels = np.array(
    [label for x, y, label in clicks],
    dtype=np.int64
)

print("Points:", points.tolist())
print("Labels:", labels.tolist())

# Add two dimensions for SAM
points = points[None, None]
labels = labels[None, None]

print("Points shape:", points.shape)
print("Labels shape:", labels.shape)


# ---------- PART 2: sort the guesses ----------
print("\nPART 2: Part, bigger, whole")

# Count positive values in each guess
sizes = [np.sum(guess > 0) for guess in guesses]
# Sort guesses from smallest to biggest
ordered = sorted(
    guesses,
    key=lambda guess: np.sum(guess > 0)
)
# Print the sizes in sorted order
print("Sizes:", [np.sum(guess > 0) for guess in ordered])


# ---------- PART 3: the whole apple, photo-sized ----------
print("\nPART 3: Mask")
# Select the biggest guess
biggest = ordered[-1]
# Resize to original photo dimensions
resized = cv2.resize(
    biggest,
    (photo.shape[1], photo.shape[0])
)

# Convert into binary mask
mask = (resized > 0).astype(np.uint8)
print("Mask shape:", mask.shape)
print("Pixels covered:", np.sum(mask))


# ---------- PART 4: the sticker ----------
print("\nPART 4: Sticker")
# Find bounding box
x, y, w, h = cv2.boundingRect(mask)
# Create alpha channel
alpha = (mask * 255).astype(np.uint8)
# Blur alpha channel using 3 x 3 kernel
alpha = cv2.blur(alpha, (3, 3))
# Stack photo and alpha channel
rgba = np.dstack((photo, alpha))
# Crop sticker using bounding box
sticker = rgba[y:y+h, x:x+w]

# Print information
print("Box:", (x, y, w, h))
print("Sticker shape:", sticker.shape)
print("Alpha middle:", sticker[h//2, w//2, 3])
print("Alpha top-left:", sticker[0, 0, 3])

# Save sticker
cv2.imwrite("sticker.png", sticker)
print("Sticker saved successfully!")
