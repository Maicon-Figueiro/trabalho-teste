from Pessoa import Pessoa

def find_pessoa_by_cpf(list_of_peoples: list[Pessoa], cpf: str) -> Pessoa:#apenas pesquisa pessoas pelo cpf
    for pessoa in list_of_peoples:
        if pessoa.CPF == cpf:
            return pessoa
    return None