 Shift Register (2-bit) 
                     class ShiftRegister: 
                    def __init__(self): 
                    self.register = [0, 0]  # 2-bit register 
 
                 def shift_right(self, bit): 
                 self.register = [bit] + self.register[:-1] 
                print("Register:", self.register) 
 
                 # Example usage 
               sr = ShiftRegister() 
               sr.shift_right(1) 
               sr.shift_right(0) 
               sr.shift_right(1) 
 
 

 
◆ Synchronous Counter (2-bit) 
class SynchronousCounter: 
    def __init__(self): 
        self.count = 0 
 
    def clock_pulse(self): 
        self.count = 
(self.count+ 1) % 4  # 2-bit 
max value = 3 (00 to 11) 
        print("Count:", 
format(self.count, '02b')) 
 
# Example usage 
counter = 
SynchronousCounter() 
for _ in range(10): 
    counter.clock_pulse() 
 

 
◆ 4-to-1 Multiplexer 
 
class Multiplexer: 
 
def  init (self, inputs): 
self.inputs = inputs 
def select(self, sel): 
output = self.inputs[sel] 
print(f"Selected Input [{sel}]: {output}") 
mux = Multiplexer([10, 20, 30, 40]) 
mux.select(2) 
 
mux.select(0) 
 
 
                    
