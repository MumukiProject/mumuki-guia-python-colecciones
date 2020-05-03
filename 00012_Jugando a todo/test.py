def test_"Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide" :
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]


def test_"Jugar a todo baja un punto la dificultad a CarlosDuty y sube en 5 la de TimbaElLeon" :
  Biblioteca.jugar_a_todo!
  expect(CarlosDuty.dificultad).to eq 29.5
  expect(TimbaElLeon.dificultad).to eq 30
