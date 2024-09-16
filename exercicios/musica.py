class Musica:
    nome = ''
    artista = ''
    duracao = int


musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355
print(musica1.nome)

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183
print(musica2.artista)

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234
print(musica3.duracao)

print(f'\nMúsica: {
      musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
