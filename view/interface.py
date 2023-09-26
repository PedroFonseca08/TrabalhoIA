import tkinter as tk
from controller.variavelglobal import listaHorarios

def atualizar_lista():
    lista_box.delete(0, tk.END)  # Limpa a lista atual
    for horario in listaHorarios:
        lista_box.insert(tk.END, horario)

def criar_interface():
  global horario_entry 
  global lista_box

  root = tk.Tk()
  root.title("Horários")
  root.geometry("400x500")  # Aumenta a altura da janela
  root.iconbitmap(r'C:\Users\pedro\OneDrive\Área de Trabalho\TrabalhoIA\model\icone.ico')

  # Criação da lista de horários
  lista_frame = tk.Frame(root)
  lista_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Preenche o espaço disponível

  scrollbar = tk.Scrollbar(lista_frame, orient=tk.VERTICAL)
  lista_box = tk.Listbox(lista_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, font=("Arial", 12))
  scrollbar.config(command=lista_box.yview)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
  lista_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

  # Botão para fechar a janela
  fechar_button = tk.Button(root, text="Fechar", command=root.quit)
  fechar_button.pack(padx=10, pady=10)

  root.mainloop()