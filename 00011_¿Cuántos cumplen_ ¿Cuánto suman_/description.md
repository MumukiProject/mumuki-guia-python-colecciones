Volviendo a nuestra colección de alumnos. Ya preguntamos si todos aprobaron o si alguno aprobó utilizando `all?`y `any?`. ¿Y si queremos saber **cuántos** aprobaron? Usamos `count`:

```ruby
alumnos.count { |un_alumno| un_alumno.aprobo? }
```

`count` nos dice cuántos elementos de una colección cumplen la condición. Por otro lado, para calcular sumatorias tenemos el mensaje `sum`. Si queremos conocer la suma de todas las notas de los alumnos, por ejemplo, podemos hacer:

```ruby
alumnos.sum { |un_alumno| un_alumno.nota_en_examen }
```

> Veamos si se entiende: agregá a la `Biblioteca` el método `promedio_de_violencia`, cuyo valor sea la sumatoria de dificultad de los juegos violentos dividida por la cantidad de juegos violentos de la `Biblioteca`.