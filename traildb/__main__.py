from __future__ import unicode_literals
from __future__ import print_function

from future import standard_library
standard_library.install_aliases()

import sys
import traildb

for cookie, trail in traildb.TrailDB(*(sys.argv[1:] or ['a.tdb'])).crumbs():
    print(cookie, trail)
