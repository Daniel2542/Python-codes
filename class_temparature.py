#class to convert temperature
class Temperature:
    def __init__(self,temperature):
        self.temperature=temperature
        
    def convert_celcius(self):
        return(self.temperature-32)+1.8
    def convert_farenheit(self):
        return(self.temperature*1.8)+32
    
T=Temperature(int(input("Enter temperature:")))
print(T.convert_celcius())
print(T.convert_farenheit())    