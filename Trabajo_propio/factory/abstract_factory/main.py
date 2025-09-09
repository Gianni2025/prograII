from .store import NYPizzaStore, ChicagoPizzaStore
from .ingredients import *
from .pizza import *

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    ny.order_pizza("cheese"); print("--------")
    chi.order_pizza("cheese"); print("--------")
    
    chi.order_pizza("clam"); print("--------")
    ny.order_pizza("veggies"); print("--------")
    chi.order_pizza("veggies"); print("--------")
    ny.order_pizza("pepperoni"); print("--------")
    chi.order_pizza("pepperoni"); print("--------")   
    ny.order_pizza("mushroom"); print("--------")
    chi.order_pizza("mushroom"); print("--------") 

if __name__ == "__main__":
    main()




    #print(chi.order_pizza("pepperoni"))
    #print(type(chi.order_pizza("pepperoni")))
    #pizza=ny.order_pizza("clam")
    #print(str(pizza.clam))
    #print(isinstance(chi.order_pizza("pepperoni"), PepperoniPizza))