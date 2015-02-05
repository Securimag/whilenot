
"""
    +:  original
        simple

    -:  import
        wait I/O is not really loop forever ...

"""

import select
select.select([], [], [])
