# Johnson To-Do App: Module 10 Assignment

import tkinter as tk
import tkinter.messagebox as msg

#Colors (complementary: gold + purple)
EVEN_TASK_BG = "#FFD700"   # gold
EVEN_TASK_FG = "#000000"   # black text on gold
ODD_TASK_BG  = "#800080"   # purple
ODD_TASK_FG  = "#FFFFFF"   # white text on purple


class Todo(tk.Tk):

    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = tasks if tasks else []

        #File and exit menu
        self.menubar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.quit_app)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menubar)

        #Window setup
        self.title("Johnson To-Do App")
        self.geometry("300x400")

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame  = tk.Frame(self.tasks_canvas)
        self.text_frame   = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        #Tells user how to delete
        instruction = tk.Label(
            self.tasks_frame,
            text="Items Added --- ** Right Click Item to Delete**",
            bg=EVEN_TASK_BG, fg=EVEN_TASK_FG, pady=10,
        )
        instruction.bind("<Button-3>", self.remove_task)
        self.tasks.append(instruction)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>",   self.mouse_scroll)
        self.bind_all("<Button-5>",   self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [
            {"bg": EVEN_TASK_BG, "fg": EVEN_TASK_FG},
            {"bg": ODD_TASK_BG,  "fg": ODD_TASK_FG},
        ]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-3>", self.remove_task)  #right-click to delete
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
            self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete \"" + task.cget("text") + "\"?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):

        _, even_or_odd = divmod(position, 2)
        colors = self.colour_schemes[even_or_odd]
        task.configure(bg=colors["bg"], fg=colors["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        self.tasks_canvas.itemconfig(self.canvas_frame, width=event.width)

    def mouse_scroll(self, event):
        if event.delta:

            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:

            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

    def quit_app(self):
        if msg.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
