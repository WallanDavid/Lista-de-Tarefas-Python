import tkinter as tk
from tkinter import ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        # Categorias de tarefas
        self.categories = [
            "Tarefas Diárias", "Trabalho/Estudo", "Casa",
            "Saúde", "Projetos Pessoais", "Finanças",
            "Social", "Autoaperfeiçoamento", "Tempo Livre/Relaxamento"
        ]

        # Dicionário para armazenar as tarefas em cada categoria
        self.tasks = {category: [] for category in self.categories}

        # Criar uma combobox para selecionar a categoria
        self.category_var = tk.StringVar()
        self.category_var.set(self.categories[0])  # Definir a categoria padrão
        self.category_dropdown = ttk.Combobox(root, textvariable=self.category_var, values=self.categories)
        self.category_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # Entrada para adicionar tarefas
        self.task_entry = ttk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para adicionar tarefas
        add_button = ttk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        add_button.grid(row=0, column=2, padx=10, pady=10)

        # Lista para exibir as tarefas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botão para excluir tarefa selecionada
        delete_button = ttk.Button(root, text="Excluir Tarefa", command=self.delete_task)
        delete_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Popular a lista inicialmente com tarefas
        self.populate_task_list()

    def add_task(self):
        category = self.category_var.get()
        task = self.task_entry.get()
        if task:
            self.tasks[category].append(task)
            self.populate_task_list()
            self.task_entry.delete(0, tk.END)  # Limpar a entrada após adicionar a tarefa

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            category = self.category_var.get()
            del self.tasks[category][selected_task_index[0]]
            self.populate_task_list()

    def populate_task_list(self):
        # Limpar a lista antes de popular
        self.task_listbox.delete(0, tk.END)
        
        # Popular a lista com as tarefas da categoria selecionada
        category = self.category_var.get()
        for task in self.tasks[category]:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
