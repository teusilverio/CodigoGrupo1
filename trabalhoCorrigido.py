import statistics

alunos = []


# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def situacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


def desempenho(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota >= 6:
        return "Regular"
    else:
        return "Reprovado"


def calcular_media():
    if len(alunos) == 0:
        return 0

    soma = 0

    for aluno in alunos:
        soma += aluno["nota"]

    return soma / len(alunos)


def buscar_aluno(nome):
    encontrados = []
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            encontrados.append(aluno)

    return encontrados


# ============================================
# 1 - CADASTRAR ALUNOS
# ============================================

def cadastrar_alunos():

    print("\n========================================")
    print("CADASTRO DE ALUNOS")
    print("========================================")

    while True:
        try:
            quantidade = int(input("Quantidade de alunos: "))

            if quantidade <= 0:
                print("Erro: a quantidade deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Erro: digite um número inteiro.")

    for i in range(quantidade):

        print(f"\nAluno {i + 1}")

        while True:
            nome = input("Nome: ").strip()

            if nome == "":
                print("Erro: o nome não pode ficar vazio.")
            else:
                break

        while True:
            try:
                nota = float(input("Nota final: ").replace(",", "."))

                if nota < 0 or nota > 10:
                    print("Erro: a nota deve estar entre 0 e 10.")
                    continue

                break

            except ValueError:
                print("Erro: digite uma nota válida.")

        aluno = {
            "nome": nome,
            "nota": nota
        }

        alunos.append(aluno)

        print("Aluno cadastrado com sucesso!")


# ============================================
# 2 - LISTAR ALUNOS
# ============================================

def listar_alunos():

    print("\n========================================")
    print("LISTA DE ALUNOS")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:

        nota = aluno["nota"]

        print(f"\nNome: {aluno['nome']}")
        print(f"Nota: {nota:.2f}")
        print(f"Situação: {situacao(nota)}")
        print(f"Desempenho: {desempenho(nota)}")
        print("----------------------------------------")


# ============================================
# 3 - ESTATÍSTICAS DA TURMA
# ============================================

def estatisticas():

    print("\n========================================")
    print("ESTATÍSTICAS DA TURMA")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    notas = []

    aprovados = 0
    reprovados = 0

    for aluno in alunos:

        notas.append(aluno["nota"])

        if aluno["nota"] >= 6:
            aprovados += 1
        else:
            reprovados += 1

    total = len(alunos)

    media = sum(notas) / total

    maior_nota = max(notas)

    menor_nota = min(notas)

    mediana = statistics.median(notas)

    amplitude = maior_nota - menor_nota

    percentual_aprovacao = (aprovados / total) * 100

    percentual_reprovacao = (reprovados / total) * 100

    print(f"Total de alunos: {total}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Menor nota: {menor_nota:.2f}")
    print(f"Amplitude: {amplitude:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
    print(f"Percentual de reprovação: {percentual_reprovacao:.2f}%")


# ============================================
# 4 - ALUNOS ACIMA DA MÉDIA
# ============================================

def alunos_acima_media():

    print("\n========================================")
    print("ALUNOS ACIMA DA MÉDIA")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    media = calcular_media()

    print(f"Média da turma: {media:.2f}\n")

    encontrou = False

    for aluno in alunos:

        if aluno["nota"] > media:

            print(f"{aluno['nome']} - {aluno['nota']:.2f}")

            encontrou = True

    if encontrou == False:
        print("Nenhum aluno ficou acima da média da turma.")


# ============================================
# 5 - DISTRIBUIÇÃO DAS NOTAS
# ============================================

def distribuicao_notas():

    print("\n========================================")
    print("DISTRIBUIÇÃO DAS NOTAS")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    faixa1 = 0
    faixa2 = 0
    faixa3 = 0
    faixa4 = 0
    faixa5 = 0

    for aluno in alunos:

        nota = aluno["nota"]

        if nota < 3:
            faixa1 += 1

        elif nota < 5:
            faixa2 += 1

        elif nota < 6:
            faixa3 += 1

        elif nota < 8:
            faixa4 += 1

        else:
            faixa5 += 1

    print(f"0,0 - 2,9  : {faixa1} aluno(s)")
    print(f"3,0 - 4,9  : {faixa2} aluno(s)")
    print(f"5,0 - 5,9  : {faixa3} aluno(s)")
    print(f"6,0 - 7,9  : {faixa4} aluno(s)")
    print(f"8,0 - 10,0 : {faixa5} aluno(s)")


# ============================================
# 6 - RANKING DA TURMA
# ============================================

def ranking():

    print("\n========================================")
    print("RANKING DA TURMA")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    ranking_alunos = sorted(
        alunos,
        key=lambda aluno: aluno["nota"],
        reverse=True
    )

    for i in range(len(ranking_alunos)):

        aluno = ranking_alunos[i]

        print(
            f"{i + 1}º - "
            f"{aluno['nome']} "
            f"{aluno['nota']:.2f}"
        )

    print("\n========================================")
    print("TOP 3 DA TURMA")
    print("========================================")

    quantidade_top = min(3, len(ranking_alunos))

    for i in range(quantidade_top):

        aluno = ranking_alunos[i]

        print(
            f"{i + 1}º - "
            f"{aluno['nome']} "
            f"{aluno['nota']:.2f}"
        )


# ============================================
# 7 - CONSULTAR ALUNO
# ============================================

def consultar_aluno():

    print("\n========================================")
    print("CONSULTAR ALUNO")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ").strip()

    encontrados = buscar_aluno(nome)

    if len(encontrados) == 0:

        print("Erro: aluno não encontrado.")

        return

    print(f"\nForam encontrados {len(encontrados)} aluno(s):")
    for i, aluno in enumerate(encontrados):

        nota = aluno["nota"]

        print("\nAluno encontrado:")
        print(f"Nome: {aluno['nome']}")
        print(f"Nota: {aluno['nota']:.2f}")
        print(f"Situação: {situacao(aluno['nota'])}")
        print(f"Desempenho: {desempenho(aluno['nota'])}")


# ============================================
# 8 - ALTERAR NOTA
# ============================================

def alterar_nota():

    print("\n========================================")
    print("ALTERAR NOTA")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ").strip()

    encontrados = buscar_aluno(nome)

    if len(encontrados) == 0:
        print("Erro: aluno não encontrado.")
        return

    if len(encontrados) > 1:

        print("\nForam encontrados vários alunos:")

        for i, aluno in enumerate(encontrados):
            print(f"{i + 1} - {aluno['nome']} - Nota: {aluno['nota']:.2f}")

        while True:
            try:
                escolha = int(input("\nEscolha o número do aluno: "))

                if escolha < 1 or escolha > len(encontrados):
                    print("Erro: escolha uma opção válida.")
                    continue

                aluno = encontrados[escolha - 1]
                break

            except ValueError:
                print("Erro: digite um número inteiro.")

    else:
        # Só existe um aluno com esse nome
        aluno = encontrados[0]

    print(f"\nNota atual: {aluno['nota']:.2f}")

    while True:

        try:
            nova_nota = float(
                input("Digite a nova nota: ").replace(",", ".")
            )

            if nova_nota < 0 or nova_nota > 10:
                print("Erro: a nota deve estar entre 0 e 10.")
                continue

            aluno["nota"] = nova_nota

            print("Nota alterada com sucesso!")
            break

        except ValueError:
            print("Erro: digite uma nota válida.")



# ============================================
# 9 - GERAR RELATÓRIO COMPLETO
# ============================================

def gerar_relatorio_completo():

    print("\n========================================")
    print("RELATÓRIO DA TURMA")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    notas = []

    aprovados = 0
    reprovados = 0

    for aluno in alunos:

        notas.append(aluno["nota"])

        if aluno["nota"] >= 6:
            aprovados += 1
        else:
            reprovados += 1

    total = len(alunos)

    media = sum(notas) / total

    maior_nota = max(notas)

    menor_nota = min(notas)

    mediana = statistics.median(notas)

    amplitude = maior_nota - menor_nota

    percentual_aprovacao = (aprovados / total) * 100

    percentual_reprovacao = (reprovados / total) * 100

    print(f"Total de alunos: {total}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Menor nota: {menor_nota:.2f}")
    print(f"Amplitude: {amplitude:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
    print(f"Percentual de reprovação: {percentual_reprovacao:.2f}%")

    print("----------------------------------------")
    print("ALUNOS ACIMA DA MÉDIA")
    print("----------------------------------------")

    encontrou = False

    for aluno in alunos:

        if aluno["nota"] > media:

            print(
                f"{aluno['nome']} "
                f"{aluno['nota']:.2f}"
            )

            encontrou = True

    if encontrou == False:
        print("Nenhum aluno acima da média.")

    print("----------------------------------------")
    print("TOP 3 DA TURMA")
    print("----------------------------------------")

    ranking_alunos = sorted(
        alunos,
        key=lambda aluno: aluno["nota"],
        reverse=True
    )

    quantidade_top = min(3, len(ranking_alunos))

    for i in range(quantidade_top):

        aluno = ranking_alunos[i]

        print(
            f"{i + 1}º "
            f"{aluno['nome']} "
            f"{aluno['nota']:.2f}"
        )

    print("========================================")


# ============================================
# MENU PRINCIPAL
# ============================================

def menu():

    while True:

        print("\n========================================")
        print("SISTEMA DE ANÁLISE DE NOTAS")
        print("========================================")

        print("1 - Cadastrar alunos")
        print("2 - Listar alunos")
        print("3 - Exibir estatísticas da turma")
        print("4 - Mostrar alunos acima da média")
        print("5 - Mostrar distribuição das notas")
        print("6 - Mostrar ranking da turma")
        print("7 - Consultar aluno")
        print("8 - Alterar nota")
        print("9 - Gerar relatório completo")
        print("10 - Sair")

        opcao = input("\nDigite uma opção: ").strip()

        if opcao == "1":

            cadastrar_alunos()

        elif opcao == "2":

            listar_alunos()

        elif opcao == "3":

            estatisticas()

        elif opcao == "4":

            alunos_acima_media()

        elif opcao == "5":

            distribuicao_notas()

        elif opcao == "6":

            ranking()

        elif opcao == "7":

            consultar_aluno()

        elif opcao == "8":

            alterar_nota()

        elif opcao == "9":

            gerar_relatorio_completo()

        elif opcao == "10":

            print("\nPrograma encerrado.")
            print("Até mais!")

            break

        else:

            print("\nErro: opção inválida.")


# ============================================
# INÍCIO DO PROGRAMA
# ============================================

menu()
