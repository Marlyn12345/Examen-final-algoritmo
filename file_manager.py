import tkinter as tk
import csv
import tkinter.messagebox
import os

def save_data():
    name = entry_name.get()
    grade = entry_grade.get()
    
    if name == "" or grade == "":
        tkinter.messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
        return
    
    try:
        grade = int(grade)
    except ValueError:
        tkinter.messagebox.showerror("Error", "La nota debe ser un número.")
        return
    
    with open('notas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])
    
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    
    tkinter.messagebox.showinfo("Éxito", "Datos guardados correctamente.")

root = tk.Tk()
root.title("Gestor de Notas")

root.config(bg="#f0f0f0")

label_name = tk.Label(root, text="Nombre:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
label_name.pack(pady=5)

entry_name = tk.Entry(root, font=("Arial", 12), bg="white", fg="black", bd=2)
entry_name.pack(pady=5)


label_grade = tk.Label(root, text="Nota:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
label_grade.pack(pady=5)


entry_grade = tk.Entry(root, font=("Arial", 12), bg="white", fg="black", bd=2)
entry_grade.pack(pady=5)


save_button = tk.Button(root, text="Guardar", command=save_data, font=("Arial", 12), bg="#4CAF50", fg="white", bd=2, relief="raised")
save_button.pack(pady=10)


root.geometry("300x250")

if not os.path.exists('notas.csv'):
    with open('notas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Nota"])

root.mainloop()

