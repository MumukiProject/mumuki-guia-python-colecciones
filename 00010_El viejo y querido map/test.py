def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"La dificultad violenta del único juego violento es 30" :
  expect(Biblioteca.dificultad_violenta).to eq [30]


def test_"Si CarlosDuty no estuviera en la Biblioteca no habría dificultad violenta" :
  Biblioteca.juegos.shift
  expect(Biblioteca.dificultad_violenta).to eq []
