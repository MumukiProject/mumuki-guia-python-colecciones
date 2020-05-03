def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"El promedio de violencia es 155" :
  expect(Biblioteca.promedio_de_violencia).to eq 30


def test_"El promedio de violencia es 125 si agrego un juego violento de dificultad 95" :
  Biblioteca.juegos.push(JuegoViolento)
  expect(Biblioteca.promedio_de_violencia).to eq 62.5
