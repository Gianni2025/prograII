from .store import NYPizzaStore, ChicagoPizzaStore

def main():

    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
#    p1 = ny.order_pizza("cheese"); print("Ethan ordered:", p1); print("-----------")
#S    p2 = chi.order_pizza("cheese"); print("Joel ordered:", p2); print("-----------")
    p3 = ny.order_pizza("veggie"); print("Ana ordered:", p3); print("-----------")
    p4 = chi.order_pizza("veggie"); print("Juliet ordered:", p4); print("-----------")
    p5 = chi.order_pizza("pepperoni"); print("Caroline ordered:", p5); print("-----------")
    p6 = chi.order_pizza("pepperoni"); print("Michael ordered:", p6); print("-----------")
       
    
if __name__ == "__main__":
    main()
