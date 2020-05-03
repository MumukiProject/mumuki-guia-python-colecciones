it "Los juegos de la Biblioteca son CarlosDuty, TimbaElLeon y Metroide"  do
  expect(Biblioteca.juegos).to eq [CarlosDuty, TimbaElLeon, Metroide]
end

it "Si se borra CarlosDuty la Biblioteca queda con dos juegos" do
  Biblioteca.borrar_juego!(CarlosDuty)
  expect(Biblioteca.juegos.include?(CarlosDuty)).to be false
  expect(Biblioteca.juegos.size()).to eq 2
  expect(Biblioteca.puntos()).to eq 0
  Biblioteca.juegos.push(CarlosDuty)
end

it "Si se adquiere otro juego se agrega a los juegos y suma puntos"  do
  Biblioteca.adquirir_juego!(OtroJuego)
  expect(Biblioteca.juegos.include?(OtroJuego)).to be true
  expect(Biblioteca.puntos()).to eq 150
end

it "La Biblioteca no es completa al iniciar" do
  expect(Biblioteca.completa?).to be false
end

it "Si se adquieren suficientes juegos la Biblioteca es completa" do
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  expect(Biblioteca.completa?).to be false
  Biblioteca.adquirir_juego!(OtroJuego)
  Biblioteca.adquirir_juego!(OtroJuego)
  expect(Biblioteca.completa?).to be true
  7.times { Biblioteca.juegos.delete(OtroJuego) } 
end

it "CarlosDuty es recomendable si no está en la biblioteca" do
  expect(Biblioteca.juego_recomendable?(CarlosDuty)).to be false
  Biblioteca.borrar_juego!(CarlosDuty)
  expect(Biblioteca.juego_recomendable?(CarlosDuty)).to be true
end

it "TimbaElLeon no es recomendable porque no es violento" do
  expect(Biblioteca.juego_recomendable?(TimbaElLeon)).to be false
end