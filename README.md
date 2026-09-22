<h1>Relatório de alterações</h1>

<h3>Problemas encontrados</h3>

<li>O programa permitia cadastrar alunos com nomes iguais mas retornava apenas um na busca</li>

<h3>Solução</h3>

<p>Antes o programa fazia a busca através de um for que comparava a o nome que o usuário digitava com os elementos da lista de alunos conforme a posição do loop e retornava quando encontrava, o problema é que caso houvesse mais de um aluno com o mesmo nome, o programa iria retornar somente o primeiro  e iria sair do loop. A solução para isso foi criar um novo vetor chamado de resultados, o for continua fazendo a exata mesma coisa, mas ao invés de retornar os elementos que ele encontra, dessa vez ele vai armazenar em um novo vetor, quando terminar de percorrer todos os elementos será mostrado os elementos do novo vetor  </p>

<h3>Novas funcionalidades</h3>

<h4>Alteração da nota</h4>
<p>Depois da busca, a função selecionar_aluno() é utilizada para identificar exatamente qual aluno será alterado. Após a seleção, o código acessa o dicionário desse aluno e modifica o valor armazenado na chave "nota".</p>

<h4>Edição do aluno</h4>
<p>A função editar_aluno() segue a mesma lógica de seleção utilizada na alteração de nota.
Primeiro, o aluno é localizado através do nome. Depois, caso existam vários resultados, o usuário seleciona qual cadastro deseja editar.</p>

<h4>Exclusão de aluno</h4>

<p>A função excluir_aluno() primeiro utiliza a busca pelo nome para localizar os possíveis alunos. Depois de selecionar o aluno, o código identifica sua posição dentro da lista alunos e utiliza o método pop() para remover aquele elemento. </p>

<h4>Prova de recuperação</h4>

<p>A função prova_recuperacao() começa  localizando o aluno que realizará a prova.
Depois disso, são apresentadas duas perguntas. Uma variável chamada acertos começa com o valor 0.

Ao final das duas questões, o código verifica a quantidade de acertos utilizando um if.

Caso acertos == 2, o código acessa a chave "nota" do dicionário do aluno selecionado e altera seu valor para 10.</p>
