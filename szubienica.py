def hanging_steps():
    A = """
/
/
"""
    B = """
/ \\
/  \\
"""
    C = """
 |
 |
/ \\
/  \\
"""
    D = """
  ___
 |
 |
 |
/ \\
/  \\
"""
    E = """
  ___
 |   |
 |
 |
/ \\
/  \\

"""
    F = """
  ___
 |/  |
 |
 |
/ \\
/  \\

"""
    G = """
  ___
 |/  |
 |   0
 |
/ \\
/   \\

"""
    H = """
          ___
         |/  |
         |   0
         |   |
        / \\
       /   \\

"""
    I = """
                 ____
                |/   |
                |    0
                |    |
               / \   /\\
              /   \\
"""
    J = """
                         ____
                        |/   |
                        |    0
                        |   _|_
                       / \   /\\
                      /   \\
    """
    steps = [A, B, C, D, E, F, G, H, I, J]
    return steps
