class FileIterator:
  def __init__(self, filename):
    self.file = open(filename)

  def __iter__(self):
    return self

  def __next__(self):
    line = self.file.readline()
    if line != '':
      return line
    else:
      self.file.close()
      raise StopIteration

for i,line in enumerate(FileIterator('C:\Workspace\Python\.txt\wordlist_de_8k.txt')):
  print(f"{i + 1} " + line)