# 👤 Skin Tone Detection & Shirt Color Recommendation 🎨

This Python project uses OpenCV to detect a user's skin tone from an image or live webcam feed and suggests suitable shirt colors based on their detected tone.

## 📌 Features

- Detect skin tone from:
  - 📷 Image file
  - 📹 Live webcam feed
- Classify skin tone as:
  - Fair
  - Medium
  - Deep
- Recommend shirt colors based on the detected tone 🎽
- Simple command-line interface

## 🧠 Skin Tone Classification Logic

Skin tone is estimated based on the average brightness (value channel) in the HSV color space:
- **V < 60** → Deep
- **60 ≤ V ≤ 180** → Medium
- **V > 180** → Fair

## 🎨 Shirt Color Recommendations

| Skin Tone | Recommended Shirt Colors |
|-----------|---------------------------|
| Deep      | White, Light Blue, Olive Green, Burgundy, Mustard Yellow, Deep Purple |
| Medium    | Teal, Rich Green, Orange, Warm Grey, Royal Blue, Maroon |
| Fair      | Navy Blue, Deep Green, Charcoal Grey, Burgundy, Earthy Tones |

## 🛠️ Installation

```bash
pip install opencv-python numpy
