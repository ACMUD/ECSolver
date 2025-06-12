import re
from typing import Any, Dict, Optional, Set


class SolverError(Exception):
    """Excepción personalizada para errores del módulo Solver."""
    pass


class CircularReferenceError(SolverError):
    """Excepción lanzada cuando se detecta una referencia circular."""
    pass


class InvalidCellReferenceError(SolverError):
    """Excepción lanzada cuando se encuentra una referencia de celda inválida."""
    pass


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

class ExcelSolver:
    """
    Módulo principal Solver para resolución de referencias de celda.
    
    Maneja la resolución segura y recursiva de referencias y detecta ciclos infinitos.
    """
    
    def __init__(self):
        """
        Inicializa el solver.
        """
        self.cell_data: Dict[str, Any] = {}
        self.validator = CellReferenceValidator()
        
    def set_cell_value(self, cell_ref: str, value: Any) -> None:
        """
        Establece el valor de una celda.
        
        Args:
            cell_ref (str): Referencia de la celda (ej: "A1")
            value (Any): Valor a asignar a la celda
            
        Raises:
            InvalidCellReferenceError: Si la referencia de celda no es válida
        """
        if not self.validator.is_valid_cell_reference(cell_ref):
            raise InvalidCellReferenceError(f"Referencia de celda inválida: {cell_ref}")
        
        self.cell_data[cell_ref.upper()] = value
    
    def get_cell_value(self, cell_ref: str) -> Any:
        """
        Obtiene el valor raw de una celda sin resolver referencias.
        
        Args:
            cell_ref (str): Referencia de la celda
            
        Returns:
            Any: Valor de la celda
        """
        return self.cell_data.get(cell_ref.upper())
    
    def _detect_circular_reference(self, cell_ref: str, visited: Set[str], 
                                recursion_stack: Set[str]) -> bool:
        """
        Detecta referencias circulares usando DFS.
        
        Args:
            cell_ref (str): Referencia actual de celda
            visited (Set[str]): Conjunto de celdas ya visitadas
            recursion_stack (Set[str]): Stack de recursión actual
            
        Returns:
            bool: True si se detecta una referencia circular
        """
        if cell_ref in recursion_stack:
            return True
        
        if cell_ref in visited:
            return False
        
        visited.add(cell_ref)
        recursion_stack.add(cell_ref)
        
        cell_value = self.get_cell_value(cell_ref)
        if cell_value is None:
            recursion_stack.remove(cell_ref)
            return False
        
        # Si el valor es una string, buscar referencias
        if isinstance(cell_value, str):
            references = self.validator.find_cell_references(cell_value)
            for ref in references:
                if self._detect_circular_reference(ref, visited, recursion_stack):
                    recursion_stack.remove(cell_ref)
                    return True
        
        recursion_stack.remove(cell_ref)
        return False
    
    def resolve_cell_reference(self, cell_ref: str, visited: Optional[Set[str]] = None) -> Any:
        """
        Resuelve una referencia de celda de forma recursiva y segura.
        
        Args:
            cell_ref (str): Referencia de celda a resolver
            visited (Set[str], optional): Conjunto de celdas visitadas (para detección de ciclos)
            
        Returns:
            Any: Valor resuelto de la celda
            
        Raises:
            InvalidCellReferenceError: Si la referencia no es válida
            CircularReferenceError: Si se detecta una referencia circular
        """
        # Validar referencia de celda
        if not self.validator.is_valid_cell_reference(cell_ref):
            raise InvalidCellReferenceError(f"Referencia de celda inválida: {cell_ref}")
        
        cell_ref = cell_ref.upper()
        
        # Inicializar conjunto de visitadas si es la primera llamada
        if visited is None:
            visited = set()
            # Verificar referencias circulares antes de comenzar
            if self._detect_circular_reference(cell_ref, set(), set()):
                raise CircularReferenceError(f"Referencia circular detectada que involucra la celda {cell_ref}")
        
        # Verificar si ya visitamos esta celda en la cadena actual
        if cell_ref in visited:
            raise CircularReferenceError(f"Referencia circular detectada que involucra la celda {cell_ref}")
        
        # Obtener valor de la celda
        cell_value = self.get_cell_value(cell_ref)
        
        # Si no es una string, devolver el valor directamente
        if not isinstance(cell_value, str):
            return cell_value
        
        # Agregar a visitadas
        visited.add(cell_ref)
        
        try:
            # Resolver referencias en la expresión
            resolved_expression = self.resolve_expression(cell_value, visited.copy())
            
            # Si la expresión contiene funciones, debería reenviarse al módulo Logic
            # Por ahora, si es una expresión numérica simple, la evaluamos
            if self._is_simple_numeric_expression(resolved_expression):
                return eval(resolved_expression)
            else:
                # Para expresiones complejas con funciones, devolver la expresión resuelta
                # En una implementación completa, esto se enviaría al módulo Logic
                return resolved_expression
                
        finally:
            # Remover de visitadas al terminar
            visited.discard(cell_ref)
    
    def resolve_expression(self, expression: str, visited: Optional[Set[str]] = None) -> str:
        """
        Resuelve todas las referencias de celda en una expresión.
        
        Args:
            expression (str): Expresión a resolver
            visited (Set[str], optional): Conjunto de celdas visitadas
            
        Returns:
            str: Expresión con referencias resueltas
        """
        if visited is None:
            visited = set()
        
        # Encontrar todas las referencias de celda en la expresión
        cell_references = self.validator.find_cell_references(expression)
        
        resolved_expression = expression
        
        # Resolver cada referencia
        for cell_ref in cell_references:
            try:
                resolved_value = self.resolve_cell_reference(cell_ref, visited.copy())
                # Reemplazar la referencia con el valor resuelto
                resolved_expression = resolved_expression.replace(cell_ref, str(resolved_value))
            except CircularReferenceError as e:
                # Re-lanzar errores críticos
                raise e
        
        return resolved_expression
    
    def _is_simple_numeric_expression(self, expression: str) -> bool:
        """
        Verifica si una expresión es una expresión numérica simple que puede evaluarse con eval().
        
        Args:
            expression (str): Expresión a verificar
            
        Returns:
            bool: True si es una expresión numérica simple
        """
        # Patrón para expresiones numéricas simples (números, operadores básicos, paréntesis)
        simple_pattern = re.compile(r'^[\d\+\-\*\/\(\)\.\s]+$')
        return bool(simple_pattern.match(expression))
    
    def clear_all_cells(self) -> None:
        """Limpia todas las celdas del solver."""
        self.cell_data.clear()
