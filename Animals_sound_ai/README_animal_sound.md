# Animal Sound Generator using Generative AI

This project generates **animal sounds from text input** using **Generative AI**.  
The user enters an animal sound description (e.g., *dog barking*), and the system generates and plays the sound in real time.

---

## 📌 Project Description
The Animal Sound Generator uses a **text-to-audio generative model** to synthesize animal sounds.  
Unlike traditional systems that play pre-recorded audio files, this project **generates new sounds using AI**.

---

## 📂 Project Files
- `animal_sound_generator.py` – Main Python program  
- `README.md` – Project documentation  
- `animal_sound.wav` – Generated sound file (created after execution)

---

## 🛠️ Requirements
- Python 3.9 or above  
- Google Colab (recommended) or local system with GPU  

### Required Libraries
```
transformers
torch
soundfile
scipy
numpy
```

---

## ▶️ How to Run (Google Colab)

1. Upload `animal_sound_generator.py` to Google Colab  
2. Install dependencies:
```python
!pip install transformers torch soundfile scipy numpy
```
3. Run the program:
```python
!python animal_sound_generator.py
```
4. Enter an animal sound prompt when asked.

---

## ✍️ Sample Input
```
dog barking
cat meowing
lion roaring
```

---

## 🔊 Output
- AI-generated animal sound  
- Sound plays immediately in Google Colab  
- Saved as `animal_sound.wav`  

---

## 🧠 How It Works
1. Takes text input describing an animal sound  
2. Uses a pretrained generative audio model  
3. Generates audio waveform  
4. Saves and plays the generated sound  

---

## 🎓 Viva / Exam Explanation
> This project uses a generative audio model to convert text prompts into animal sounds. The system generates audio dynamically rather than using stored sound files.

---

## ⭐ Conclusion
This project demonstrates the application of **Generative AI in audio synthesis**, specifically for generating animal sounds from text input.

