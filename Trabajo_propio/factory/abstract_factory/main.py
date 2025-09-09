from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    ny.order_pizza("cheese"); print("--------")
    chi.order_pizza("cheese"); print("--------")
    
    chi.order_pizza("clam"); print("--------")
    ny.order_pizza("veggies"); print("--------")
    chi.order_pizza("veggies"); print("--------")
    ny.order_pizza("pepperoni"); print("--------")
    chi.order_pizza("pepperoni"); print("--------")  
    

if __name__ == "__main__":
    main()
