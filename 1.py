import tkinter as tk
import random
import string


MIN_AVERAGE = 10
MAX_AVERAGE = 15
KEY_LENGTHS = [5, 4, 4]


def get_weight(char):
    if char.isdigit():
        return int(char) + 27  # Цифры 0-9 получают вес 27-36
    return ord(char) - ord('A') + 1  # Буквы A-Z получают вес 1-26


def generate_block(length):
    while True:
        block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        avg_weight = sum(get_weight(c) for c in block) / length
        if MIN_AVERAGE <= avg_weight <= MAX_AVERAGE:
            return block


def generate_key():
    return '-'.join(generate_block(length) for length in KEY_LENGTHS)


def init_gui():
    root = tk.Tk()
    root.title("Keygen with Background")
    root.geometry("900x500")
    return root


def init_canvas(root):
    bg_image = tk.PhotoImage(file="lphub40o5g4a11.png")
    canvas = tk.Canvas(root, width=900, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.bg_image = bg_image
    return canvas


def display_key(canvas, text):
    global lbl_key
    if 'lbl_key' in globals() and lbl_key.winfo_exists():
        lbl_key.config(text=text)
    else:
        lbl_key = tk.Label(
            canvas,
            text=text,
            font=("Arial", 14),
            background='#92c2f2')
        canvas.create_window(450, 200, window=lbl_key)


def init_input(canvas):
    btn_generate = tk.Button(canvas, text='Generate Key', font=("Arial", 12), command=lambda: display_key(canvas, generate_key()))
    canvas.create_window(450, 250, window=btn_generate)


if __name__ == '__main__':
    root = init_gui()
    canvas = init_canvas(root)
    init_input(canvas)
    root.mainloop()
