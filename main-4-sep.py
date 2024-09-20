# oops in python
# 1. classes and objects
# 2. Inheritance
# 3. Polymorphism
# 4. Encapsulation
# 5. Abstraction
# 6. constructors
# 7. operator overloading
# 8. static and cass methods
# 9. decorators
# 10.abstract classes
#ex1
class chair:
    noofLegs = 4
    material  = "wood"
    price = 1200

c1 = chair()
print(c1.material)
c2 = chair()
print(c2.price)
c3 = chair()
print(c3.noofLegs)

#ex2
class chair:
    noofLegs = 4
    material  = "wood"
    price = 1200
print(chair.material)