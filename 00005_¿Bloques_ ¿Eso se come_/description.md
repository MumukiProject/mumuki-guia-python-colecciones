¡Pausa! :hand: Antes de continuar, necesitamos conocer a unos nuevos amigos: los _bloques_.

Los _bloques_ son **objetos** que representan un mensaje o una secuencia de envíos de mensajes, **sin ejecutar**, lista para ser evaluada cuando corresponda. La palabra con la que se definen los bloques en Ruby es _proc_. Por ejemplo, en este caso le asignamos un _bloque_ a `incrementador`:

```ruby
un_numero = 7
incrementador = proc { un_numero = un_numero + 1 }
```

Ahora avancemos un pasito: en este segundo ejemplo, al _bloque_ `{ otro_numero = otro_numero * 2 }` le enviamos el mensaje _call_, que le indica que **evalúe la secuencia de envíos de mensajes** dentro de él.

```ruby
otro_numero = 5
duplicador = proc { otro_numero = otro_numero * 2 }.call
```

¡Es hora de poner a prueba tu conocimiento! :open_mouth: Marcá las respuestas correctas: