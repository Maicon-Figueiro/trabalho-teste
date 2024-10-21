import sys
import Utils
from Pessoa  import *
from Partido import Partido
from Eleicao import Eleicao
from Urna    import Urna
from Votacao import Votacao
def main():
    if len(sys.argv) < 3: #verifica a quantidade de parÂmetros no terminal ao rodar
        print("Faltam argumentos")
        sys.exit(1)
        
    eleicao_path = sys.argv[1]
    urnas_path = sys.argv[2:]
        
    # print(f"Eleição: {eleicao_path}")
    # print(f"Urna: {urnas_path}")
    pessoas, candidatos, partidos = read_file_eleicao(eleicao_path)
    eleicao = Eleicao(candidatos, partidos)
    read_file_urnas(urnas_path, eleicao, candidatos)

def read_file_eleicao(file_path):
    pessoas = []
    candidatos= []
    partidos = []
    with open(file_path, "r", encoding="UTF-8") as file:
        LEFT  = 1
        RIGHT = 0

        for linha in file.readlines()[1:]:
            linha_splited = linha.split(":")
            command = linha_splited[RIGHT]
            atributes = linha_splited[LEFT].split(",")
            
            strip_list(atributes)

            if command == "adicionar_partido":
                partidos.append(Partido(atributes[1], atributes[0], atributes[2]))

            if command == "adicionar_pessoa":
                pessoas.append(Pessoa(atributes[0], atributes[1], atributes[2]))

            if command == "adicionar_candidato":
                pessoa = Utils.find_pessoa_by_cpf(pessoas, atributes[0])
                atributes[4] = atributes[4]

                if pessoa: #se for achada no banco de dados 
                    if atributes[4] == "DepFederal":
                        candidatos.append(DepFederal(pessoa.nome, pessoa.CPF, pessoa.data_nascimento, atributes[1], atributes[2], atributes[3]))
                    elif atributes[4] == "DepEstadual":
                        candidatos.append(DepEstadual(pessoa.nome, pessoa.CPF, pessoa.data_nascimento, atributes[1], atributes[2], atributes[3]))
                    elif atributes[4] == "Senador":
                        candidatos.append(Senador(pessoa.nome, pessoa._CPF, pessoa.data_nascimento, atributes[1], atributes[2], atributes[3]))
                    elif atributes[4] == "Governador":
                            candidatos.append(Governador(pessoa.nome, pessoa._CPF, pessoa.data_nascimento, atributes[1], atributes[2], atributes[3]))
                    elif atributes[4] == "Presidente":
                            candidatos.append(Presidente(pessoa.nome, pessoa._CPF, pessoa.data_nascimento, atributes[1], atributes[2], atributes[3]))
    return pessoas, candidatos, partidos

def read_file_urnas(file_paths, eleicao, candidatos):
    urnas_id = {}
    for file_path in file_paths:  
        with open(file_path, 'r', encoding="UTF-8") as file:
            for linha in file.readlines():
                attributes = (linha.split(":")[1].split(','))
                strip_list(attributes)
                print(attributes)
                if attributes[0] not in urnas_id:
                    urnas_id[attributes[0]] = Urna(attributes[0], eleicao)
                else:
                    try:    
                        urnas_id[attributes[0]].votar(attributes[2:]) #terminar
                    except:
                        pass

    print(Votacao.total_de_eleitores)


def strip_list(list):#apenas eliminas os espaços em branco tornando o dado mais limpo
    for i in range(len(list)):
        list[i] = list[i].strip()

if __name__ == "__main__":
    main()
    
#falta fazer os arquivos de saída 
#criar uma função que cria os arquivos de saída 
#open\ (saida) método with 

