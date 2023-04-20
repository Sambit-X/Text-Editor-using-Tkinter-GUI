from tkinter import *

class StackEditor:
    def __init__(self):
        self.stack = []
        self.undo_stack = []

    def insert(self, text):
        self.stack.append(text)
        self.undo_stack.clear()

    def delete(self):
        if self.stack:
            self.undo_stack.append(self.stack.pop())
        else:
            print("Editor is empty")

    def redo(self):
        if self.undo_stack:
            self.stack.append(self.undo_stack.pop())
        else:
            print("Nothing to redo")

    def undo(self):
        if self.stack:
            self.undo_stack.append(self.stack.pop())
        else:
            print("Nothing to undo")

    def get_text(self):
        return "".join(self.stack)

    def cut(self):
        if self.stack:
            cut_text = self.stack[-1]
            self.stack[-1] = ""
            self.undo_stack.append(cut_text)
        else:
            print("Editor is empty")

    def copy(self):
        if self.stack:
            copy_text = self.stack[-1]
            self.undo_stack.append(copy_text)
        else:
            print("Editor is empty")

    def paste(self):
        if self.undo_stack:
            paste_text = self.undo_stack[-1]
            self.stack.append(paste_text)
        else:
            print("Nothing to paste")

def insert_text():
    text = text_entry.get()
    editor.insert(text)
    text_entry.delete(0, END)
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

def delete_last_char():
    editor.delete()
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

def redo_last_change():
    editor.redo()
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

def undo_last_change():
    editor.undo()
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

def cut_last_word():
    editor.cut()
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

def copy_last_word():
    editor.copy()
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

def paste_text():
    editor.paste()
    text_area.delete("1.0", END)
    text_area.insert(END, editor.get_text())

# Initialize a StackEditor object
editor = StackEditor()

# Create a window
root = Tk()
root.title("TextEditor")
root.configure(bg='#BDEDFF')

# Create a text entry field for users to enter text
text_entry = Entry(root,width=50)
text_entry.pack(side=TOP,pady=5)
text_entry.configure(bg='#E5E4E2')

# Create frames 
frame1 = Frame(root)
frame1.pack(side=TOP,pady=5)
frame1.configure(bg='#BDEDFF')

frame2 = Frame(root)
frame2.pack(side=TOP,pady=5)
frame2.configure(bg='#BDEDFF')

frame3 = Frame(root)
frame3.pack(side=TOP,pady=5)
frame3.configure(bg='#BDEDFF')


# Create buttons for the different operations
insert_button = Button(frame1, text="Insert", command=insert_text, width=10)
insert_button.pack(side=LEFT, padx=5)
delete_button = Button(frame1, text="Delete", command=delete_last_char, width=10)
delete_button.pack(side=LEFT, padx=5)

undo_button = Button(frame2, text="Undo", command=undo_last_change, width=10)
undo_button.pack(side=LEFT, padx=5)
redo_button = Button(frame2, text="Redo", command=redo_last_change, width=10)
redo_button.pack(side=LEFT, padx=5)

cut_button = Button(frame3, text="Cut", command=cut_last_word, width=10)
cut_button.pack(side=LEFT, padx=5)
copy_button = Button(frame3, text="Copy", command=copy_last_word, width=10)
copy_button.pack(side=LEFT, padx=5)
paste_button = Button(frame3, text="Paste", command=paste_text, width=10)
paste_button.pack(side=LEFT, padx=5)

# Create a text area to display the current text in the editor
text_area = Text(root)
text_area.pack(expand=True,padx=10,pady=10,fill=BOTH)
text_area.configure(bg='#E5E4E2')

# Start the event loop to handle user input
root.mainloop()