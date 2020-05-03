def test_"El primer juego de la la Biblioteca es el CarlosDuty":
  expect(Biblioteca.juegos.shift).to be CarlosDuty


def test_"El segundo juego de la Biblioteca es TimbaElLeon" :
  expect(Biblioteca.juegos.shift).to be TimbaElLeon


def test_"El tercer juego de la Biblioteca es Metroide" :
  expect(Biblioteca.juegos.shift).to be Metroide


def test_"La Biblioteca tiene únicamente esos tres juegos" :
  expect(Biblioteca.juegos.empty?).to be True

