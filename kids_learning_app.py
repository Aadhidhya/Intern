# kids_learning_app.py
# AI-based Kids Learning App: Alphabets & Animals

import ipywidgets as widgets
from IPython.display import display, clear_output, Audio, Image as IPyImage
from gtts import gTTS

alphabets = [
    {
        "sentence": f"{chr(65+i)} for {word}.",
        "image": img
    }
    for i, (word, img) in enumerate([
        ("Apple", "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg"),
        ("Ball", "https://upload.wikimedia.org/wikipedia/commons/7/7a/Basketball.png"),
        ("Cat", "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"),
        ("Dog", "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"),
        ("Elephant", "https://upload.wikimedia.org/wikipedia/commons/6/63/African_elephant_warning_raised_trunk.jpg"),
        ("Fish", "https://upload.wikimedia.org/wikipedia/commons/1/17/Clownfish_in_the_Andaman_Coral_Reef.jpg"),
        ("Grapes", "https://upload.wikimedia.org/wikipedia/commons/1/11/Table_grapes_on_white.jpg"),
        ("Hen", "https://upload.wikimedia.org/wikipedia/commons/8/84/Hen.jpg"),
        ("Ice cream", "https://upload.wikimedia.org/wikipedia/commons/6/6a/Ice_cream_cone.jpg"),
        ("Jug", "https://upload.wikimedia.org/wikipedia/commons/3/3f/Jug.jpg"),
        ("Kite", "https://upload.wikimedia.org/wikipedia/commons/4/4c/Kite.jpg"),
        ("Lion", "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg"),
        ("Mango", "https://upload.wikimedia.org/wikipedia/commons/9/90/Hapus_Mango.jpg"),
        ("Nest", "https://upload.wikimedia.org/wikipedia/commons/6/6b/Bird_nest.jpg"),
        ("Orange", "https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg"),
        ("Parrot", "https://upload.wikimedia.org/wikipedia/commons/2/2f/Amazona_aestiva_-Brazil-8.jpg"),
        ("Queen", "https://upload.wikimedia.org/wikipedia/commons/3/32/Queen_Elizabeth_II_March_2015.jpg"),
        ("Rabbit", "https://upload.wikimedia.org/wikipedia/commons/7/70/Rabbit_in_montana.jpg"),
        ("Sun", "https://upload.wikimedia.org/wikipedia/commons/c/c3/Solar_sys8.jpg"),
        ("Tiger", "https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg"),
        ("Umbrella", "https://upload.wikimedia.org/wikipedia/commons/8/89/Umbrella.jpg"),
        ("Van", "https://upload.wikimedia.org/wikipedia/commons/0/0b/Van.jpg"),
        ("Watch", "https://upload.wikimedia.org/wikipedia/commons/8/87/Wristwatch.jpg"),
        ("Xylophone", "https://upload.wikimedia.org/wikipedia/commons/7/7e/Xylophone.jpg"),
        ("Yak", "https://upload.wikimedia.org/wikipedia/commons/b/b2/Yak_in_Sikkim.jpg"),
        ("Zebra", "https://upload.wikimedia.org/wikipedia/commons/0/0f/Plains_Zebra_Equus_quagga.jpg")
    ])
]

animals = [
    {"sentence": "I am a dog. I bark.", "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"},
    {"sentence": "I am a cat. I meow.", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"},
    {"sentence": "I am a cow. I moo.", "image": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Holstein_Friesian_cow.jpg"},
    {"sentence": "I am a lion. I roar.", "image": "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg"},
    {"sentence": "I am an elephant. I trumpet.", "image": "https://upload.wikimedia.org/wikipedia/commons/6/63/African_elephant_warning_raised_trunk.jpg"}
]

current_data = []
index = 0

title = widgets.HTML("<h1>🧒 Learn Alphabets & Animals 🧒</h1>")
text_label = widgets.HTML("<h3></h3>")
next_button = widgets.Button(description="Next ➡️", button_style="success")

btn_alpha = widgets.Button(description="📘 Learn Alphabets", button_style="info")
btn_animal = widgets.Button(description="🐾 Learn Animals", button_style="warning")

def play_item():
    clear_output(wait=True)
    display(title)
    item = current_data[index]
    display(IPyImage(url=item["image"], width=450))
    text_label.value = f"<h3>{item['sentence']}</h3>"
    display(text_label, next_button)
    tts = gTTS(item["sentence"])
    audio_file = f"audio_{index}.mp3"
    tts.save(audio_file)
    display(Audio(audio_file, autoplay=True))

def next_item(b):
    global index
    index = (index + 1) % len(current_data)
    play_item()

def choose_alphabet(b):
    global current_data, index
    current_data = alphabets
    index = 0
    play_item()

def choose_animal(b):
    global current_data, index
    current_data = animals
    index = 0
    play_item()

next_button.on_click(next_item)
btn_alpha.on_click(choose_alphabet)
btn_animal.on_click(choose_animal)

display(title, btn_alpha, btn_animal)
