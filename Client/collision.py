character_block_y = int(math.floor(self.character.position.y/32.0))
character_chunk_y = int(math.floor(character_block_y/20.0))
character_block_y -= character_chunk_y * 20

character_block_x = int(math.floor(self.character.position.x/32.0))
character_chunk_x = int(math.floor(character_block_x/20.0))
character_block_x -= character_chunk_x * 20

for entity in self.entities:
	#get initial position
	#update normally, if collision occurs, check if the block(s) in the direction of the entity are solid or not

	#We need to look at the four corners of the entity. these corners are determined by the shadow of the entity
	size = entity.getShadow().get_size()
	pos_x = entity.position.x
	pos_y = entity.position.y
	entity.update(delta)
	#corners can be done by checking (pos (+/-) (size/2))/ 32 if == pos/32 ignore corner. (???)
	is_solid = []
	for j in range(2):
		for i in range(2):
			y = -1
			x = -1
			if i:
				x = 1
			if j:
				y = 1
			x = entity.position.x + size[0]/2 * x
			y = entity.position.y + size[1]/2 * y
			corner_block_y = int(math.floor(y/32.0))
			corner_chunk_y = int(math.floor(corner_block_y/20.0))
			corner_block_y -= corner_chunk_y * 20
			corner_block_x = int(math.floor(x/32.0))
			corner_chunk_x = int(math.floor(corner_block_x/20.0))
			corner_block_x -= corner_chunk_x * 20
			is_solid.append(self.map.isSolidAt('%d_%d' % (corner_chunk_x, corner_chunk_y), (corner_block_x, corner_block_y)))
	# is_solid = ['TOP_LEFT', 'TOP_RIGHT', 'BOT_LEFT', 'BOT_RIGHT']
	if is_solid[0]:
		if is_solid[1]:
			if is_solid[2]:
				if is_solid[3]:	# 0 1 2 3
					entity.position.x = pos_x
					entity.position.y = pos_y
				else:			# 0 1 2
					#TOP_LEFT corner
					entity.position.x = pos_x - pos_x % 32 + size[0]/2
					entity.position.y = pos_y - pos_y % 32 + size[1]/2
			elif is_solid[3]:	# 0 1 3
				#TOP_RIGHT corner
				entity.position.x = pos_x + (32 - pos_x % 32) - size[0]/2
				entity.position.y = pos_y - pos_y % 32 + size[1]/2
			else:				# 0 1
				#TOP
				entity.position.y = pos_y - pos_y % 32 + size[1]/2
		elif is_solid[2]:
			if is_solid[3]:		# 0 2 3
				#BOT_LEFT
				entity.position.x = pos_x - pos_x % 32 + size[0]/2
				entity.position.y = pos_y + (32 - pos_y % 32) - size[1]/2
			else:				# 0 2
				#LEFT
				entity.position.x = pos_x - pos_x % 32 + size[0]/2
		elif is_solid[3]:		# 0 3
			entity.position.x = pos_x
			entity.position.y = pos_y
		else:					# 0
			pass
	elif is_solid[1]:
		if is_solid[2]:
			if is_solid[3]:		# 1 2 3
				entity.position.x = pos_x + (32 - pos_x % 32) - size[0]/2
				entity.position.y = pos_y + (32 - pos_y % 32) - size[1]/2
			else:				# 1 2
				entity.position.x = pos_x
				entity.position.y = pos_y
		elif is_solid[3]:		# 1 3
			entity.position.x = pos_x + (32 - pos_x % 32) - size[0]/2
		else:					# 1
			pass
	elif is_solid[2]:
		if is_solid[3]:			# 2 3
			entity.position.y = pos_y + (32 - pos_y % 32) - size[1]/2
		else:					# 2
			pass
	elif is_solid[3]:			# 3
		pass
	else:
		pass
		

for i in range(3):
	char.update(delta,i)    
	isSolid = ['','','','']
	reverted = False
	charPos = char.position.negative()
	loc = [(charPos.x+6,charPos.y+24),(charPos.x+6,charPos.y+38),(charPos.x+26,charPos.y+24),(charPos.x+26,charPos.y+38)]
	CCs = ['','','','']
	BBs = ['','','','']
	for j in range(len(loc)):
		chunkX = int(loc[j][0]/(32*CHUNK.floor.x))
		chunkY = int(loc[j][1]/(32*CHUNK.floor.y))
		blockX = int((loc[j][0]-chunkX*32*CHUNK.floor.x)/32)
		blockY = int((loc[j][1]-chunkY*32*CHUNK.floor.y)/32)
		CCs[j] = [chunkX, chunkY]
		BBs[j] = [blockX, blockY]
		for c in loadedChunks:
			if c.location.x == chunkX and c.location.y == chunkY:
				isSolid[j] = (c.floor.getComponent(blockX,blockY).isSolid() or c.environment.getComponent(blockX,blockY).isSolid())
				break
	for j in range(len(isSolid)):
		if isSolid[j]:
			char.update(-delta,i)
			reverted = True
			break
	if not reverted:
		break

for mob in mobs:
	mobDirection = mob.direction
	mobMoving = mob.isWalking()
	initialPosition = [mob.position.x, mob.position.y]
	try:
		for i in range(3):
			mobB4 = [mob.position.negative().x,mob.position.negative().y]
			mob.update(delta,mobDirection,mobMoving,i)
			bisSolid = ['','','','']
			reverted = False
			mobPos = mob.position.negative()
			mloc = [(mobPos.x+6,mobPos.y+24),(mobPos.x+6,mobPos.y+38),(mobPos.x+26,mobPos.y+24),(mobPos.x+26,mobPos.y+38)]
			CCs = ['','','','']
			BBs = ['','','','']
			for j in range(len(loc)):
				mchunkX = int(mloc[j][0]/(32*CHUNK.floor.x))
				mchunkY = int(mloc[j][1]/(32*CHUNK.floor.y))
				mblockX = int((mloc[j][0]-mchunkX*32*CHUNK.floor.x)/32)
				mblockY = int((mloc[j][1]-mchunkY*32*CHUNK.floor.y)/32)
				CCs[j] = [chunkX, chunkY]
				BBs[j] = [blockX, blockY]
				for c in loadedChunks:
					if c.location.x == mchunkX and c.location.y == mchunkY:
						bisSolid[j] = (c.floor.getComponent(mblockX,mblockY).isSolid() or c.environment.getComponent(mblockX,mblockY).isSolid())
						break
			for j in range(len(isSolid)):
				if bisSolid[j] == True:
					#print 'reverting to initial position'
					mob.setPosition(Vector(initialPosition[0],initialPosition[1]))
					reverted = True
					break
				elif type(bisSolid[j]) == str:
					mob.setPosition(Vector(initialPosition[0],initialPosition[1]))
					raise Exception('Mob touching unloaded chunk.')
			if not reverted:
				break
	except:
		s = ''
#                print 'mob touching unloaded chunk'
d = time.time() - previousTime
if d < 0.00001:
	d = 0.00001
FPS_S.pop(0)
FPS_S.append(1/d)
