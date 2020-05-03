it "Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide"  do
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]
end

it "En la Biblioteca no hay mucha violencia porque TimbaElLeon no es violento"  do
  expect(Biblioteca.mucha_violencia?).to be false
end

it "La Biblioteca es muy difícil porque CarlosDuty y Metroide tienen más de 25 puntos de dificultad"  do
  expect(Biblioteca.muy_dificil?).to eq true
end