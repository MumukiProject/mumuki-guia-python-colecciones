def test_"CarlosDuty es violento" :
  expect(CarlosDuty.violento?).to be True


def test_"TimbaElLeon no es violento" :
  expect(!TimbaElLeon.violento?).to be True


def test_"Metroide inicialmente no es violento" :
  expect(!Metroide.violento?).to be True


def test_"Metroide se vuelve violento si se juega muchas veces" :
  5.times { Metroide.jugar!(10) }
  expect(Metroide.violento?).to be True


def test_"La dificultad inicial del CarlosDuty es 30" :
  expect(CarlosDuty.dificultad).to eq 30


def test_"CarlosDuty no tiene logros al empezar" :
  expect(CarlosDuty.cantidad_logros).to eq 0


def test_"Si se juega dos veces al CarlosDuty por menos de dos horas su dificultad sigue siendo 30" :
  CarlosDuty.jugar!(1)
  CarlosDuty.jugar!(1)
  expect(CarlosDuty.dificultad).to eq 30


def test_"Si se juega dos veces al CarlosDuty más de dos horas seguidas, su dificultad es 29" :
  CarlosDuty.jugar!(5)
  CarlosDuty.jugar!(7)
  expect(CarlosDuty.dificultad).to eq 29


def test_"La dificultad inicial de TimbaElLeon es 25":
  expect(TimbaElLeon.dificultad).to eq 25


def test_"La dificultad de TimbaElLeon aumenta en 20 puntos si se juega 20 horas" :
  TimbaElLeon.reiniciar_dificultad
  TimbaElLeon.jugar!(20)
  expect(TimbaElLeon.dificultad).to eq 45


def test_"La dificultad de Metroide es siempre 100":
  expect(Metroide.dificultad).to eq 100
  Metroide.jugar!(20)
  Metroide.jugar!(10)
  expect(Metroide.dificultad).to eq 100
