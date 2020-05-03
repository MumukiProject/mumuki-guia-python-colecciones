def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"Si se borra CarlosDuty la Biblioteca queda con dos juegos":
  Biblioteca.borrar_juego!(CarlosDuty)
  expect(Biblioteca.juegos.include?(CarlosDuty)).to be False
  expect(Biblioteca.juegos.size()).to eq 2
  expect(Biblioteca.puntos()).to eq 0
  Biblioteca.juegos.push(CarlosDuty)


def test_"Si se adquiere otro juego se agrega a los juegos y suma puntos" :
  Biblioteca.adquirir_juego!(OtroJuego)
  expect(Biblioteca.juegos.include?(OtroJuego)).to be True
  expect(Biblioteca.puntos()).to eq 150


def test_"La Biblioteca no es completa al iniciar":
  expect(Biblioteca.completa?).to be False


def test_"Si se adquieren suficientes juegos la Biblioteca es completa":
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  expect(Biblioteca.completa?).to be False
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  expect(Biblioteca.completa?).to be True
  7.times { Biblioteca.juegos.delete(OtroJuego) }


def test_"CarlosDuty es recomendable si no está en la biblioteca":
  expect(Biblioteca.juego_recomendable?(CarlosDuty)).to be False
  Biblioteca.borrar_juego!(CarlosDuty)
  expect(Biblioteca.juego_recomendable?(CarlosDuty)).to be True


def test_"TimbaElLeon no es recomendable porque no es violento":
  expect(Biblioteca.juego_recomendable?(TimbaElLeon)).to be False
