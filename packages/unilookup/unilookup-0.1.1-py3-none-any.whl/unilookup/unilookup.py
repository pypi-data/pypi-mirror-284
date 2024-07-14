#!/usr/bin/env python

# (C) Mia Nordentoft 2016-2018
# (C) Martin Maciaszek 2024
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import unicodedata2 as ud
from terminaltables import AsciiTable

directory = os.path.dirname(os.path.realpath(__file__))


def main():
    # Read input
    for line in sys.stdin:
        chars = list(line)

        table_data = [["character", "byte", "UTF-32", "name", "glyph"]]

        byte = 0
        for point in chars:
            num = ord(point)

            # https://en.wikipedia.org/wiki/UTF-8#Description
            if num >= 0x10000:
                point_length = 4
            elif num >= 0x800:
                point_length = 3
            elif num >= 0x80:
                point_length = 2
            else:
                point_length = 1

            utf32 = hex(num)[2:].upper().zfill(8)
            glyph = point

            table_data.append(
                [
                    hex(num)[2:].upper().zfill(point_length * 2),
                    str(byte),
                    utf32,
                    ud.name(point, "UNKNOWN"),
                    glyph,
                ]
            )

            byte += point_length

        table = AsciiTable(table_data)
        table.inner_column_border = False
        table.outer_border = False
        print(table.table)


if __name__ == "__main__":
    main()
