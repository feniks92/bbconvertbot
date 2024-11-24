'''нельзя обращаться по индексу, использовать методы
pop, len, срезы
print
должен остаться внутри цикла'''


my_list = [1, 2, 3]
for i in my_list:
  print(i)


  def update_by_orm(self):
    self.model.objects.counter += 1
    self.model.update()
