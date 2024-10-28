class Foo:
  def __init__(self, x = None):
    self._x = x

  @property
  def x(self):
    return self._x or 0

  @x.setter
  def x(self, value):
    _x = self._x or 0 
    _value = value or 0
    self._x = _x + _value

  # def increment(self, value):
  #   _x = self._x or 0
  #   _value = value or 0
  #   self._x += _value
  #   return self._x

  @x.deleter
  def x(self):
    if self._x == 0:
      self._x = 0
    elif self._x < 0:
      pass
    else:
      self._x -= 1
    # del self._x




foo = Foo(10)
print(foo.x)
foo.x = 10
# foo.increment(10)
print(foo.x)
del foo.x
print(foo.x)