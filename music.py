import tkinter as tk
import winsound




# Frequências das notas musicais
notas = {
    'C': 261,
    'D': 293,
    'E': 329,
    'F': 349,
    'G': 392,
    'A': 440,
    'B': 493,
}

# Função para tocar uma nota musical
def tocar_nota(nota, acorde):
    if nota in notas:
        frequencia = notas[nota] + acorde * 100
        winsound.Beep(frequencia, 300)  # Emitir som de "beep" quando o usuário
        
    else:
        print(f"Nota inválida: {nota}")

# Função para interpretar a sequência de entrada e tocar as notas
def interpretar_sequencia():
    sequencia = entrada_text.get("1.0", "end-1c").upper()
    acorde = 5  # Acorde inicial

    for caractere in sequencia:
        if caractere.isalnum():
            tocar_nota(caractere, acorde)
            acorde = (acorde + 1) % 10  # Altera o acorde de 0 a 9
        elif caractere == '\n':
            pass  # Ignora a quebra de linha
        else:
            print(f"Caractere inválido: {caractere}")

# Criar a janela
root = tk.Tk()
root.title("Interpretador de Notas Musicais")
root.configure(bg="yellow")

# Área de texto para introdução de letras ou números
entrada_text = tk.Text(root, wrap="none", width=40, height=10, bg="yellow", fg="black")
entrada_text.pack()
entrada_text.insert("1.0","ABCDEF\n1ABCDEF\n9ABCDEF\n")
# Botão para executar o interpretador
interpretar_button = tk.Button(root, text="Interpretar", command=interpretar_sequencia, bg="yellow", fg="black")
interpretar_button.pack()

root.mainloop()
