def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"En la Biblioteca no hay mucha violencia porque TimbaElLeon no es violento" :
  expect(Biblioteca.mucha_violencia?).to be False


def test_"La Biblioteca es muy difícil porque CarlosDuty y Metroide tienen más de 25 puntos de dificultad" :
  expect(Biblioteca.muy_dificil?).to eq True
