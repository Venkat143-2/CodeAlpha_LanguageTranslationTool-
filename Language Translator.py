import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import threading
import pyperclip
languages = {
    "English": "en", "Telugu": "te", "Hindi": "hi", "Tamil": "ta", "Kannada": "kn",
    "Malayalam": "ml", "Marathi": "mr", "Gujarati": "gu", "Punjabi": "pa", "Bengali": "bn",
    "Urdu": "ur", "Odia": "or", "Assamese": "as", "Sanskrit": "sa", "French": "fr",
    "Spanish": "es", "German": "de", "Italian": "it", "Portuguese": "pt", "Russian": "ru",
    "Japanese": "ja", "Korean": "ko", "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW",
    "Arabic": "ar", "Turkish": "tr", "Dutch": "nl", "Polish": "pl", "Thai": "th",
    "Vietnamese": "vi", "Indonesian": "id", "Malay": "ms", "Filipino": "tl", "Greek": "el",
    "Hebrew": "iw", "Persian": "fa", "Ukrainian": "uk", "Romanian": "ro", "Hungarian": "hu",
    "Czech": "cs", "Slovak": "sk", "Bulgarian": "bg", "Croatian": "hr", "Serbian": "sr",
    "Slovenian": "sl", "Danish": "da", "Swedish": "sv", "Norwegian": "no", "Finnish": "fi",
    "Lithuanian": "lt", "Latvian": "lv", "Estonian": "et", "Swahili": "sw", "Afrikaans": "af",
    "Albanian": "sq", "Belarusian": "be", "Catalan": "ca", "Irish": "ga", "Maltese": "mt", "Welsh": "cy"
}
def translate_text():
    def translate_worker():
        try:
            text = input_box.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Warning", "Enter some text, soldier!")
                return
            source = languages[source_lang.get()]
            target = languages[target_lang.get()]
            translated = GoogleTranslator(source=source, target=target).translate(text)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("Translation Failed", f"Error: {str(e)}\nCheck your internet!")
    threading.Thread(target=translate_worker, daemon=True).start()
def copy_text():
    translated = output_box.get("1.0", tk.END).strip()
    if translated:
        pyperclip.copy(translated)
        messagebox.showinfo("Victory!", "Text copied to clipboard")
    else:
        messagebox.showwarning("Empty", "Nothing to copy.")
def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)
def update_char_count(event=None):
    count = len(input_box.get("1.0", tk.END).strip())
    char_label.config(text=f"Characters: {count}/5000")
root = tk.Tk()
root.title("🌍 Elite Language Translator")
root.geometry("950x700")
root.configure(bg="#0f0f0f")
root.resizable(True, True)
title = tk.Label(root, text="🌍 Elite Language Translator", 
                 font=("Arial", 22, "bold"), fg="#00ff9d", bg="#0f0f0f")
title.pack(pady=15)
input_label = tk.Label(root, text="Enter Text", font=("Arial", 12, "bold"), fg="white", bg="#0f0f0f")
input_label.pack(anchor="w", padx=20)
input_box = tk.Text(root, height=10, width=100, font=("Arial", 11), bg="#1e1e1e", fg="white", insertbackground="white")
input_box.pack(pady=10, padx=20)
input_box.bind("<KeyRelease>", update_char_count)
char_label = tk.Label(root, text="Characters: 0/5000", font=("Arial", 10), fg="#888888", bg="#0f0f0f")
char_label.pack(anchor="e", padx=20)
lang_frame = tk.Frame(root, bg="#0f0f0f")
lang_frame.pack(pady=10)
tk.Label(lang_frame, text="Source:", font=("Arial", 11, "bold"), fg="white", bg="#0f0f0f").grid(row=0, column=0, padx=8)
source_lang = ttk.Combobox(lang_frame, values=list(languages.keys()), width=28, state="readonly")
source_lang.set("Spanish")
source_lang.grid(row=0, column=1, padx=8)
tk.Label(lang_frame, text="Target:", font=("Arial", 11, "bold"), fg="white", bg="#0f0f0f").grid(row=0, column=2, padx=8)
target_lang = ttk.Combobox(lang_frame, values=list(languages.keys()), width=28, state="readonly")
target_lang.set("English")
target_lang.grid(row=0, column=3, padx=8)
button_frame = tk.Frame(root, bg="#0f0f0f")
button_frame.pack(pady=15)
translate_btn = tk.Button(button_frame, text="🔥 Translate", command=translate_text,
                          width=18, font=("Arial", 11, "bold"), bg="#00ff9d", fg="black")
translate_btn.grid(row=0, column=0, padx=10)
copy_btn = tk.Button(button_frame, text="📋 Copy", command=copy_text,
                     width=18, font=("Arial", 11, "bold"), bg="#1e90ff", fg="white")
copy_btn.grid(row=0, column=1, padx=10)
clear_btn = tk.Button(button_frame, text="🗑 Clear", command=clear_text,
                      width=18, font=("Arial", 11, "bold"), bg="#ff4444", fg="white")
clear_btn.grid(row=0, column=2, padx=10)
output_label = tk.Label(root, text="Translated Text", font=("Arial", 12, "bold"), fg="white", bg="#0f0f0f")
output_label.pack(anchor="w", padx=20)
output_box = tk.Text(root, height=10, width=100, font=("Arial", 11), bg="#1e1e1e", fg="#00ff9d")
output_box.pack(pady=10, padx=20)
footer = tk.Label(root, text="Supports 60+ Languages | Powered by Google Translate • Built with Discipline",font=("Arial", 9), fg="#666666", bg="#0f0f0f")
footer.pack(pady=10)
root.mainloop()
