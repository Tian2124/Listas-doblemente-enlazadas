import tkinter as tk
import ttkbootstrap as ttk
from linked_list import DoublyLinkedList

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor con Historial")

        self.history = DoublyLinkedList()

        self.text_area = tk.Text(root, height=15, width=60)
        self.text_area.pack(pady=10)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack()

        self.save_button = ttk.Button(self.button_frame, text="Guardar estado", command=self.save_state)
        self.save_button.pack(side="left", padx=5)

        self.undo_button = ttk.Button(self.button_frame, text="Deshacer", command=self.undo)
        self.undo_button.pack(side="left", padx=5)

        self.redo_button = ttk.Button(self.button_frame, text="Rehacer", command=self.redo)
        self.redo_button.pack(side="left", padx=5)

    def save_state(self):
        text = self.text_area.get("1.0", tk.END).strip()
        self.history.append(text)

    def undo(self):
        self.history.move_backward()
        self._update_text_area()

    def redo(self):
        self.history.move_forward()
        self._update_text_area()

    def _update_text_area(self):
        self.text_area.delete("1.0", tk.END)
        current_text = self.history.current()
        self.text_area.insert(tk.END, current_text)

if __name__ == "__main__":
    root = ttk.Window(themename="litera")
    app = TextEditorApp(root)
    root.mainloop()

