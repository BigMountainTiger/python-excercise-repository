def run():
  dir = '/home/song/sandbox/python-excercise-repository/' \
    + 'b_01_apache-spark-excercise/test-files/a_03/{}'
    
  path_1 = dir.format('file-1.txt')
  path_2 = dir.format('file-2.txt')

  file_1 = open(path_1)
  lines_1 = file_1.read().splitlines()
  lines_1.append('Added an item')
  del lines_1[0]

  print(len(lines_1))
  print(lines_1)

if __name__ == "__main__":
  run()