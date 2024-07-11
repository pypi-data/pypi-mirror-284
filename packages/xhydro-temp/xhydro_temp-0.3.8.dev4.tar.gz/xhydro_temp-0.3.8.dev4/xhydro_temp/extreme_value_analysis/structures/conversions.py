from xhydro_temp.extreme_value_analysis.julia_import import jl
from juliacall import convert as jl_convert
import math
import numpy as np
from xhydro_temp.extreme_value_analysis.structures.dataitem import Variable
jl.seval("using DataFrames")

def py_variable_to_jl_variable(py_var: Variable):
    r"""Converts a python Variable object to a Julia Variable object"""
    return jl.Extremes.Variable(py_var.name, jl_convert(jl.Vector[jl.Real], py_var.value))

def py_str_to_jl_symbol(str: str):
    r"""Converts a python string to a Julia Symbol object"""
    return jl.Symbol(str)

def py_list_to_jl_vector(py_list: list):
    r"""Converts a python list to a Julia Vector object"""
    # Cleaning up nans and numpy.float32 elements
    py_list = [x for x in py_list if not math.isnan(x)] #TODO: deal with nans beter
    py_list = [float(i) if isinstance(i, np.float32) else i for i in py_list]

    if all(isinstance(i, float) or isinstance(i, int) for i in py_list):
        return jl_convert(jl.Vector[jl.Real], py_list)
    elif all(isinstance(i, str) for i in py_list):
        return jl_convert(jl.Vector[jl.String], py_list)
    elif not(all(isinstance(i, float) or isinstance(i, int) for i in py_list)) and not(all(isinstance(i, str) for i in py_list)):
        raise ValueError(f" Cannot convert unsupported type {type(py_list)} to julia vector: all values are not strings or numbers")
    else:
        raise ValueError(f" Cannot convert unsupported type {type(py_list)} to julia vector")

def jl_vector_to_py_list(jl_vector) -> list:
    r"""Converts a Julia vector to a python list"""
    return list(jl_vector)

# for a julia vector containing a single tuple, i.e. [(1,2,3)]
def jl_vector_tuple_to_py_list(jl_vector_tuple) -> list:
    r""" Converts a julia vector containing a single tuple (i.e. [(1,2,3)]) to a python list"""
    jl_sub_tuple, = jl_vector_tuple  # Unpack the single tuple from the list
    py_sub_list = list(jl_sub_tuple)
    return py_sub_list

# for a julia matrix of tuples, i.e. [(1,2,3), (4,5,6), (7,8,9)]
def jl_matrix_tuple_to_py_list(jl_matrix_tuple):
    r"""Converts a julia matrix of tuples to a python list of lists"""
    py_list = [tuple(row) for row in jl_matrix_tuple]
    return py_list

