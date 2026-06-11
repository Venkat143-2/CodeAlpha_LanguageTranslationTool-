import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "Odia": "or",
    "Assamese": "as",
    "Sanskrit": "sa",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Polish": "pl",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Malay": "ms",
    "Filipino": "tl",
    "Greek": "el",
    "Hebrew": "iw",
    "Persian": "fa",
    "Ukrainian": "uk",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Czech": "cs",
    "Slovak": "sk",
    "Bulgarian": "bg",
    "Croatian": "hr",
    "Serbian": "sr",
    "Slovenian": "sl",
    "Danish": "da",
    "Swedish": "sv",
    "Norwegian": "no",
    "Finnish": "fi",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Swahili": "sw",
    "Afrikaans": "af",
    "Albanian": "sq",
    "Belarusian": "be",
    "Catalan": "ca",
    "Irish": "ga",
    "Maltese": "mt",
    "Welsh": "cy"
}

def translate_text():
    try:
        text = input_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning(
                "Warning",
                "Please enter some text!"
            )
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror(
            "Translation Error",
            str(e)
        )

def copy_text():
    translated = output_box.get("1.0", tk.END)

    root.clipboard_clear()
    root.clipboard_append(translated)

    messagebox.showinfo(
        "Copied",
        "Translated text copied successfully!"
    )

def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("900x650")
root.resizable(True, True)

title = tk.Label(
    root,
    text="🌍 Language Translation Tool",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

input_label = tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 12, "bold")
)
input_label.pack()

input_box = tk.Text(
    root,
    height=8,
    width=90,
    font=("Arial", 11)
)
input_box.pack(pady=10)

lang_frame = tk.Frame(root)
lang_frame.pack(pady=10)

tk.Label(
    lang_frame,
    text="Source Language",
    font=("Arial", 10, "bold")
).grid(row=0, column=0, padx=10)

source_lang = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    width=25,
    state="readonly"
)
source_lang.set("Spanish")
source_lang.grid(row=0, column=1, padx=10)

tk.Label(
    lang_frame,
    text="Target Language",
    font=("Arial", 10, "bold")
).grid(row=0, column=2, padx=10)

target_lang = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    width=25,
    state="readonly"
)
target_lang.set("English")
target_lang.grid(row=0, column=3, padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

translate_btn = tk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    width=15,
    font=("Arial", 11, "bold")
)
translate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    command=copy_text,
    width=15,
    font=("Arial", 11, "bold")
)
copy_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=15,
    font=("Arial", 11, "bold")
)
clear_btn.grid(row=0, column=2, padx=10)

output_label = tk.Label(
    root,
    text="Translated Text",
    font=("Arial", 12, "bold")
)
output_label.pack()

output_box = tk.Text(
    root,
    height=8,
    width=90,
    font=("Arial", 11)
)
output_box.pack(pady=10)

footer = tk.Label(
    root,
    text="Supports 60 Languages | Powered by Google Translator",
    font=("Arial", 9)
)
footer.pack(pady=10)

root.mainloop()
