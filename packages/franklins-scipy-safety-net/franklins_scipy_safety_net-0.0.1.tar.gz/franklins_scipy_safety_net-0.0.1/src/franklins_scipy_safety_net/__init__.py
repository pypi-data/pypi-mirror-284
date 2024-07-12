import random
import time
import threading
from IPython.display import display, HTML
import ipywidgets as widgets


def relax():
    breathe = widgets.Label(
        value="", style=dict(font_family="courier", font_size="20px")
    )

    def work(breathe):
        total = 5000
        for i in range(total):
            breathe.value = "😱 breathe in...."
            time.sleep(1)
            breathe.value = "😮‍💨 breathe out..."
            time.sleep(1)

    thread = threading.Thread(target=work, args=(breathe,))
    display(breathe)
    thread.start()


def panic():
    display(
        HTML(
            '<p style="font-family:courier;font-size:20px">🚨 Unknown command. Did you mean <b>`fssn.PANIC`</b>? 🚨</p>'
        )
    )


def PANIC():
    display(
        HTML(
            '<p style="font-family:courier;font-size:20px">🚨🚨🚨🚨 <font color="red">Unknown command. Did you mean <b>`fssn.PUNic`</b>? 🚨🚨🚨🚨</p>'
        )
    )


puns = [
    "Opti *MyST* - Optimist",
    "Pessi *MyST* - Pessimist",
    "Che *MyST* - Chemist",
    "Alche *MyST* - Alchemist",
    "Opti *MyST* ic - Optimistic",
    "Pessi *MyST* ic - Pessimistic",
    "Re *MyST* - Remissed",
    "Dis *MyST* - Dismissed",
    "Per *MyST* - Permissed",
    "De *MyST* ify - Demystify",
    "*MyST* ake - Mistake",
    "*MyST* y - Misty",
    "*MyST* aken - Mistaken",
    "*MyST* reat - Mistreat",
    "*MyST* rust - Mistrust",
    "*MyST* letoe - Mistletoe",
    "*MyST* ral - Mistral",
    "*MyST* rial - Mistrial",
    "*MyST* ep - Misstep",
    "*MyST* - Missed",
    "*MyST* ery - Mystery",
    "*MyST* ical - Mystical",
    "*MyST* ify - Mystify",
    "*MyST* erious - Mysterious",
    "*MyST* icism - Mysticism",
    "*MyST* ique - Mystique",
]


def PUNic():
    button = widgets.Button(
        description="help", style=dict(font_family="courier", font_size="15px")
    )
    label = widgets.Label(value="", style=dict(font_family="courier", font_size="20px"))

    vb = widgets.VBox([button, label])

    def on_click_update(b):
        label.value = f"💡 {random.choice(puns)}"

    button.on_click(on_click_update)

    display(vb)
