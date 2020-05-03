it "Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide"  do
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]
end

it "La dificultad violenta del único juego violento es 30"  do
  expect(Biblioteca.dificultad_violenta).to eq [30]
end

it "Si CarlosDuty no estuviera en la Biblioteca no habría dificultad violenta"  do
  Biblioteca.juegos.shift
  expect(Biblioteca.dificultad_violenta).to eq []
end