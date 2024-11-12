class Chatbot:
    def  __init__(self):
        self.options [
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
        ]


        self.respuestas={
            "precio.collar" : "$9900",
            "precio.aritos" : "$5000",
            "precio.anillos" : "4500",
            "precio.pulseras": "8000",
            "precio.lentes" : "12000",
        }


    if self.estado_actual == "inicio":
                if opcion == 1:
                    self.estado_actual = "productos"
                elif opcion == 2:
                    print("\n📝 Información de Contactos:")
                    print(self.respuestas["contactos"])
                elif opcion == 3:
                    print("\n📞 Información de Sucursal:")
                    print(self.respuestas["sucursal"])
                elif opcion == 4:
                    print("\n🕒 Horario de Atención:")
                    print(self.respuestas["horario_atencion"])


            elif self.estado_actual == "Productos":
                if opcion == 1:
                    self.estado_actual = "Collar"
                elif opcion == 2:
                    self.estado_actual = "Aritos"
                elif opcion == 3:
                    self.estado_actual = "Pulsera"
                elif opcion == 4:
                    self.estado_actual = "Lentes"
                elif opcion == 5:
                    self.estado_actual = "Productos"


     
            elif self.estado_actual in ["Collares", "Aritos", "Pulsera", "Lentes"]:
                if opcion == 1:  # Jornada
                    print(f"\n🕒 Jornada {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_jornada"])
                elif opcion == 2:  # Edades/Actividades/Electivas
                    if self.estado_actual == "Collares":
                        print("\n👶 Edades:")
                        print(self.respuestas["kinder_edades"])
                    elif self.estado_actual == "Aritos":
                        print("\n📚 Electivas y Orientativas:")
                        print(self.respuestas["senior_electivas"])
                    else:
                        print(f"\n📋 Actividades {self.estado_actual.capitalize()}:")
                        print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 3:  # Actividades
                    print(f"\n🎯 Actividades {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 4:  # Volver a secciones
                    self.estado_actual = "Producto"
                elif opcion == 5:  # Volver al inicio
                    self.estado_actual = "inicio"