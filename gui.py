import tkinter as tk
from tkinter import messagebox
from db import crear_tabla, agregar_item, obtener_items, eliminar_item

class InventarioApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inventario Mecatrónico")
        self.root.geometry("500x400")
        crear_tabla()
        self.setup_ui()

    def setup_ui(self):
        self.nombre_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()

        tk.Label(self.root, text="Nombre:").pack()
        tk.Entry(self.root, textvariable=self.nombre_var).pack()
        tk.Label(self.root, text="Cantidad:").pack()
        tk.Entry(self.root, textvariable=self.cantidad_var).pack()
        tk.Label(self.root, text="Descripción:").pack()
        tk.Entry(self.root, textvariable=self.descripcion_var).pack()

        tk.Button(self.root, text="Agregar", command=self.agregar).pack(pady=5)
        tk.Button(self.root, text="Eliminar seleccionado", command=self.eliminar_seleccionado).pack(pady=5)

        self.lista = tk.Listbox(self.root)
        self.lista.pack(expand=True, fill="both")
        self.actualizar_lista()

    def agregar(self):
        nombre = self.nombre_var.get()
        cantidad = self.cantidad_var.get()
        descripcion = self.descripcion_var.get()
        if not nombre or not cantidad:
            messagebox.showwarning("Campos vacíos", "Por favor, rellena nombre y cantidad.")
            return
        try:
            cantidad_int = int(cantidad)
        except ValueError:
            messagebox.showwarning("Cantidad inválida", "La cantidad debe ser un número.")
            return
        agregar_item(nombre, cantidad_int, descripcion)
        self.nombre_var.set("")
        self.cantidad_var.set("")
        self.descripcion_var.set("")
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for item in obtener_items():
            self.lista.insert(tk.END, f"{item[0]}. {item[1]} ({item[2]}) - {item[3]}")

    def eliminar_seleccionado(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona un elemento para eliminar.")
            return
        item_text = self.lista.get(seleccion[0])
        item_id = int(item_text.split(".")[0])
        eliminar_item(item_id)
        self.actualizar_lista()

    def run(self):
        self.root.mainloop()