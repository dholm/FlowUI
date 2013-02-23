# FlowUI table widget
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

import re
import textwrap

from flowui.widget import Widget


class Table(Widget):
    '''Table widget

    The table is a widget for structured data presentation. It is very similar
    to the table widget of HTML or as used by many spreadsheet tools. A table
    can consist of rows and or cells that are laid out in an orderly fashion on
    screen.

    Cells that are stored in rows are sized so that each column lines up
    vertically in every row. The size of each cell is calculated based on the
    maximum available table width and the size of each cell. If the cells of a
    row are too big to fit on one row they are broken up into multiple lines
    which are aligned within each column.

    Cells that are not stored in rows are all normalized to the same size and
    lined up vertically in the table as if they all belonged to a row
    consisting of the maximum number of cells that will fit on a row.

    '''
    def _max_cell_width(self, terminal):
        max_width = 0
        for cell in self._cells:
            max_width = max(max_width, cell.width(terminal))
        return max_width

    def __init__(self):
        self._rows = []
        self._cols_per_row = 0
        self._cells = []

    def add_cell(self, cell):
        '''Adds the cell to the table'''
        assert isinstance(cell, Cell)
        self._cells.append(cell)

    def add_row(self, row):
        '''Adds the row to the table'''
        assert isinstance(row, Row)
        self._cols_per_row = max(len(row.cells()), self._cols_per_row)
        self._rows.append(row)

    def _draw_cells(self, terminal, width):
        cell_width = self._max_cell_width(terminal)
        cells_per_row = int(width / cell_width)
        assert cells_per_row

        cell_row_width = (cell_width * cells_per_row)
        row_padding_begin = int((width - cell_row_width) / 2)
        row_padding_end = (width - cell_row_width - row_padding_begin)

        terminal.write('%s' % ' ' * int(row_padding_begin))
        cell_offset = 0
        for cell in self._cells:
            if cells_per_row <= cell_offset:
                cell_offset = 0
                terminal.write('%s\n%s' % (' ' * row_padding_end,
                                           ' ' * row_padding_begin))

            cell.draw(terminal, cell_width)
            cell_offset += 1

        last_row_padding = (width - (cell_width * cell_offset) -
                            row_padding_begin)
        terminal.write('%s\n' % (' ' * last_row_padding))

    def _cols_median(self, terminal):
        cols_width = [[0 for i in range(len(self._rows))]
                      for j in range(self._cols_per_row)]
        for i in range(len(self._rows)):
            row = self._rows[i]
            for j in range(len(row.cells())):
                cell = row.cells()[j]
                cols_width[j][i] = cell.width(terminal)

        cols_median = [0 for i in range(len(cols_width))]
        for i in range(len(cols_width)):
            lst = sorted(cols_width[i])
            length = len(lst)
            if not length % 2:
                neighbours_sum = (lst[int(length / 2)] +
                                  lst[int(length / 2) - 1])
                cols_median[i] = int(neighbours_sum / 2)

            else:
                cols_median[i] = lst[int(length / 2)]

        return cols_median

    def _cols_mean(self, terminal):
        cols_width = [[0 for i in range(len(self._rows))]
                      for j in range(self._cols_per_row)]
        for i in range(len(self._rows)):
            row = self._rows[i]
            for j in range(len(row.cells())):
                cell = row.cells()[j]
                cols_width[j][i] = cell.width(terminal)

        cols_mean = [0 for i in range(len(cols_width))]
        for i in range(len(cols_width)):
            cols_mean[i] = int(sum(cols_width[i]) / len(cols_width[i]))

        return cols_mean

    def _fill_widths(self, widths, wanted_widths, max_widths):
        for i in range(len(max_widths)):
            if widths[i] is not None:
                continue
            elif wanted_widths[i] <= max_widths[i]:
                widths[i] = wanted_widths[i]

        return widths

    def _col_widths(self, terminal, width):
        cell_widths = []
        for row in self._rows:
            cells = len(row.cells())
            cell_widths.extend([0] * (cells - len(cell_widths)))

            for i in range(len(row.cells())):
                cell_widths[i] = max(cell_widths[i],
                                     row.cells()[i].width(terminal))

        if width < sum(cell_widths):
            adjusted_widths = [None] * len(cell_widths)

            mean_widths = [(int(width / len(cell_widths)))] * len(cell_widths)
            adjusted_widths = self._fill_widths(adjusted_widths, cell_widths,
                                                mean_widths)
            mean_widths = self._cols_mean(terminal)
            median_widths = self._cols_median(terminal)
            if adjusted_widths.count(None):
                left_width = width - sum([x for x in adjusted_widths
                                          if x is not None])
                max_cell_width = int(left_width / adjusted_widths.count(None))
                max_widths = [min(max(mean_widths[i], median_widths[i]),
                                  max_cell_width)
                              for i in range(len(cell_widths))]
                adjusted_widths = self._fill_widths(adjusted_widths,
                                                    cell_widths, max_widths)

            while adjusted_widths.count(None):
                left_width = width - sum([x for x in adjusted_widths
                                          if x is not None])
                max_cell_width = int(left_width / adjusted_widths.count(None))
                current_min = min([cell_widths[i]
                                   for i in range(len(cell_widths))
                                   if adjusted_widths[i] is None])
                index = cell_widths.index(current_min)
                adjusted_widths[index] = max_cell_width

            return adjusted_widths

        return cell_widths

    def _draw_rows(self, terminal, width):
        cell_widths = self._col_widths(terminal, width)
        row_width = sum(cell_widths)
        for row in self._rows:
            while row is not None:
                row = row.draw(terminal, cell_widths)
                padding = ' ' * (width - row_width)
                terminal.write('%s\n' % padding)

    def draw(self, terminal, width):
        '''Draw the table on the specified terminal constrained to the
        specified width'''
        terminal.write('%(face-normal)s')
        if self._rows:
            self._draw_rows(terminal, width)
        if self._cells:
            self._draw_cells(terminal, width)


class Row(Widget):
    '''A table row'''

    def __init__(self):
        super(Row, self).__init__()
        self._cells = []

    def cells(self):
        '''Returns a list of the cells stored in the row'''
        return self._cells

    def add_cell(self, cell):
        '''Appends the cell to the row'''
        self._cells.append(cell)

    def width(self, terminal):
        '''Calculate and return the width of the row in characters'''
        width = 0
        for cell in self._cells:
            width += cell.width(terminal)
        return width

    def draw(self, terminal, cell_widths):
        '''Draw the row on the terminal using the defined column widths'''
        assert len(cell_widths) == len(self._cells)

        cells_rest = []
        for i in range(len(self._cells)):
            rest = self._cells[i].draw(terminal, cell_widths[i])
            if len(rest):
                cells_rest.append(rest)
            else:
                cells_rest.append(None)

        if cells_rest.count(None) < len(cells_rest):
            row = Row()
            for content in cells_rest:
                if content is None:
                    row.add_cell(Cell(''))
                else:
                    row.add_cell(Cell(content))
            return row
        return None


class Cell(Widget):
    '''A table cell'''

    _format_exp = re.compile(r'(%\([^\s]+?\)s)')

    def __init__(self, contents=''):
        super(Cell, self).__init__()
        self._contents = ''
        if contents:
            self._contents = (' %s ' % contents)

    def width(self, theme):
        '''Calculate and return the width in characters of the cell contents'''
        return theme.len(self._contents)

    def contents(self):
        '''Return the contents of the cell'''
        return self._contents

    def draw(self, terminal, width):
        '''Draw the cell on the terminal constrained to the specified width'''
        split = self._format_exp.split(self._contents)
        contents = [[]]
        width_left = width
        last_format = ''
        for item in split:
            if self._format_exp.match(item):
                contents[-1].append(item)
                last_format = item

            else:
                item_len = len(item.replace('%%', '%'))
                if item_len <= width_left:
                    contents[-1].append(item)
                    width_left -= item_len

                elif item_len < width:
                    contents.append([last_format, item])
                    width_left = width - item_len

                elif len(item[:width_left]):
                    first = textwrap.wrap(item[:width_left], width_left)[0]
                    contents[-1].append(first)
                    rest = textwrap.wrap(item[len(first):], width)
                    for line in rest:
                        contents.append([last_format, line])
                    width_left = width - len(contents[-1][-1])

        contents = [''.join(x) for x in contents]
        cell_content = ''
        if len(contents):
            cell_content = contents[0]

        line_width = terminal.len(cell_content)
        padding = ' ' * (width - line_width)
        terminal.write(('%(contents)s%(padding)s' %
                        {'contents': cell_content,
                         'padding': padding}))

        return ''.join(contents[1:])
