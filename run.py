import sys
sys.path.append('/home/maruachi/home-make_code/pyworks/createDefect/')
from src import *

file_final = sys.argv[1]
file_def_index = sys.argv[2]

cell = read_final(file_final).get_all()
defect_indexes = read_defect_indexes(file_def_index).get_all()

defect = defect(cell)

for defect_index in defect_indexes:
	type_def = defect_index[0]

	if "substitute" in type_def:
		_, index, spe = defect_index 
		defect.substitute(index, spe)

	elif "vacancy" in type_def:
		_, index = defect_index
		defect.vacancy(index)

	elif "insert" in type_def:
		_, spe, pos = defect_index
		defect.insert(spe, pos)
	
	else:
		pass

defect.get_defected().print_input()
