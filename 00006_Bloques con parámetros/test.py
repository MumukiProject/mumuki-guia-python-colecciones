def test_"Si se evalúa jugar_a_timba con 120 minutos, la dificultad es 27" :
  jugar_a_timba.call(120)
  expect(TimbaElLeon.dificultad).to be 27
