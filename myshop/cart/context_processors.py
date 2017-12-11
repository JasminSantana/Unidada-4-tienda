""""Jasmin Santana Mares"""
""""Jose Mauricio hernandez"""
""""GITI9071-E"""
'carga los cart'
from .cart import Cart

def cart(request):
    return {'cart': Cart(request) }
