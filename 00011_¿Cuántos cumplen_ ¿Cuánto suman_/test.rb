it "Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide"  do
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]
end

it "El promedio de violencia es 155"  do
  expect(Biblioteca.promedio_de_violencia).to eq 30
end

it "El promedio de violencia es 125 si agrego un juego violento de dificultad 95"  do
  Biblioteca.juegos.push(JuegoViolento)
  expect(Biblioteca.promedio_de_violencia).to eq 62.5
end