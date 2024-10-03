import tkinter as tk

def add_task():
    task=task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)

def remove_task():
    selected_task_index=task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")

task_listbox = tk.Listbox(root)
task_listbox.pack(pady=10)

task_entry = tk.Entry(root)
task_entry.pack(pady=10)
add_button = tk.Button(root,text="Add Task",command=add_task)
remove_button = tk.Button(root,text="Remove Task",command=remove_task)
add_button.pack()
remove_button.pack()
root.mainloop()
                          


