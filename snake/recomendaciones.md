# Algunas recomendaciones

- Las clases por convencion empiezan con mayuscula. 
```python
class Board():
    pass
```

- Crear un archivo por clase.

- Hacer los nombres mas redundantes a pesar de que sean un poco mas largos. No importa, pero el que lea el codigo entiende mas rapido

```python
class Food():
    __foodx = 3 # Se entiende pero puede no quedar claro en codigos un poco mas complejos.
    __positionX = 3 # Aca se ve más rapido que es la posición en un eje de coordenadas cartesianas.
```

- Tener en cuenta la encapsulacion y el hecho de que las variable sean privadas a la clase
```python
class Food():
    __positionX = 0
    __positionY = 0

    def getPositionX(self):
        return self.__positionX

    # No es necesario ya que cuando se crea la fruta se le asigna una posición pero en caso de querer cambiar la variable a fuera de la clase si se usa este metodo especial
    def setPositionX(self, positionX): 
        self.__positionX = positionX
```

- En el metodo restart recomiendo simple mente no crear nuevas instancias llamando al init. Es mejor cambiar el nombre de este metodo y asignar una nueva posición a la fruta.

- Usando encapsulacion se puede sacar el metodo ate y crashedBoundaries de Snake. ¿Porque?
```python
def ate(self, brd, fd):
    if self.__snakeHeadPositionX == fd._food__foodx and self.__snakeHeadPositionY == fd._food__foody: # Esto usando los getters de Food y Snake se puede verificar en el tablero

        # Este es el metodo restart() de Food. Si fuera más complicado estariamos repitiendo codigo
        fd._food__foodx = round(random.randrange(0, brd._board__dis_width - self.__snake_block) / 10.0) * 10.0
        fd._food__foody = round(random.randrange(0, brd._board__dis_height - self.__snake_block) / 10.0) * 10.0
        self.__snake_length += 1 # Esto se puede poner como un metodo publico de snake
```

- El metodo update board nos mostrara las ventajas de la encapsulacion 

- Tener cuidado con la encapsulasión. Porque una fruta debe recibir un tablero y una culebra? Se entiende que la fruta **tiene** un tablero y una culebra. Semanticamente es más correcto pensar que el tablero tiene una culebra y una fruta.

```python
class Food(): 
def __init__(self, brd, snk): 

    # Fijese que brd y snk no se usan ni son relevantes por eso se pueden quitar para evitar errores semanticos.
    self.__positionX = round(random.randrange(0, brd._board__dis_width - snk._snake__snake_block) / 10.0) * 10.0
    self.__positionY = round(random.randrange(0, brd._board__dis_height - snk._snake__snake_block) / 10.0) * 10.0
```