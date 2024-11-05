class Chatbot:
    def  __init__(self):
        self.options =(
            "inicio": {
                "mensaje": "Bienvenidos al chatbot ¿En qué te puedo ayudar?"
                "opiciones":[
                    "1. Productos",
                    "2. Contactos",
                    "3. Sucursales"
                    "4. Horario de atención"
                    "5. Descuento"
                ]
            },


            "Productos":{
                "1. Collares",
                "2. Aritos",
                "3. Anillos",
                "4. Pulseras",
                "5. Lentes"
            },


            "Collares":{
                "1. Dorado"
                "2. Plateado"
                "3. Bronce"
                "4. Rosado"
            },
        )

        self.respuestas={
            "precio.collar": "20.000",
            "precios.aritos": "$12.000",
            "precio.anillos": "$9.000",
            "precios.pulseras": "$15.000",
            "precios.lentes": "$22.000"
        }

def mostrar_menu(self):
        try:
            if self.estado_actual not in self.options:
                raise KeyError(f"Estado no válido: {self.estado_actual}")

            menu_actual = self.options[self.estado_actual]
            
            print("\n" + "="*50)
            print("\n🏫 " + menu_actual["mensaje"])
            print("\n📋 Opciones disponibles:")
            for opcion in menu_actual["opciones"]:
                print("  " + opcion)
            
            print("\n" + "="*50)
            print("(Ingresa 'q' para salir)")
            
        except KeyError as e:
            print(f"\nError: {e}")
            self.estado_actual = "inicio"
            print("Regresando al menú principal...")
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, contacta al administrador del sistema.")

    def procesar_entrada(self, opcion):
        """Procesa la entrada del usuario y actualiza el estado"""
        try:
            # Convertir la entrada a un número (si es posible)
            opcion = opcion.strip()
            
            # Verificar si la opción es válida para el menú actual
            opciones_validas = len(self.options[self.estado_actual]["opciones"])
             if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > opciones_validas:
                print("\n❌ Opción no válida. Por favor, elige un número entre 1 y", opciones_validas)
                return

            opcion = int(opcion)
            
            # Procesar según el estado actual
            if self.estado_actual == "inicio":
                if opcion == 1:
                    self.estado_actual = "secciones"
                elif opcion == 2:
                    print("\n📝 Información de Admisiones:")
                    print(self.respuestas["admisiones"])
                elif opcion == 3:
                    print("\n📞 Información de Contacto:")
                    print(self.respuestas["contacto"])
                elif opcion == 4:
                    print("\n🕒 Horario de Atención:")
                    print(self.respuestas["horario_atencion"])

            #RESPUESTAS SECCIONES

            elif self.estado_actual == "secciones":
                if opcion == 1:
                    self.estado_actual = "kinder"
                elif opcion == 2:
                    self.estado_actual = "primary"
                elif opcion == 3:
                    self.estado_actual = "middle"
                elif opcion == 4:
                    self.estado_actual = "senior"
                elif opcion == 5:  self.estado_actual = "inicio"

            #RESPUESTAS POR AREAS
                    
            elif self.estado_actual in ["kinder", "primary", "middle", "senior"]:
                if opcion == 1:  # Jornada
                    print(f"\n🕒 Jornada {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_jornada"])
                elif opcion == 2:  # Edades/Actividades/Electivas
                    if self.estado_actual == "kinder":
                        print("\n👶 Edades:")
                        print(self.respuestas["kinder_edades"])
                    elif self.estado_actual == "senior":
                        print("\n📚 Electivas y Orientativas:")
                        print(self.respuestas["senior_electivas"])
                    else:
                        print(f"\n📋 Actividades {self.estado_actual.capitalize()}:")
                        print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 3:  # Actividades
                    print(f"\n🎯 Actividades {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 4:  # Volver a secciones
                    self.estado_actual = "secciones"
                elif opcion == 5:  # Volver al inicio
                    self.estado_actual = "inicio"
                    
        except Exception as e:
            print(f"\n❌ Error procesando la opción: {e}")
            print("Por favor, intenta nuevamente.")
 def ejecutar(self):
        print("\n¡Bienvenido al ChatBot del Day School! 🎓")
        
        while True:
            self.mostrar_menu()
            opcion = input("\n➤ Ingresa el número de la opción deseada: ").strip()
            
            if opcion.lower() == 'q':
                print("\n¡Gracias por usar nuestro ChatBot! ¡Hasta pronto! 👋")
                break
                
            self.procesar_entrada(opcion)

# Ejemplo de uso
if __name__ == "__main__":
    bot = ChatBot()
    bot.ejecutar()