it "El primer juego de la la Biblioteca es el CarlosDuty" do
  expect(Biblioteca.juegos.shift).to be CarlosDuty
end

it "El segundo juego de la Biblioteca es TimbaElLeon"  do
  expect(Biblioteca.juegos.shift).to be TimbaElLeon
end

it "El tercer juego de la Biblioteca es Metroide"  do
  expect(Biblioteca.juegos.shift).to be Metroide
end

it "La Biblioteca tiene únicamente esos tres juegos"  do
  expect(Biblioteca.juegos.empty?).to be true
end
