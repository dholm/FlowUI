# FlowUI

FlowUI is a simple presentation toolkit for text-based displays where it is not
possible to move the cursor backwards. All widgets are designed so that they
are rendered one character at a time and assuming the cursor is moved forward
one character each time.


## Requirements

FlowUI has been tested with Python 2.7 on MacOS X and GNU/Linux but it should
work equally well on any terminal which supports
[ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code).


## Themes

Theme's are loosely based on the controls used by [Vim](http://www.vim.org/)
color schemes. This makes it easier to port existing themes to FlowUI. A
domain-specific language similar to the one used to defined lexers in
[Pygments](http://pygments.org/) is used to define a theme.


### Format controls

Text is formatted by embedding certain keywords in the string before sending it
to the Theme's or AnsiTerminal's write method. For instance, to format the
statement "if a < 5:" on could write:

```python
('%(face-statement)sif%(face-normal)s %(face-identifier)sa%(face-normal)s < '
 '%(face-constant)s5%(face-normal)s:')
```

As seen in this example formatting can become quite verbose so prefer wrapping
it inside a widget which inserts the necessary keywords so that strings remain
readable inside your core logic.


### Typefaces

 * Regular

   Default face

 * Bold
 * Italic
 * Underline


### Text faces

 * face-normal
 * face-comment
 * face-constant

   string, char, number etc constants.

 * face-identifier

   Variable/function name.

 * face-statement

   Statements (if, else, for etc.)

 * face-define

   Definitions (i.e. #define X.)

 * face-type

   Types (integer, static, struct etc.)

 * face-special

   Special symbols or characters.

 * face-underlined

   Text that stands out (i.e. links.)

 * face-error

 * face-attention

   Anything that needs extra attention.

 * face-header

   Section headers etc.


## Widgets

FlowUI widgets inherit from the *Widget* class which serve to provide them with
a basic API.


### Containers

Containers are used to group widgets that belong to the same context.

 * Section

   The section provides a divider with an optional headline. Padding is added
   in order to illustrate that components in side it belong to that section.


### Tables

The table is a widget for structured data presentation. It is very similar to
the table widget of HTML or as used by many spreadsheet tools. A table can
consist of rows and or cells that are laid out in an orderly fashion on screen.

 * Table

   The table widget acts mainly as a container for the rows and cells as well
   as wrapping the drawing methods for them.

 * Row

   The row, as the name suggests, represents a single row in the table
   containing one or more cells.

 * Cell

   The cell is the most basic building block of the Table and also the widget
   that contains the actual table content. Cells are contained either in a row
   or directly inside the table and the difference is in how they are drawn.

   Cells that are stored in rows are sized so that each column lines up
   vertically in every row. The size of each cell is calculated based on the
   maximum available table width and the size of each cell. If the cells of a
   row are too big to fit on one row they are broken up into multiple lines
   which are aligned within each column.

   Cells that are not stored in rows are all normalized to the same size and
   lined up vertically in the table as if they all belonged to a row consisting
   of the maximum number of cells that will fit on a row.


## Terminal

Output from FlowUI passes to an instance of a *Terminal* object which is the
abstraction that represents the terminal emulator. This can either be directly
backed by an actual terminal emulator or wrap an interface which will
eventually output to a terminal.

A terminal needs to provide at least the width, in characters, and the number
of colors supported by the terminal in order for widgets to render properly.

FlowUI comes with one terminal implementation, *SysTerminal*, which uses
sys.stdout.

*AnsiTerminal* is a decorator for the terminal object which attaches a theme
to it while still providing the same interface as a *Terminal*.


## Example

Here follows a short example showing how a matrix of data can be rendered into
into a table.

![FlowUI Screenshot](https://github.com/dholm/FlowUI/raw/master/screenshot.png)


```python
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
    ansi_terminal = AnsiTerminal(SysTerminal(), Solarized())
    sample_table(ansi_terminal)
```


## Changelog

### 0.2.1
 - Fixes invalid length calculation when using AnsiTerminal
 - Fixes issue when writing percent sign (%%)

### 0.2.0
 - Defines a domain-specific language for themes.
   - Breaks Python 3000 support in this release.
   - The new theme format makes it easier to write non-ANSI backends for
     FlowUI and for this reason ThemedTerminal has been renamed AnsiTerminal.

### 0.1.0
 - Initial release


## License

FlowUI is distributed under the 3-clause
[Revised BSD License](http://opensource.org/licenses/BSD-3-Clause). See
LICENSE.md for the full license text.
