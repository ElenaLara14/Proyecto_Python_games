{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "‼️‼️‼️🌍🌍🌍Bienvenidos al juego de preguntas de Geodrafía🌍🌍🌍‼️‼️‼️ \n",
      "\n",
      "\n",
      "📒 Reglas del Juego : \n",
      "\n",
      " - Te vamos a hacer preguntas que nos tendrás que responder. \n",
      " - Cada pregunta tiene una respuesta única y correcta. La podrás escribir tanto en Mayúsculas, Minúsculas y sin acentos. La respuesta es una única palabra\n",
      " - El jugador tiene un número limitado de intentos para responder correctamente a cada pregunta. \n",
      " - El juego sigue hasta que el jugador responda incorrectamente 3 de veces o haya respondido 5 preguntas correctamente.\n",
      " \n",
      "\n",
      "💪😎 EMPECEMOS \n",
      "\n",
      "\n",
      "Has respondido 'africa'. Esto es correcto ✅\n",
      "Has acertado, sigue jugando 👌🏻\n",
      "➖➖➖➖➖➖➖➖➖➖➖➖➖\n",
      "Has respondido 's'. Esto es incorrecto ❌, prueba otra vez\n",
      "➖➖➖➖➖➖➖➖➖➖➖➖➖\n",
      "Has respondido 'Ottawa'. Esto es incorrecto ❌, prueba otra vez\n",
      "➖➖➖➖➖➖➖➖➖➖➖➖➖\n",
      "Has respondido 'India'. Esto es correcto ✅\n",
      "Has acertado, sigue jugando 👌🏻\n",
      "➖➖➖➖➖➖➖➖➖➖➖➖➖\n",
      "Has respondido 'a'. Esto es incorrecto ❌, prueba otra vez\n",
      "➖➖➖➖➖➖➖➖➖➖➖➖➖\n",
      "\n",
      "💀💀💀¡¡¡PERDISTE!!!💀💀💀\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "from unidecode import unidecode\n",
    "\n",
    "print(f'‼️‼️‼️🌍🌍🌍Bienvenidos al juego de preguntas de Geodrafía🌍🌍🌍‼️‼️‼️ \\n\\n')\n",
    "\n",
    "print(f'📒 Reglas del Juego : \\n\\n - Te vamos a hacer preguntas que nos tendrás que responder. \\n - Cada pregunta tiene una respuesta única y correcta. La podrás escribir tanto en Mayúsculas, Minúsculas y sin acentos. La respuesta es una única palabra\\n - El jugador tiene un número limitado de intentos para responder correctamente a cada pregunta. \\n - El juego sigue hasta que el jugador responda incorrectamente 3 de veces o haya respondido 5 preguntas correctamente.\\n \\n')\n",
    "\n",
    "print('💪😎 EMPECEMOS \\n\\n')\n",
    "\n",
    "# Diccionario con preguntas y respuestas de geografía\n",
    "preguntas = {\n",
    "    \"¿Cuál es el río más largo del mundo?\": \"Nilo\",\n",
    "    \"¿En qué continente se encuentra el desierto del Sahara?\": \"África\",\n",
    "    \"¿Cuál es la capital de Australia?\": \"Canberra\",\n",
    "    \"¿Cuál es la montaña más alta del mundo?\": \"Everest\",\n",
    "    \"¿Cuál es el país más pequeño del mundo por superficie y población?\": \"Vaticano\",\n",
    "    \"¿Qué océano es el más grande del mundo?\": \"Pacífico\",\n",
    "    \"¿Cuál es el río más largo de América del Sur?\": \"Amazonas\",\n",
    "    \"¿En qué país se encuentra el desierto de Atacama?\": \"Chile\",\n",
    "    \"¿Cuál es la capital de Canadá?\": \"Ottawa\",\n",
    "    \"¿Cuál es el país más poblado del mundo?\": \"India\",\n",
    "    \"¿Qué país es conocido por sus relojes de cuco y chocolate?\": \"Suiza\",\n",
    "    \"¿Qué país tiene una bandera con una hoja de arce?\" : \"Canadá\",\n",
    "    \"¿Qué país es famoso por tener una ciudad llamada - Batman?\": \"Turquía\",\n",
    "    \"¿Qué país tiene una bandera con un círculo rojo en el centro de un campo blanco?\": \"Japón\"}\n",
    "\n",
    "# Variables para el seguimiento de respuestas correctas e incorrectas\n",
    "respuestas_correctas = 0\n",
    "respuestas_incorrectas = 0\n",
    "\n",
    "# Convertir el diccionario a una lista de tuplas para usar con random.choice\n",
    "lista_preguntas = list(preguntas.items())\n",
    "\n",
    "# Set para rastrear preguntas ya realizadas\n",
    "preguntas_realizadas = set()\n",
    "\n",
    "# Bucle principal del juego \n",
    " \n",
    "while respuestas_correctas <= 5 or respuestas_incorrectas <= 3:\n",
    "         # Seleccionar una pregunta aleatoria - Desempaquetamos tupla para crear variable pregunta y respuesta correcta\n",
    "        pregunta, respuesta_correcta = random.choice(lista_preguntas)\n",
    "\n",
    "        # Verificar la pregunta seleccionada en el set para que no se repita\n",
    "        if pregunta in preguntas_realizadas:\n",
    "            continue  # Si ya se ha hecho, saltar a la siguiente iteración\n",
    "\n",
    "    # Agregar la pregunta como realizada al set\n",
    "        preguntas_realizadas.add(pregunta)\n",
    "        \n",
    "        # Preguntamos al usuario\n",
    "        usuario = (input(pregunta)) ### se repiten preguntas \n",
    "    \n",
    "        if unidecode(respuesta_correcta).lower() == unidecode(usuario).lower(): # importar unidecode para que no falle por las tildes\n",
    "            respuestas_correctas += 1\n",
    "            print(f\"Has respondido '{usuario}'. Esto es correcto ✅\")\n",
    "            print(f\"Has acertado, sigue jugando 👌🏻\")\n",
    "            print(\"➖➖➖➖➖➖➖➖➖➖➖➖➖\")\n",
    "\n",
    "            if respuestas_correctas == 5:\n",
    "                print(\"🎉🎉🎉¡¡¡GANASTE!!!🎉🎉🎉\")\n",
    "                break\n",
    "\n",
    "        else:\n",
    "            print(f\"Has respondido '{usuario}'. Esto es incorrecto ❌, prueba otra vez\")\n",
    "            print(\"➖➖➖➖➖➖➖➖➖➖➖➖➖\")\n",
    "            respuestas_incorrectas += 1\n",
    "            if respuestas_incorrectas == 3:\n",
    "                print(\"\\n💀💀💀¡¡¡PERDISTE!!!💀💀💀\")\n",
    "                break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
