import bs4
import re, httpx, io, os
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from tkinter import (
    Tk,
    ttk,
    Text,
    Entry,
    Label,
    Button,
    Checkbutton,
    filedialog,
    Radiobutton,
    font,
    OptionMenu,
    StringVar,
    dialog
)

class RenderKit(Tk):
    def __init__(self,
                html: str,
                width: int = 500,
                height: int = 500,
                background = None
            ) -> None:
        super().__init__()
        self._elements: dict = {}

        self.display(html)

        if background:
            background(self)

        self.geometry(f"{width}x{height}")
        self.mainloop()

    def get(self, element_id: str):
        return self._elements.get(element_id, None)

    def display(self, html: str) -> None:
        parser = BeautifulSoup(html, "html.parser")

        for element in parser.find_all(True):

            id: str = element.get("id") if element.get("id") else ""

            alignments: dict = {"left": "w", "right": "e", "top": "n", "bottom": "s"}
            alignment: str = element.get("align")

            if alignment and "center" not in alignment:
                alignment = "".join([alignments.get(i, "") for i in alignment.split(" ")])
            elif alignment and alignment == "center":
                pass
            else:
                alignment = "nw"

            if element.name == "title":
                self.title(element.text)

            elif element.name.startswith("h") and len(element.name) == 2:
                font_sizes: dict = {"h1": 32, "h2": 26, "h3": 24, "h4": 20, "h5" : 18}
                font_size = font.Font(size=font_sizes.get(element.name, 14))

                heading = Label(self, text=element.text, font=font_size)
                heading.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = heading

            elif element.name == "p":
                paragraph = Label(self, text=element.text)
                paragraph.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = paragraph

            elif element.name == "input" and element.get("type") == "text":
                text_input = Entry(self)
                text_input.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = text_input

            elif element.name == "input" and element.get("type") == "password":
                passwd_input = Entry(self, show="*")
                passwd_input.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = passwd_input

            elif element.name == "input" and element.get("type") == "checkbox":
                checkbox = Checkbutton(self)
                checkbox.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = checkbox

            elif element.name == "input" and element.get("type") == "radio":
                radio = Radiobutton(self)
                radio.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = radio

            elif element.name == "textarea":
                textarea = Text(self)
                textarea.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = textarea

            elif element.name == "button":
                button = Button(self, text=element.text)
                button.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = button

            elif element.name == "select":
                options: list = [option.text for option in element.find_all("option")]

                inital_value = StringVar(self)
                inital_value.set(options[0])

                select_menu = OptionMenu(self, inital_value, *options)
                select_menu.pack(padx=2, pady=2, anchor=alignment)

                if id:
                    self._elements[id] = select_menu

            elif element.name == "img":
                image_src = element.get("src", "")
                image_height = element.get("height", "")
                image_width = element.get("width", "")
                image_content = None

                if re.match(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', image_src):
                    image_content = httpx.get(image_src).content
                    image_content = Image.open(io.BytesIO(image_content))
                elif os.path.exists(image_src):
                    image_content = Image.open(image_src)
                else:
                    continue

                if image_content:
                    if image_width and image_height:
                        image_content = image_content.resize((int(image_width), int(image_height)))
                    image = ImageTk.PhotoImage(image_content)
                    image_label = Label(self, image=image)
                    image_label.image = image
                    image_label.pack(padx=2, pady=2, anchor=alignment)

                    if id:
                        self._elements[id] = image_label

    def addEventListener(self, widget, name, handler) -> None:
        events = {
            "click": "<Button-1>",
            "double_click": "<Double-Button-1>",
            "triple_click": "<Triple-Button-1>",
            "middle_click": "<Button-2>",
            "right_click": "<Button-3>",
            "scroll_up": "<Button-4>",
            "scroll_down": "<Button-5>",
            "button_release": "<ButtonRelease-1>",
            "return_press": "<Return>",
            "enter": "<Enter>",
            "leave": "<Leave>",
            "motion": "<Motion>",
            "key_press": "<KeyPress>",
            "key_release": "<KeyRelease>",
            "focus_in": "<FocusIn>",
            "focus_out": "<FocusOut>",
            "destroy": "<Destroy>",
            "visibility": "<Visibility>",
            "mouse_wheel": "<MouseWheel>"
        }

        if name in events:
            widget.bind(events[name], lambda e: handler(name, e))
