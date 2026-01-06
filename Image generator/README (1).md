# Random Image Generator (Generative AI)

This project generates images from text prompts using **Generative AI** with the **Stable Diffusion** model.

## 📌 Project Description
The user enters a text prompt, and the system generates a corresponding image using a pre-trained Stable Diffusion model.  
The generated image is saved locally and can be displayed in Google Colab or Python environments.

---

## 📂 Project Files
- `random_image_generator.py` – Main Python program
- `README.md` – Project documentation
- `output.png` – Generated image (created after running the code)

---

## 🛠️ Requirements
- Python 3.9 or above
- Google Colab (recommended) or local system with GPU

### Required Libraries
```
diffusers
transformers
torch
accelerate
```

---

## ▶️ How to Run (Google Colab)

1. Upload `random_image_generator.py` to Google Colab  
2. Install dependencies:
```python
!pip install diffusers transformers torch accelerate
```
3. Run the program:
```python
!python random_image_generator.py
```
4. Enter a text prompt when asked.

---

## ✍️ Sample Input
```
A cat sitting on a chair, cartoon style
```

---

## 🖼️ Output
- An AI-generated image
- Saved as `output.png`

---

## 🧠 How It Works
1. Loads a pre-trained Stable Diffusion model
2. Takes text input from the user
3. Generates an image using Generative AI
4. Saves and displays the image

---

## 🎓 Viva / Exam Explanation
> This project uses a generative diffusion model to convert text input into images. The model was pre-trained on large image datasets, allowing image generation without training from scratch.

---

## ⭐ Conclusion
This project demonstrates the practical use of Generative AI for text-to-image generation using modern deep learning models.

