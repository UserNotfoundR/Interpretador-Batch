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
            processo_start = subprocess.Popen(f'start cmd /c temp_batch_file.bat', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            saida_start, _ = processo_start.communicate()

            if processo_start.returncode != 0:
                # Se o processo retornar um código diferente de 0, significa que ocorreu um erro
                raise subprocess.CalledProcessError(processo_start.returncode, cmd=f'start cmd /c {codigo}')

            text_saida.delete("1.0", tk.END)
            text_saida.insert(tk.END, f"Saida do codigo: {saida_start}")

        except subprocess.CalledProcessError as e:
            text_saida.delete("1.0", tk.END)
            text_saida.insert(tk.END, f"Erro durante a execução: {e}")

        except Exception as e:
            text_saida.delete("1.0", tk.END)
            text_saida.insert(tk.END, f"Erro inesperado: {e}")

        finally:
            # Remover o arquivo batch temporário
            os.remove("temp_batch_file.bat")

    # Criar e iniciar a thread
    thread = threading.Thread(target=thread_executar)
    thread.start()

# Restante do código permanece inalterado


# Criar janela
janela = tk.Tk()
janela.title("Interpretador")

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
