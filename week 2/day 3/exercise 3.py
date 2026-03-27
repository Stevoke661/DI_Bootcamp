#exs1
from abc import ABC, abstractmethod

class Temperature(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def to_kelvin(self):
        pass

    @classmethod
    @abstractmethod
    def from_kelvin(cls, k_value):
        pass

    def convert_to(self, target_class):
        """Converts current temperature to any other Temperature subclass."""
        kelvin_val = self.to_kelvin()
        return target_class.from_kelvin(kelvin_val)

class Celsius(Temperature):
    def to_kelvin(self):
        return self.value + 273.15
    
    @classmethod
    def from_kelvin(cls, k_value):
        return cls(k_value - 273.15)

class Fahrenheit(Temperature):
    def to_kelvin(self):
        return (self.value - 32) * 5/9 + 273.15
    
    @classmethod
    def from_kelvin(cls, k_value):
        return cls((k_value - 273.15) * 9/5 + 32)

class Kelvin(Temperature):
    def to_kelvin(self):
        return self.value
    
    @classmethod
    def from_kelvin(cls, k_value):
        return cls(k_value)
    
#exs2
import random

class QuantumParticle:
    def __init__(self, x=0, y=0.0, p=0.5):
        self._x = x          # position
        self._y = y          # momentum
        self._p = p          # spin
        self.entangled_with = None

    def _disturb(self):
        """Internal method to trigger uncertainty/interference."""
        self._x = random.randint(1, 10000)
        self._y = random.random()
        print("Quantum Interferences!!")

    def position(self):
        self._disturb()
        return self._x

    def momentum(self):
        self._disturb()
        return self._y

    def spin(self):
        """Measures spin and handles entanglement logic."""
        self._p = random.choice([0.5, -0.5])
        
        if self.entangled_with:
            # Spooky action: set the partner's spin to the opposite
            self.entangled_with._p = -self._p
            print("Spooky Action at a Distance !!")
            
        return self._p

    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            raise TypeError("Can only entangle with another QuantumParticle!")
        
        self.entangled_with = other
        other.entangled_with = self
        print(f"Particle is now in quantum entanglement.")

    def __repr__(self):
        status = "Entangled" if self.entangled_with else "Isolated"
        return f"QuantumParticle(x={self._x}, y={self._y:.2f}, spin={self._p}, status={status})"

# Example Usage:
p1 = QuantumParticle()
p2 = QuantumParticle()
p1.entangle(p2)
print(f"P1 Spin: {p1.spin()}")
print(f"P2's spin is now automatically: {p2._p}")