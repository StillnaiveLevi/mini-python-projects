import tkinter as tk
from tkinter import messagebox, ttk


LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Urdu": "ur",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Swahili": "sw",
}


class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Translator")
        self.geometry("860x560")
        self.minsize(760, 500)
        self.configure(bg="#f4f7fb")

        self.source_language = tk.StringVar(value="Auto Detect")
        self.target_language = tk.StringVar(value="English")
        self.status_text = tk.StringVar(value="Ready")

        self._build_styles()
        self._build_ui()

    def _build_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "TCombobox",
            fieldbackground="white",
            background="white",
            padding=7,
            arrowsize=14,
        )
        style.configure(
            "Primary.TButton",
            background="#2563eb",
            foreground="white",
            borderwidth=0,
            padding=(18, 10),
            font=("Segoe UI", 10, "bold"),
        )
        style.map("Primary.TButton", background=[("active", "#1d4ed8")])
        style.configure(
            "Tool.TButton",
            background="#e8eef8",
            foreground="#172033",
            borderwidth=0,
            padding=(14, 9),
            font=("Segoe UI", 10),
        )
        style.map("Tool.TButton", background=[("active", "#d7e2f3")])

    def _build_ui(self):
        header = tk.Frame(self, bg="#172033", height=76)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="Language Translator",
            bg="#172033",
            fg="white",
            font=("Segoe UI", 24, "bold"),
        ).pack(side="left", padx=28)

        main = tk.Frame(self, bg="#f4f7fb", padx=26, pady=24)
        main.pack(fill="both", expand=True)

        controls = tk.Frame(main, bg="#f4f7fb")
        controls.pack(fill="x", pady=(0, 16))

        self._language_picker(
            controls,
            "From",
            self.source_language,
            0,
            include_auto=True,
        )
        ttk.Button(
            controls,
            text="Swap",
            style="Tool.TButton",
            command=self.swap_languages,
        ).grid(row=0, column=1, padx=18, pady=(20, 0))
        self._language_picker(
            controls,
            "To",
            self.target_language,
            2,
            include_auto=False,
        )
        controls.columnconfigure(0, weight=1)
        controls.columnconfigure(2, weight=1)

        text_area = tk.Frame(main, bg="#f4f7fb")
        text_area.pack(fill="both", expand=True)
        text_area.columnconfigure(0, weight=1)
        text_area.columnconfigure(1, weight=1)
        text_area.rowconfigure(1, weight=1)

        tk.Label(
            text_area,
            text="Enter Text",
            bg="#f4f7fb",
            fg="#253044",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 7))
        tk.Label(
            text_area,
            text="Translation",
            bg="#f4f7fb",
            fg="#253044",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=1, sticky="w", padx=(16, 0), pady=(0, 7))

        self.input_text = tk.Text(
            text_area,
            wrap="word",
            undo=True,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#d7dfec",
            highlightcolor="#2563eb",
            font=("Segoe UI", 12),
            padx=14,
            pady=12,
        )
        self.input_text.grid(row=1, column=0, sticky="nsew", padx=(0, 8))

        self.output_text = tk.Text(
            text_area,
            wrap="word",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#d7dfec",
            highlightcolor="#2563eb",
            font=("Segoe UI", 12),
            padx=14,
            pady=12,
            bg="#fbfcff",
        )
        self.output_text.grid(row=1, column=1, sticky="nsew", padx=(8, 0))

        actions = tk.Frame(main, bg="#f4f7fb")
        actions.pack(fill="x", pady=(18, 0))

        ttk.Button(
            actions,
            text="Translate",
            style="Primary.TButton",
            command=self.translate_text,
        ).pack(side="left")
        ttk.Button(
            actions,
            text="Clear",
            style="Tool.TButton",
            command=self.clear_text,
        ).pack(side="left", padx=10)
        ttk.Button(
            actions,
            text="Copy Result",
            style="Tool.TButton",
            command=self.copy_result,
        ).pack(side="left")

        tk.Label(
            actions,
            textvariable=self.status_text,
            bg="#f4f7fb",
            fg="#5b6678",
            font=("Segoe UI", 10),
        ).pack(side="right")

    def _language_picker(self, parent, label, variable, column, include_auto):
        frame = tk.Frame(parent, bg="#f4f7fb")
        frame.grid(row=0, column=column, sticky="ew")
        tk.Label(
            frame,
            text=label,
            bg="#f4f7fb",
            fg="#253044",
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(0, 5))

        values = list(LANGUAGES.keys())
        if not include_auto:
            values.remove("Auto Detect")

        ttk.Combobox(
            frame,
            textvariable=variable,
            values=values,
            state="readonly",
            font=("Segoe UI", 11),
        ).pack(fill="x")

    def translate_text(self):
        source_text = self.input_text.get("1.0", "end-1c").strip()
        if not source_text:
            messagebox.showinfo("Translator", "Please enter text to translate.")
            return

        source = LANGUAGES[self.source_language.get()]
        target = LANGUAGES[self.target_language.get()]

        self.status_text.set("Translating...")
        self.update_idletasks()

        try:
            from deep_translator import GoogleTranslator

            translated = GoogleTranslator(source=source, target=target).translate(
                source_text
            )
        except ModuleNotFoundError:
            messagebox.showerror(
                "Missing package",
                "Install the translator package first:\n\npip install -r requirements.txt",
            )
            self.status_text.set("Missing dependency")
            return
        except Exception as exc:
            messagebox.showerror("Translation failed", str(exc))
            self.status_text.set("Translation failed")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translated)
        self.status_text.set("Done")

    def swap_languages(self):
        source = self.source_language.get()
        target = self.target_language.get()

        if source == "Auto Detect":
            messagebox.showinfo("Translator", "Choose a source language before swapping.")
            return

        self.source_language.set(target)
        self.target_language.set(source)

        input_value = self.input_text.get("1.0", "end-1c")
        output_value = self.output_text.get("1.0", "end-1c")
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, output_value)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, input_value)
        self.status_text.set("Languages swapped")

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status_text.set("Ready")

    def copy_result(self):
        result = self.output_text.get("1.0", "end-1c").strip()
        if not result:
            messagebox.showinfo("Translator", "There is no translation to copy.")
            return

        self.clipboard_clear()
        self.clipboard_append(result)
        self.status_text.set("Copied")


if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
