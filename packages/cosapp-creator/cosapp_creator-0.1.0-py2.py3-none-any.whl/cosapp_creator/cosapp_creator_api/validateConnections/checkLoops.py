from typing import List, Dict, Union, Any

from cosapp.base import System
from cosapp.core import MathematicalProblem
from cosapp.core.numerics.boundary import Unknown
from cosapp.core.numerics.residues import Residue


def format_dict(data: Union[Dict[str, Unknown], Dict[str, Residue]]) -> List[Dict[str, Any]]:
    def to_context_content_dict(obj: Union[Unknown, Residue]):
        objDict = obj.to_dict()
        return {
            'context': objDict['context'],
            'content': objDict['name'],
        }    
    return list(map(to_context_content_dict, data.values()))


def format_problem(problem: MathematicalProblem) -> Dict[str, Any]:
    """Format a MathematicalProblem instance into a dictionary"""
    unknowns = None
    equations = None
    if problem.unknowns:
        unknowns = format_dict(problem.unknowns)
    if problem.residues:
        equations = format_dict(problem.residues)
    return {
        'nUnknowns': problem.n_unknowns,
        'nEquations': problem.n_equations,
        'unknowns': unknowns,
        'equations': equations,
    }


def checkLoops(system: System) -> Dict[str, Any]:
    """Get the inner mathematical problem of `system`
    """
    system.open_loops()
    loops = format_problem(system.assembled_problem())
    system.close_loops()
    return loops
