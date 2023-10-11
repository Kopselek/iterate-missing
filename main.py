from ruamel.yaml import YAML

class LangKey():
	def __init__(self, path, key, value, filename):
		self.path = path
		self.key = key
		self.value = value
		self.filename = filename

class FileKeyComparer:
	def __init__(self, object_list_1 : list[object], object_list_2: list[object]):
		self.object_list_1 = object_list_1
		self.object_list_2 = object_list_2
		self.list_keys : list[str] = [i.key for i in self.object_list_2]
	def check_key(self) -> list[str]:
		wrong_keys = [i.path for i in self.object_list_1 if i.key not in self.list_keys]
		return wrong_keys


def irerate_oredered_dict(ordered_dict, parentPath = "", filename = ""):
	key_container = []
	for key,value in ordered_dict.items():
		if(parentPath != ""):
			path = parentPath + "." + str(key)
		else:
			path = str(key)
		if(isinstance(value, str)):
			langKey = LangKey(str(path), str(key), str(value), str(filename))
			key_container.append(langKey)
		elif(isinstance(value, int)):
			langKey = LangKey(str(path), str(key), str(value), str(filename))
			key_container.append(langKey)
		elif(value is None):
			continue
		else:
			langKey = LangKey(str(path), str(key), "", str(filename))
			next_key_container = irerate_oredered_dict(value, parentPath=path, filename=filename)
			key_container.append(langKey)
			key_container += next_key_container
	return key_container

def iterate_file_keys(input_file):
	yaml = YAML()
	yaml_dict = yaml.load(open(input_file, encoding="UTF-8"))
	key_container = irerate_oredered_dict(yaml_dict, filename=input_file)
	return key_container

def print_missing_key(key, source):
	print("================")
	print("source: " + source)
	print("missing: " + key)

base_file = 'messages.pl.yaml'
base_keys = iterate_file_keys(base_file)

compare_files = [
	'messages.en.yaml',
	'messages.de.yaml',
	'messages.es.yaml',
]

for compare_file in compare_files:
	compare_keys = iterate_file_keys(compare_file)
	comparer = FileKeyComparer(base_keys, compare_keys)
	results = comparer.check_key()
	for result in results:
		print_missing_key(result, compare_file)
