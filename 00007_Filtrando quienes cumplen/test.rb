it "Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide"  do
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]
end

it "CarlosDuty es el único juego violento"  do
  expect(Biblioteca.juegos_violentos).to eq [CarlosDuty]
end