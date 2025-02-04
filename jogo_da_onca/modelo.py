class Peca:
    pass


class Cachorro(Peca):
    
    def __repr__(self) -> str:
        return 'C'


class Onca(Peca):
    
    def __repr__(self) -> str:
        return 'O'


class Tabuleiro:
    """
    Representação do tabuleiro de jogo, responsável pela disposição e
    movimentação correta das peças.
    """
    def __init__(self):
        self.estado = [Cachorro() for _ in range(12)]
        self.estado += [Onca(), Cachorro(), Cachorro()]
        self.estado += [None for _ in range(16)]
        self.turno_onca = True
    
    def __repr__(self) -> str:
        cnx_pares = '\n'.join((
                '|\\ | /|\\ | /|',
                '| \\|/ | \\|/ |',

            ))
        cnx_impares = '\n'.join((
                '| /|\\ | /|\\ |',
                '|/ | \\|/ | \\|',
            ))

        def string(obj: object):
            if obj is None:
                return '+'

            return str(obj)

        def linha(n: int):
            i = n * 5
            return '--'.join(map(string, self.estado[i:(i + 5)]))

        return '\n'.join((
            linha(0),
            cnx_pares,
            linha(1),
            cnx_impares,
            linha(2),
            cnx_pares,
            linha(3),
            cnx_impares,
            linha(4),
            ((' ' * 5) + '/|\\' + (' ' * 5)).center(13),
            ('-'.join(map(string, self.estado[25:28]))).center(13),
            '  /  |  \\  '.center(13),
            ('---'.join(map(string, self.estado[28:31]))).center(13),
        ))

    @classmethod
    def eh_vizinho(cls, casa_a: int, casa_b: int) -> bool:
        """
        Verifica se duas casas são "vizinhas", isto é, se é permitida a
        movimentação entre elas. Duas casas iguais não são consideradas
        vizinhas.
        
        Não considera o movimento de "captura" da onça sobre um cachorro.
        """
        if casa_b == casa_a:
            return False

        if casa_a > casa_b:
            casa_a, casa_b = casa_b, casa_a
        
        if casa_a == 22 and (24 < casa_b < 28):
            return True

        if casa_a < 25 and casa_b > 24:
            return False

        def coord(casa: int, toca=False):
            temp = 3 if toca else 5
            temp_casa = casa - 25 if toca else casa
            return temp_casa % temp, temp_casa // temp

        a_x, a_y = coord(casa_a, casa_a > 25)
        b_x, b_y = coord(casa_b, casa_b > 25)

        if ((a_x == b_x) and ((a_y - b_y) in (1, -1))) or \
                ((a_y == b_y) and ((a_x - b_x) in (1, -1))):
            return True

        if casa_a > 19 or (casa_a % 2) or (casa_b % 2):
            return False

        return ((casa_a % 5 < 4) and (casa_b == (casa_a + 6))) or \
            ((casa_a % 5 > 0) and (casa_b == (casa_a + 4)))
    
    @classmethod
    def movimento_valido(cls, estado: list, turno_onca: bool, origem: int,
                         destino: int) -> bool:
        """
        Avalia se um movimento envolvendo duas casas, dado um estado de jogo,
        é considerado válido sendo levada para uma posição destino vazia e ao
        redor da origem no seu devido turno.
        """
        if turno_onca and not isinstance(estado[origem], Onca):
            return False

        peca_destino = estado[destino]
        return peca_destino is None and cls.eh_vizinho(origem, destino)
    
    def eh_captura(self, casa_a: int, casa_b: int) -> bool:
        """
        Verifica se a passagem de `casa_a` para `casa_b` é um movimento válido
        de captura da onça sobre um cachorro.
        """
        if not self.turno_onca or casa_a == casa_b:
            return False
        
        if casa_a > casa_b:
            casa_a, casa_b = casa_b, casa_a
        
        # TODO: implementar restante da função

    def mover(self, origem: int, destino: int):
        """
        Realiza a movimentação de uma peça, conforme a posição de `origem` e
        `destino` informadas.

        Tanto `origem` e `destino` devem ser números inteiros, representando a
        posição da casa no tabuleiro, sendo contadas em ordem de leitura (de
        cima para baixo, esquerda para direita) a partir de 0.
        
        Todo movimento inválido será acusado por um erro do tipo
        `AssertionError`.

        Todo movimento válido será realizado, alternando para o turno do
        próximo jogador.
        """
        estado = self.estado
        assert self.movimento_valido(
            estado,
            self.turno_onca,
            origem,
            destino,
        )

        # TODO: adicionar condição da onça capturando cachorro

        estado[origem], estado[destino] = estado[destino], estado[origem]
        self.turno_onca = not self.turno_onca
