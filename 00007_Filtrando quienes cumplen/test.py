def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"CarlosDuty es el único juego violento" :
  expect(Biblioteca.juegos_violentos).to eq [CarlosDuty]
