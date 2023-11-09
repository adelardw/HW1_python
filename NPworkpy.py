import numpy as np
from typing import Any

def mult_table(n: int, m: int, /, base=1) -> Any:
    """
    Annotation:
    n: size of axes 0 for mult table
    m: size of axes 1 for mult table
    /: some parameters
    base = 1: basic parameters for this mult table
    """
    table = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            table[i][j] = (i + base)*(j + base)

    return table


if __name__ == "__main__":
    print(mult_table(2,3,base=2))
