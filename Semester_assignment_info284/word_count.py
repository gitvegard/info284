import io
import nbformat

with io.open('Semester_assignment_info284/Semester_assignment.ipynb', 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

word_count = 0
for cell in notebook.cells:
    if cell.cell_type == "markdown":
        word_count += len(cell['source'].replace('#', '').lstrip().split())

print(word_count)