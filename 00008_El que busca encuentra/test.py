def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"CarlosDuty es más difícil que 10" :
  expect(Biblioteca.juego_mas_dificil_que(10)).to eq CarlosDuty


def test_"Metroide es más difícil que 90" :
  expect(Biblioteca.juego_mas_dificil_que(90)).to eq Metroide


def test_"Ningún juego es más difícil que 110" :
  expect(Biblioteca.juego_mas_dificil_que(110)).to eq None
