# Python doc String > public documentation
# modulename:planning
# module descripion:math utilities moduek
# module info: marh statistics random...(python starndar library)

# ----------
# constantes a nivel de modulo
# ----------
DAYS_LEAP_YEAR:int = 366
DAYS_NON_LEAP_YEAR:int=365
JANUARY:int=1
FEBRUARY:int=2
MARCH:int=3
APRIL:int=4
MAY:int=5
JUNE:int=6
JULY:int=7
AUGUST:int=8
SEPTEMBRER:int=9
OCTOBER:int=10
NOVEMBERint=11
DECEMBER:int=12

MONDAY:int=1
TUESDAY:int=2
WENESDAT:int=3
THURSDAY:int=4
FRIDAY:int=5
SATURDAY:int=6
SUNDAY:int=7




# ----------
# funciones  a nivel de modulo
# -> son type hint(PEP) Sugar syntax es documentar de forma publica los tipos de datos devueltos que esperan los parametros van a devolver un entero
# ----------


def current_year() -> int :
    """ Python Docstring"""
    pass

def elapsed_days()-> int:
     """ Python Docstring"""
     pass

def remaining_days() -> int:
     """ Python Docstring"""
     pass


#year:int = current-year() por defecto es el current yea si no se le pasa ningun parametro
def is_lap_year(year:int = current_year()) -> bool:  
     """ Python Docstring"""
     pass

def total_days(year:int = current_year) -> int:
     """ Python Docstring"""
     pass

def next_lap_year(year:int = current_year) -> int:
     """ Python Docstring"""
     pass


def previous_lap_year(year:int = current_year) -> int:
     """ Python Docstring"""
     pass

def year_progress(pretty:bool=True) -> str|float:
     """ Python Docstring"""
     pass


# ----------
# clase o definiciones de porpios tipos de datos o modulos  a nivel de 
# ----------
