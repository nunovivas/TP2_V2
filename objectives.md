<h1>
Etapas de Desenvolvimento
</h1>
Considere a seguinte informação para o desenvolvimento do trabalho prático:
A aplicação deve ser desenvolvida em Python, utilizando exclusivamente a framework Flet.
Deve funcionar corretamente num dispositivo móvel (iOS ou Android) e num computador (Windows, macOS ou Linux).
Todos os objetivos especificados abaixo são obrigatórios e devem ser cumpridos na ordem em que são apresentados.
O peso de cada objetivo na avaliação está indicado entre parêntesis.
No entanto, sinta-se à vontade para explorar e experimentar funcionalidades adicionais, desde que as funcionalidades obrigatórias estejam implementadas e a aplicação esteja a funcionar corretamente.
Não serão aceites trabalhos que implementem estes objetivos de forma desconexa, ou seja, é necessário que sejam todos integrados numa app única.

<h3>(DONE)Objetivo 1 – Base (10%)</h3>
Siga os passos do seguinte tutorial:
Create a Calculator app in Python with Flet.
No final do Tutorial deverá ter implementado uma calculadora, com as seguintes funcionalidades:
Adição, subtração, multiplicação e divisão.
Inversão de sinal e percentagem.
Cálculo do resultado.
Limpeza do ecrã (AC).
Apresentação do resultado.
Calculadora

<h3>Objetivo 2 – Apresentação e Cálculo de Expressões Numéricas (25%)</h3>
A calculadora implementada apenas suporta instruções de cálculo simples, como 2 + 2 ou 3 * 4. No entanto, a calculadora deveria ser capaz de lidar com expressões mais complexas, como 2 + 3 * 4 ou (2 + 3) * 4 (i.e., ordem de operações PEMDAS/BODMAS).
Desta forma, altere o necessário para que a calculadora possa resolver expressões numéricas:
Veja o módulo SymPy para calcular o resultado de expressões numéricas.
Certifique-se que o cálculo do resultado apresenta a precisão dos arredondamentos correta.
Acrescente à calculadora um campo de texto, por cima do atual, onde se possa visualizar a expressão numérica completa.
Calculadora

<h3>(ALMOST DONE)Objetivo 3 – Funcionalidades Extra (15%)</h3>
Formate todos os números apresentados no campo de texto de entrada para utilizar um espaço como separador de milhares (e.g., 1 000 000 em vez de 1000000).
Acrescente à calculadora os seguintes quatro (4) botões standard:
Clear Entry (CE), para apagar a entrada atual.
Backspace (⬅️), para apagar o último dígito inserido.
Dois botões para adicionar parêntesis (abrir e fechar): ( e ).
Acrescente à calculadora pelo menos quatro (4) botões, à sua escolha, entre as seguintes opções:
Raiz quadrada
Inversão
Potência
-> Logaritmo
-> Exponencial
Fatorial
Seno
Cosseno
Tangente
Arco-seno
Arco-cosseno
Arco-tangente
Módulo
-> Valor absoluto
-> Número aleatório

<h3>Objetivo 4 – Histórico de Cálculos (25%)</h3>
Acrescente à calculadora um botão (ou outro controlo adequado) para mostrar/ocultar o histórico de cálculos.
Fica ao seu critério a forma como o histórico de cálculos é apresentado, mas terá de cumprir os seguintes requisitos:
Deve apresentar uma lista de expressões calculadas, com a mais recente no topo.
Cada elemento da lista deve conter:
Índice (auto-incrementado) do cálculo na lista
Data e hora do cálculo
Expressão numérica
Resultado
Um botão para apagar o elemento do histórico de cálculos.
Um botão para copiar o resultado para a área de transferência do dispositivo.
As expressões calculadas devem apenas ser adicionadas ao histórico quando é iniciado um novo cálculo (i.e., quando não é continuado um cálculo anterior).
Quando o histórico de cálculos chegar aos 10 elementos, os elementos mais antigos devem ser apagados automaticamente.

<h3>Objetivo 5 – Armazenamento Local do Histórico de Cálculos (15%)</h3>
Acrescente à calculadora a capacidade de salvar e carregar automaticamente o histórico de cálculos realizados, através de client-side storage.
O histórico deve deve ser salvo sempre que for alterado e carregado sempre que a aplicação for iniciada.

<h3>Objetivo 6 – Deploy no Replit (10%)</h3>
Prepare o deploy da aplicação – mude o favicon e a animação de carregamento: Customizing a web app.
Faça deploy da aplicação no Replit: Deploying a web app – Hosting providers – Replit.
Teste a aplicação em diferentes dispositivos/sistemas operativos e verifique se a aplicação está a funcionar corretamente.