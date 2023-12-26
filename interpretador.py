import subprocess
import tkinter as tk
from tkinter import scrolledtext
import threading
import os

def executar_codigo():
    def thread_executar():
        try:
            codigo = entry_codigo.get("1.0", tk.END).strip()

            # Criar um arquivo batch temporário
            with open("temp_batch_file.bat", "w") as batch_file:
                batch_file.write(codigo)

            # Executar o arquivo batch
            processo = subprocess.run(['cmd', '/c', 'temp_batch_file.bat'], capture_output=True, text=True, check=True)

            # Obter a saída do comando
            saida_type = processo.stdout

            text_saida.delete("1.0", tk.END)
            text_saida.insert(tk.END, f"Saida do codigo:\n{saida_type}\n")

        except subprocess.CalledProcessError as e:
            # Exibir erros na área de texto
            text_saida.delete("1.0", tk.END)
            text_saida.insert(tk.END, f"Erro durante a execução: {e}")

        except Exception as e:
            # Exibir erros na área de texto
            text_saida.delete("1.0", tk.END)
            text_saida.insert(tk.END, f"Erro inesperado: {e}")

        finally:
            # Remover arquivo temporário
            os.remove("temp_batch_file.bat")

    # Iniciar uma nova thread para executar o código
    thread = threading.Thread(target=thread_executar)
    thread.start()

# Criar janela
janela = tk.Tk()
janela.title("Executor de Scripts Batch")

# Entrada para o código
label_codigo = tk.Label(janela, text="Digite o código:")
label_codigo.pack()

entry_codigo = scrolledtext.ScrolledText(janela, height=10, width=50)
entry_codigo.pack()

# Botão para executar
btn_executar = tk.Button(janela, text="Executar Código", command=executar_codigo)
btn_executar.pack()

# Saída
label_saida = tk.Label(janela, text="Saída:")
label_saida.pack()

text_saida = scrolledtext.ScrolledText(janela, height=10, width=50)
text_saida.pack()

# Iniciar a janela
if __name__ == "__main__":
    janela.mainloop()
