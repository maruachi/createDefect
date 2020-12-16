import re
import sys

from .atom import atom, cell

class read_final:
	def __init__(self, filename):
		self.filename = filename
		self.num_format = re.compile('[+-]?[0-9]+\.[0-9]+')
		self.lat_vecs = []
		self.atoms = []

		self.get_lat_vecs()
		self.get_atoms()
		self.cell = cell(self.lat_vecs, self.atoms)

	def get_lat_vecs(self):
		with open(self.filename, 'r') as f:
			for line in f:
				if "CELL_PARAMETERS" in line:
					for i in range(3):
						temp_line = f.readline()
						temp = self.num_format.findall(temp_line)
						temp = [float(item) for item in temp]
						self.lat_vecs.append(temp)
	
	def get_atoms(self):
		with open(self.filename, 'r') as f:
			for line in f:
				if "ATOMIC_POSITIONS" in line:
					i = 1
					atoms = []
					for temp_line in f:
						temp_atm_pos = self.num_format.findall(temp_line)
						temp_atm_pos = [float(item) for item in temp_atm_pos]
						temp_spe = re.match('[a-zA-Z]+', temp_line).group()
						temp_atom = atom(temp_spe, temp_atm_pos, i)
						self.atoms.append(temp_atom)
						i += 1

	def get_all(self):
		return self.cell

class read_defect_indexes:
	def __init__(self, filename):
		self.filename = filename
		self.f = open(self.filename, 'r')
		self.defect_indexes = []
	
	def get_one_defect_info(self):
		type_def = self.f.readline().rstrip('\n')
		if len(type_def) == 0:
			return False
		defect_index = ()
		if "substitute" in type_def:
			index = self.f.readline()
			index = int(index)
			spe = self.f.readline().rstrip('\n')
			defect_index = (type_def, index, spe)
		elif "vacancy" in type_def:
			index = self.f.readline()
			index = int(index)
			defect_index = (type_def, index)
		elif "insert" in type_def:
			spe = self.f.readline().rstrip('\n')
			line = self.f.readline()
			pos = re.findall('[0-9]+\.[0-9]+', line)
			pos = [float(pos) for pos in pos]
			defect_index = (type_def, spe, pos)
		else:
			print("invalid defect index inputs", file = sys.stderr)
		self.defect_indexes.append(defect_index)

		return True
	
	def get_all(self):
		flag = self.get_one_defect_info()
		while(flag):
			flag = self.get_one_defect_info()
		return self.defect_indexes
