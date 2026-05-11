class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_nome(self, nome):
        if len(nome) != 0:
            self.__nome  = nome
        else:
            raise ValueError
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def __str__(self):
        return f'A playlist {self.get_nome()} tem a descrição "{self.get_descricao()}" e id: {self.get_id()}'


class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_titulo(self, titulo):
        if len(titulo) != 0:
            self.__titulo = titulo
        else:
            raise ValueError
        self.__titulo = titulo
    def set_artista(self, artista):
        if len(artista) != 0:
            self.__artista = artista
        else:
            raise ValueError
    def set_album(self, album):
        if len(album) != 0:
            self.__album = album
        else:
            raise ValueError
    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    def __str__(self):
        return f'A música {self.get_titulo()}, de {self.get_artista()} e do álbum {self.get_album()} tem id: {self.get_id()}'


class PlayListItem:
    def __init__(self, id, idPlaylist, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlaylist(idPlaylist)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)
    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_idPlaylist(self, idPlaylist):
        self.__idPlaylist = idPlaylist
    def set_idMusica(self, idMusica):
        self.__idMusica = idMusica
    def set_sequencia(self, sequencia):
        self.__sequencia = sequencia
    def get_id(self):
        return self.__id
    def get_idPlaylist(self):
        return self.__idPlaylist
    def get_idMusica(self):
        return self.__idMusica
    def get_sequencia(self):
        return self.__sequencia
    def __str__(self):
        return f'A música de id: {self.get_id()} vai para a playlist de id {self.get_idPlaylist()} como sequência: {self.get_sequencia()}, esse item terá id: {self.get_id()}'


class PlayListUI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = PlayListUI.menu()
            if op == 1: 
                PlayListUI.inserir_playlist()
            if op == 2: 
                PlayListUI.listar_playlist()
            if op == 3: 
                PlayListUI.atualizar_playlist()
            if op == 4: 
                PlayListUI.excluir_playlist()
            if op == 5: 
                PlayListUI.inserir_musica()
            if op == 6: 
                PlayListUI.listar_musica()
            if op == 7: 
                PlayListUI.atualizar_musica()
            if op == 8: 
                PlayListUI.excluir_musica()
            if op == 9: 
                PlayListUI.inserir_item()
            if op == 10:
                PlayListUI.listar_itens_playlist()

    @staticmethod
    def menu():
        print('1 - Inserir playlist  2 - Listar playlist  3 - Atualizar playlist  4 - Excluir playlist  5 - Inserir música  6 - Listar música  7 - Atualizar música  8 - Excluir música  9 - Inserir item playlist  10 - Listar itens da playlist  11 - Sair')
        return int(input('Escolha: '))

    @classmethod
    def inserir_playlist(cls):
        id = int(input('Id da playlist: '))
        nome = input('Nome: ')
        descricao = input('Descrição: ')

        x = PlayList(id, nome, descricao)
        cls.playlists.append(x)

        print('Playlist inserida')

    @classmethod
    def listar_playlist(cls):
        if len(cls.playlists) == 0:
            print('Nenhuma playlist cadastrada')
        else:
            for x in cls.playlists:
                print(x)

    @classmethod
    def atualizar_playlist(cls):
        PlayListUI.listar_playlist()

        id = int(input('Informe o id da playlist: '))
        for x in cls.playlists:
            if x.get_id() == id:
                cls.playlists.remove(x)

                nome = input('Novo nome: ')
                descricao = input('Nova descrição: ')

                novo = PlayList(id, nome, descricao)
                cls.playlists.append(novo)

                print('Playlist atualizada')

    @classmethod
    def excluir_playlist(cls):
        PlayListUI.listar_playlist()

        id = int(input('Informe o id da playlist: '))
        for x in cls.playlists:
            if x.get_id() == id:
                cls.playlists.remove(x)

                print('Playlist removida')

    @classmethod
    def inserir_musica(cls):
        id = int(input('Id da música: '))
        titulo = input('Título: ')
        artista = input('Artista: ')
        album = input('Álbum: ')

        x = Musica(id, titulo, artista, album)
        cls.musicas.append(x)

        print('Música inserida')

    @classmethod
    def listar_musica(cls):
        if len(cls.musicas) == 0:
            print('Nenhuma música cadastrada')
        else:
            for x in cls.musicas:
                print(x)

    @classmethod
    def atualizar_musica(cls):

        PlayListUI.listar_musica()

        id = int(input('Informe o id da música: '))
        for x in cls.musicas:
            if x.get_id() == id:
                cls.musicas.remove(x)

                titulo = input('Novo título: ')
                artista = input('Novo artista: ')
                album = input('Novo álbum: ')

                novo = Musica(id, titulo, artista, album)
                cls.musicas.append(novo)

                print('Música atualizada')

    @classmethod
    def excluir_musica(cls):
        PlayListUI.listar_musica()

        id = int(input('Informe o id da música: '))
        for x in cls.musicas:
            if x.get_id() == id:
                cls.musicas.remove(x)

                print('Música removida')

    @classmethod
    def inserir_item(cls):
        id = int(input('Id do item: '))
        idPlaylist = int(input('Id da playlist: '))
        idMusica = int(input('Id da música: '))
        sequencia = int(input('Sequência: '))

        x = PlayListItem(id, idPlaylist, idMusica, sequencia)
        cls.itens.append(x)

        print('Item inserido')

    @classmethod
    def listar_itens_playlist(cls):
        idPlaylist = int(input('Informe o id da playlist: '))

        for x in cls.itens:
            if x.get_idPlaylist() == idPlaylist:
                idMusica = x.get_idMusica()

                for y in cls.musicas:
                    if y.get_id() == idMusica:
                     print(y)

PlayListUI.main()