# Interpretador-para-.bat
#interface Gráfica (GUI):

O código utiliza a biblioteca Tkinter para criar uma interface gráfica para o usuário.
Um rótulo (label_codigo) é exibido para indicar onde o usuário deve inserir o código.
Uma caixa de texto com rolagem (entry_codigo) é fornecida para o usuário inserir o código do script batch.
Um botão (btn_executar) é fornecido para iniciar a execução do script.
#Função executar_codigo:

A função executar_codigo é chamada quando o botão "Executar Código" é pressionado.
A função obtém o código do script a partir da caixa de texto.
Cria um arquivo batch temporário (temp_batch_file.bat) e escreve o código nesse arquivo.
Usa subprocess.Popen para executar o arquivo batch temporário no prompt de comando.
Captura a saída padrão do processo e exibe na área de texto (text_saida) na interface gráfica.
Lida com exceções (como CalledProcessError) e exibe mensagens de erro na área de texto.
#Thread:

A função thread_executar é definida dentro de executar_codigo e é usada como o alvo da thread.
A thread é iniciada para permitir que a execução do código ocorra em segundo plano, mantendo a interface responsiva.
Remoção do Arquivo Batch Temporário:

Após a execução, o arquivo batch temporário é removido no bloco finally para limpar os recursos.
#Avisos:

Um aviso é incluído no código indicando que é apenas um executor de scripts batch, não um interpretador. Isso sugere que, por enquanto, o código lida principalmente com a execução de scripts existentes, em vez de interpretar novos comandos interativamente.
