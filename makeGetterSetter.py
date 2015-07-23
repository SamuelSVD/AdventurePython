def make(name):
	s = ''
	s += '\tdef get'+name[0].upper()+name[1:]+'(self):\n'
	s += '\t\treturn self.'+name+'\n'
	s += '\tdef set'+name[0].upper()+name[1:]+'(self,'+name+'):\n'
	s += '\t\tself.'+name+' = ' +name+'\t'
	print s


stats = ['HP', 'MP', 'defence', 'accuracy', 'damageRange', 'speed', 'strength', 'intelligence', 'wisdom', 'luck']
