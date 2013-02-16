# FlowUI themes unit tests
#
# Copyright (c) 2012-2013, David Holm <dholmster@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author of FlowUI nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL DAVID HOLM BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from unittest import TestCase

from flowui.terminals import SysTerminal
from flowui.themes import Solarized
from flowui.widgets import Section
from flowui.widgets import table


class WidgetsTest(TestCase):
    def theme(self):
        return self._theme

    def setUp(self):
        self._terminal = SysTerminal()
        self._theme = Solarized(self._terminal.depth())

        reset = self.theme().property('normal')
        self._terminal.write('%s\n\t# Begin Widget #\n' % reset)

    def tearDown(self):
        reset = self.theme().property('normal')
        self._terminal.write('%s\t# End Widget #\n' % reset)

    def test_section(self):
        section = Section('test section')
        section.draw(self._terminal, self._theme, self._terminal.width())

        self.assertRaises(AssertionError, section.draw, self._terminal,
                          self._theme, 1)

    def test_table(self):
        tbl = table.Table()
        tbl.draw(self._terminal, self._theme, self._terminal.width())

    def test_tables_cells(self):
        tbl = table.Table()
        for i in range(0, 20):
            cell = table.Cell('cell %d' % i)
            tbl.add_cell(cell)

        width = int(self._terminal.width() / 2)
        tbl.draw(self._terminal, self._theme, width)

    def test_table_row_multiline_cell(self):
        row = table.Row()
        cells = [table.Cell('First col'),
                 table.Cell('this cell should span multiple lines'),
                 table.Cell('Third col')]
        for cell in cells:
            row.add_cell(cell)
        row_len = (sum(x.width(self._theme) for x in cells) -
                   int(cells[1].width(self._theme) / 2))

        tbl = table.Table()
        tbl.add_row(row)
        tbl.draw(self._terminal, self._theme, row_len)

    def test_tables_rows(self):
        tbl = table.Table()
        for i in range(0, 5):
            row = table.Row()
            for j in range(0, 5):
                cell = table.Cell('cell %d,%d' % (i, j))
                row.add_cell(cell)

            tbl.add_row(row)

        width = int(self._terminal.width() / 2)
        tbl.draw(self._terminal, self._theme, width)

    def test_table_cells_rows(self):
        tbl = table.Table()
        for i in range(0, 5):
            row = table.Row()
            for j in range(0, 5):
                cell = table.Cell('cell %d,%d' % (i, j))
                row.add_cell(cell)

            tbl.add_row(row)
            cell = table.Cell('cell %d' % i)
            tbl.add_cell(cell)

        width = int(self._terminal.width() / 2)
        tbl.draw(self._terminal, self._theme, width)

    def test_table_rows_varying_cells(self):
        data = [['col 1', 'col 2', 'col 3'],
                ['xxYYxxYYxx', '-', ''],
                ['', '-', 'xxYYxxYY']]

        tbl = table.Table()
        for r in data:
            row = table.Row()
            for c in r:
                row.add_cell(table.Cell(c))

            tbl.add_row(row)

        tbl.draw(self._terminal, self._theme, self._terminal.width())
