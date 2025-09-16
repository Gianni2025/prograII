
import os
import sys
#factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

""" 
def test_import_simple_factory():
    simple_factory_path = os.path.join(factory_dir, "simple_factory")
    sys.path.insert(0, simple_factory_path )      
    import main as s  
    from simple_factory import SimplePizzaFactory 
    from store import PizzaStore
    from pizza import CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza
    assert callable(s.main)
"""
 
def test_import_factory_method():   

    import factory.factory_method.main as fm 
    from factory.factory_method.store import NYPizzaStore, ChicagoPizzaStore
    from factory.factory_method.pizza import (NYStyleCheesePizza,  ChicagoStyleCheesePizza, NYStyleVeggiePizza,
    ChicagoStyleVeggiePizza, NYStylePepperoniPizza,  ChicagoStylePepperoniPizza, )
    assert   callable(fm.main)
"""    
def test_import_abstract_factory():   
    #factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    abstract_factory_path = os.path.join(factory_dir, "abstract_factory")
    sys.path.insert(0, abstract_factory_path )  
    from store import NYPizzaStore, ChicagoPizzaStore
    from pizza import PepperoniPizza, CheesePizza, MushroomPizza    
    import factory.abstract_factory.main as af
    assert callable(af.main)  
"""