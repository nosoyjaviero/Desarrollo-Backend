class Automovil:
     def __init__(self, modelo, marca, color,año, pasajeros=1 ):
      self.modelo=modelo
      self. marca =  marca
      self.color= color
      self._estado='en_reposo'
      self._motor= Motor(cilindros=4)
      self.pasajeros=pasajeros
      self.chocado=False
      self.año=año
      
     def acelerar (self, tipo='despacio'):
        if tipo=='despacio':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
            
        self._estado='en_movimiento'
        
     def auto_chocado(self, chocado):
         if chocado==True:
             self.chocado=True
        
          
        

class Motor:
    def __init__(self,cilindros, tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo=tipo;
        self._temperatura=0;
        
    def inyecta_gasolina(self,cantidad):
        pass
    
    
        
class llantas:
    def __init__(self,tipo,marca,agujeros=0,ponchada=False):
        self.tipo=tipo
        self.marca=marca
        self.agujeros=agujeros
        self.ponchada=ponchada
        
    def llantaPonchada(self,ponchada):
        if ponchada:
            self.ponchada=True
            print("Ir al mecanico a reparar")
            
    def AumentarAgujeros(self, agujeros):
        self.agujeros=agujeros
