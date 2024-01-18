# Lab Assignment 1: Caesar Cipher
#Software Security, Winter 2024
import tkinter as tk
from tkinter import ttk
import pyperclip

def caesar_cipher():
    message = entry_message.get()
    key = int(entry_key.get())
    mode = combo_mode.get()

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    result_text.set(translated)
    pyperclip.copy(translated)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Message Label and Entry
ttk.Label(frame, text="Message:").grid(row=0, column=0, sticky=tk.W)
entry_message = ttk.Entry(frame, width=40)
entry_message.grid(row=0, column=1, columnspan=2, sticky=tk.W)

# Key Label and Entry
ttk.Label(frame, text="Key:").grid(row=1, column=0, sticky=tk.W)
entry_key = ttk.Entry(frame, width=5)
entry_key.grid(row=1, column=1, sticky=tk.W)

# Mode Label and Combobox
ttk.Label(frame, text="Mode:").grid(row=1, column=2, sticky=tk.W)
combo_mode = ttk.Combobox(frame, values=["encrypt", "decrypt"], state="readonly")
combo_mode.set("encrypt")
combo_mode.grid(row=1, column=3, sticky=tk.W)

# Translate Button
translate_button = ttk.Button(frame, text="Translate", command=caesar_cipher)
translate_button.grid(row=2, column=0, columnspan=4, pady=(10, 0))

ttk.Label(frame, text="Result:").grid(row=3, column=0, columnspan=4, sticky=tk.W)
result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text, wraplength=400, justify="left")
result_label.grid(row=4, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))

root.mainloop()
