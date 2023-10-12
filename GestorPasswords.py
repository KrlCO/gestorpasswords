from tkinter import CENTER, Entry, Tk, Label, Button
from tkinter import ttk

class root_window:

    def __init__(self, root):
        self.root = root
        self.root.title("Cancerbero")
        self.root.geometry("900x550+140+40")

        head_title = Label(self.root, text="Cancerbero", width=40, bg="purple", font=("Ariel",20), padx=10, pady=10, justify=CENTER, anchor="center").grid(columnspan=4, padx=140, pady=20)

        crud_frame = ttk.Frame(self.root)
        crud_frame.grid()


        entry_boxes = []
        row_no = col_no = 0
        for i in range(4):
            show=""
            if i == 3:
                show = "*"
            entry_box = Entry(crud_frame, width=20, background="lightgrey", font=("Ariel", 12), show=show)
            entry_box.grid(row=row_no, column=col_no, padx=5, pady=2)
            col_no +=1




if  __name__ == "__main__": 
    root = Tk() 
    root_class = root_window(root) 
    root.mainloop()