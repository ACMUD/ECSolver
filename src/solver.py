import re
from typing import Set


class CellReferenceValidator:
    """
    Componente encargado de detectar y validar referencias válidas a celdas.
    
    Soporta formatos estándar como A1, B2, Z10, AA1, etc.
    Verifica que el formato sea correcto (letra(s) seguidas de número).
    """
    
    # Patrón regex para referencias de celda válidas
    CELL_REFERENCE_PATTERN = re.compile(r'^[A-Z]+[1-9]\d*$')
    
    @classmethod
    def is_valid_cell_reference(cls, reference: str) -> bool:
        if not isinstance(reference, str):
            return False
        return bool(cls.CELL_REFERENCE_PATTERN.match(reference.upper()))
    
    @classmethod
    def find_cell_references(cls, expression: str) -> Set[str]:
        if not isinstance(expression, str):
            return set()
        
        # Buscar todas las posibles referencias de celda
        potential_refs = re.findall(r'\b[A-Z]+\d+\b', expression.upper())
        
        # Filtrar solo las referencias válidas
        valid_refs = {ref for ref in potential_refs if cls.is_valid_cell_reference(ref)}
        
        return valid_refs


