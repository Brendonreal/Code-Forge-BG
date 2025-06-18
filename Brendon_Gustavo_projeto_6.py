#cores
verde = '\033[92m'
azul = '\033[94m'
amarelo = '\033[93m'
magenta = '\033[95m'
ciano = '\033[96m'
vermelho = '\033[91m'
CorNormal = '\033[0m'

AbasdeJogadores = []
AbasdeJogos = []

def cadastrar_jogador():
    print(f"{verde}Cadastrar Jogador")
    NomedoJogador = str(input(f"Digite o nome do jogador: "))
    Idade = int(input(f"Digite a idade do jogador: "))
    JogoQueIraParticipar = str(input(f"Qual jogo ele participará: "))
    jogadores = {
        "Jogador": NomedoJogador,
        "Idade": Idade,
        "Jogo_que_irá_participar": JogoQueIraParticipar,
        "Cadastrado": True
    }
    AbasdeJogadores.append(jogadores)
    print(f'Jogador cadastrado com sucesso⚽⚾🏀{CorNormal}')

def Cadastrar_Jogo():
    print(f"{azul}Cadastrar Jogo")
    NomedoJogo = str(input(f"Digite o nome do jogo: "))
    Jogo = str(input(f"Digite o jogo: "))
    jogo = {
        "Jogo": NomedoJogo,
        "jogo": Jogo,
        "Cadastrado": True
    }
    AbasdeJogos.append(jogo)
    print(f'Jogo cadastrado com sucesso🥅⛳{CorNormal}')

def Ver_Jogo():
    print(f"{amarelo}Ver Jogos")
    if len(AbasdeJogos) == 0:
        print(f"🙄 Nenhum jogo cadastrado.🙄 \n")
        return
    ConsultarVerdadeiro = 1
    for registrodejogo in AbasdeJogos:
        status = "✅" if registrodejogo['Cadastrado'] else "❌"
        print(f"[{ConsultarVerdadeiro}] Jogo: {registrodejogo['Jogo']} "
              f"| jogo: {registrodejogo['jogo']} | Status: {status}")
        ConsultarVerdadeiro += 1
    print()

def Ver_Jogadores():
    print(f"{magenta} Ver Jogadores")
    if len(AbasdeJogadores) == 0:
        print(f"🙄 Nenhum jogador cadastrado.🙄 \n")
        return
    ConsultarVerdadeiro = 1
    for registrodejogador in AbasdeJogadores:
        status = "✅" if registrodejogador['Cadastrado'] else "❌"
        print(f"[{ConsultarVerdadeiro}] Jogador: {registrodejogador['Jogador']} | Idade: {registrodejogador['Idade']} |"
              f" Jogo que irá participar: {registrodejogador['Jogo_que_irá_participar']} | Status: {status}")
        ConsultarVerdadeiro += 1
    print()

def Marcacomo_Acontecido():
    print(f"{ciano} Marca como Acontecido")
    if len(AbasdeJogos) == 0:
        return
    try:
        Ver_Jogo()
        numero = int(input(f"Digite o número do jogo para mostrar que já aconteceu: "))
        indice = numero - 1
        if 0 <= indice < len(AbasdeJogos):
            print(f"Descrição: {AbasdeJogos[indice]['Jogo']}")
            AbasdeJogos[indice]["Já aconteceu"] = True
            print(f"✅ Jogo marcado como já acontecido ✅\n")
        else:
            print(f"⚠ Número inválido.⚠ \n")
    except ValueError:
        print(f"⚠ Entrada inválida. Digite um número. ⚠\n{CorNormal}")

def exibir_menu():
    while True:
        print("\n\033[1m=== Sistema de Gerenciamento de Jogos e Jogadores ===\033[0m")
        print(f"{verde}1. Cadastrar Jogador")
        print(f"{azul}2. Cadastrar Jogo")
        print(f"{amarelo}3. Ver Jogo")
        print(f"{magenta}4. Ver Jogadores")
        print(f"{ciano}5. Anotar Resultados")
        print(f"{vermelho}6. Sair")
        escolha = str(input("Escolha uma opção: "))
        if escolha == "1":
            cadastrar_jogador()
        elif escolha == "2":
            Cadastrar_Jogo()
        elif escolha == "3":
            Ver_Jogo()
        elif escolha == "4":
            Ver_Jogadores()
        elif escolha == "5":
            Marcacomo_Acontecido()
        elif escolha == "6":
            print(f"{vermelho}Saindo do sistema.{CorNormal}")
            break
        else:
            print(f"{vermelho}⚠ Opção invalida. tente novamente. ⚠\n{CorNormal}")

exibir_menu()
