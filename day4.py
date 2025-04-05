import copy

NO_OVERLAP = True

def check_matrix_is_square(m):
  for line in m:
    assert(len(line) == len(m))

def make_matrix(puzzle):
  line = []
  lines = []
  for v in puzzle:
    if (v == '\n'):
      if line != []:
        if line != ['\n']:
          lines.append(copy.copy(line))
          line = []
    else:
      if v != '\n':
        line.append(copy.copy(v))
  check_matrix_is_square(lines)
  return lines


# word search with gaps
def find_word_with_gaps(line, word):
  found = False
  ok = 0
  for v in line:
    if v == word[ok]:
      ok += 1
    if ok == len(word):
      found = True
      break
  if found:
    print("--M Matched: line -> {}, word -> {}".format(line,word))
  return found

def find_word(line, word):
  return line.startswith(word)

# traversors
def traverseToEast(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if x+i >= cnt:
        break
    elem_x = (x + i) % cnt
    line += m[y][elem_x]
  assert(line[0] == 'X')
  print("-- ({},{}) East line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToEast_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range = min(len_word, cnt-x)
	for i in range(cnt_range):
		assert(x+i < cnt)
		line += m[y][x+i]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToWest(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if x-i < 0:
        break
    elem_x = (x - i) % cnt
    line += m[y][elem_x]
  assert(line[0] == 'X')
  print("-- ({},{}) West line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToWest_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range = min(len_word, x+1)
	for i in range(cnt_range):
		assert(x-i >= 0)
		line += m[y][x-i]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToNorth(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if y-i < 0:
        break
    elem_y = (y - i) % cnt
    line += m[elem_y][x]
  assert(line[0] == 'X')
  print("-- ({},{}) North line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToNorth_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range = min(len_word, y+1)
	for i in range(cnt_range):
		assert(y-i >= 0)
		line += m[y-i][x]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToSouth(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if y+i >= cnt:
        break
    elem_y = (y + i) % cnt
    line += m[elem_y][x]
  assert(line[0] == 'X')
  print("-- ({},{}) South line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToSouth_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range = min(len_word, cnt-y)
	for i in range(cnt_range):
		assert(y+i < cnt)
		line += m[y+i][x]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToNorthEast(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if x+i >= cnt:
        break
      if y-i < 0:
        break
    elem_x = (x + i) % cnt
    elem_y = (y - i) % cnt
    line += m[elem_y][elem_x]
  assert(line[0] == 'X')
  print("-- ({},{}) North-East line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToNorthEast_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range_x = min(len_word, cnt-x)
	cnt_range_y = min(len_word, y+1)
	cnt_range = min(cnt_range_x, cnt_range_y)
	for i in range(cnt_range):
		assert(x+i < cnt)
		assert(y-i >= 0)
		line += m[y-i][x+i]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToSouthEast(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if x+i >= cnt:
        break
      if y+i >= cnt:
        break
    elem_x = (x + i) % cnt
    elem_y = (y + i) % cnt
    line += m[elem_y][elem_x]
  assert(line[0] == 'X')
  print("-- ({},{}) South-East line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToSouthEast_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range_x = min(len_word, cnt-x)
	cnt_range_y = min(len_word, cnt-y)
	cnt_range = min(cnt_range_x, cnt_range_y)
	for i in range(cnt_range):
		assert(x+i < cnt)
		assert(y+i < cnt)
		line += m[y+i][x+i]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToSouthWest(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if x-i < 0:
        break
      if y+i >= cnt:
        break
    elem_x = (x - i) % cnt
    elem_y = (y + i) % cnt
    line += m[elem_y][elem_x]
  assert(line[0] == 'X')
  print("-- ({},{}) South-West line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToSouthWest_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range_x = min(len_word, x+1)
	cnt_range_y = min(len_word, cnt-y)
	cnt_range = min(cnt_range_x, cnt_range_y)
	for i in range(cnt_range):
		assert(x-i >= 0)
		assert(y+i < cnt)
		line += m[y+i][x-i]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

def traverseToNorthWest(x,y,m,word):
  cnt = len(m)
  line = ""
  for i in range(cnt):
    if NO_OVERLAP:
      if x-i < 0:
        break
      if y-i < 0:
        break
    elem_x = (x - i) % cnt
    elem_y = (y - i) % cnt
    line += m[elem_y][elem_x]
  assert(line[0] == 'X')
  print("-- ({},{}) North-West line -> {}".format(x+1,y+1,line))
  return find_word(line, word)
  
def traverseToNorthWest_Func(x,y,m,word):
	cnt = len(m)
	len_word = len(word)
	line = ""
	cnt_range_x = min(len_word, x+1)
	cnt_range_y = min(len_word, y+1)
	cnt_range = min(cnt_range_x, cnt_range_y)
	for i in range(cnt_range):
		assert(x-i >= 0)
		assert(y-i >= 0)
		line += m[y-i][x-i]
	assert(line != "")
	assert(line[0] == 'X')
	return line.startswith(word)

# the solver
def day4(puzzle, word):
  # make matrix
  m = make_matrix(puzzle)
  # traverse all lines and cols and find (x,y) with 'X', because that's the first symbol of XMAS
  assert(word!="")
  cnt_found = 0
  firstSym = word[0]
  cnt = len(m)
  for y in range(cnt):
    for x in range(cnt):
      if firstSym == m[y][x]:
        # try all traversors
        # 90 deg traversors
        if traverseToEast(x,y,m,word) == True:
          print("To East from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToEast(x,y,m,word) == traverseToEast_Func(x,y,m,word))
        if traverseToWest(x,y,m,word) == True:
          print("To West from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToWest(x,y,m,word) == traverseToWest_Func(x,y,m,word))
        if traverseToNorth(x,y,m,word) == True:
          print("To North from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToNorth(x,y,m,word) == traverseToNorth_Func(x,y,m,word))
        if traverseToSouth(x,y,m,word) == True:
          print("To South from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToSouth(x,y,m,word) == traverseToSouth_Func(x,y,m,word))
        # diagonal traversors
        if traverseToNorthEast(x,y,m,word) == True:
          print("To North-East from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToNorthEast(x,y,m,word) == traverseToNorthEast_Func(x,y,m,word))
        if traverseToSouthEast(x,y,m,word) == True:
          print("To South-East from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToSouthEast(x,y,m,word) == traverseToSouthEast_Func(x,y,m,word))
        if traverseToSouthWest(x,y,m,word) == True:
          print("To South-West from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToSouthWest(x,y,m,word) == traverseToSouthWest_Func(x,y,m,word))
        if traverseToNorthWest(x,y,m,word) == True:
          print("To North-West from ({},{})".format(x+1,y+1))
          cnt_found += 1
        assert(traverseToNorthWest(x,y,m,word) == traverseToNorthWest_Func(x,y,m,word))
  return cnt_found



puzzle = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".replace("\n\r", "\n")

print(day4(puzzle,"XMAS"))
