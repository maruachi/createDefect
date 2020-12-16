from .atom import atom, cell

class defect:
	def __init__(self, cell):
		self.cell = cell
		self.lat_vecs = cell.lat_vecs
		self.atoms = cell.atoms
		self.defects = []
	
	def substitute(self, index, spe):
		for atom in self.atoms:
			if atom.index == index:
				selected_atom = atom
				selected_atom.spe = spe
				self.atoms.remove(atom)
				break

		self.defects.append(selected_atom)

	def vacancy(self, index):
		for atom in self.atoms:
			if atom.index == index:
				self.atoms.remove(atom)
				break

	def insert(self, spe, pos):
		temp_atom = atom(spe, pos, -1)
		self.defects.append(temp_atom)
	
	def get_defected(self):
		atoms_defected = self.atoms + self.defects
		return cell(self.lat_vecs, atoms_defected)
