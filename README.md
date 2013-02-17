# FlowUI

FlowUI is a simple presentation toolkit for text-based displays where it is not
possible to move the cursor backwards. All widgets are designed so that they
are rendered one character at a time and assuming the cursor is moved forward
one character each time.


## Requirements

FlowUI has been tested with Python 2.7 and 3.3 on MacOS X and GNU/Linux.


## Example

Here follows a short example showing how a matrix of data can be rendered into
into a table.

![FlowUI Screenshot](https://github.com/dholm/FlowUI/raw/master/screenshot.png)


    def sample_table(term):
        data = [['#', 'Thickness', 'Temperature', 'Concentration'],
                [1, 2.1740228, 82, 0.066],
                [2, 1.8774501, 77, 0.071],
                [3, 1.8774704, 77, 0.072],
                [4, 1.9762727, 79, 0.069]]

        tbl = table.Table()
        for r in data:
            row = table.Row()
            for c in r:
                row.add_cell(table.Cell(c))

            tbl.add_row(row)

        experiment_section = Section('Experiment data')
        experiment_section.add_component(tbl)
        experiment_section.draw(term, term.width())

    if __name__ == '__main__':
        terminal = SysTerminal()
        solarized = Solarized(terminal.depth())
        themed_terminal = ThemedTerminal(terminal, solarized)
        sample_table(themed_terminal)


## License

FlowUI is distributed under the 3-clause "Revised BSD License". See LICENSE.md
for the full license text.
