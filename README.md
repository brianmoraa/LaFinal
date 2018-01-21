#Videojuego La Final con Q-Learning
#Código fuete originalmente modificado para el propósito de este trabajo: https://github.com/hasanIqbalAnik/q-learning-python-example


Descripción del Problema

  En este juego hay varios tiros de penal y la idea es de que el arquero aprenda a tapar.
  
  El círculo vacío representa el balón y el cuadrado en negrita representa el arquero.
  
  El ancho del arco es cinco cuadrados (de los que se ven en la figura) y la pelota puede ser 
  
  pateada máximo dos cuadrados fuera del arco (de ambos lados). La distancia del arco a donde la
  
  pelota es pateada no tiene mayor relevancia.

  
  Reglas
    
    1. Cuando el arquero ataja, se ganan dos puntos (+2)
    
    2. Cuando el arquero no ataja, se pierden dos puntos (−2)
    
    3. Cuando la pelota es disparada fuera del arco y el arquero se mueve a ese lugar, se pierde un punto (−1).
      	
        Tenga en cuenta que el arquero sí podría moverse, pero no fuera del arco (vea el punto 4).
    
    4. Cuando la pelota es disparada fuera del arco y el arquero no se sale del arco, se gana un punto (+1)
    
    5. Los disparos del balón son realizados enseguida uno después del otro. Esto quiere decir que el arquero, luego de un disparo, no     
        se posiciona al centro del arco sino que trata de atajar el siguiente disparo desde el lugar en el que quedó luego del primer
      
      disparo.


      | | | | |ð| | | | |
      | | | | | | | | | |
      | | | | | | | | | |
      | | | | | | | | | |
      | | | | | | | | | |
      | | | | | | | | | |
      | | ║ | |▄| | ║ | |


Desarrolladores

  Daniel Gomez Jaramillo
  
  Brian Mora Aguirre
  
  Mauricio Pesantez Guzñay
  
  David Valladarez Muñoz


Materia 
  
  Machine Learning - Universidad de Cuenca


Docente responsable
  
  Ing. Ángel Vazquez P.
