class Category:
    categories = ["11", "22", "33", "44"]

    def poisk_category(self, category: str) -> bool:
        for i in range(len(self.categories)):
            if self.categories[i] == category:
                return True

    def add(self, category: str):
        if self.poisk_category(category):
            raise ValueError
        else:
            self.categories.append(category)
            return self.categories.index(category)

    def get(self, index: int):
        if int(index) > len(self.categories):
            return IndexError
        return self.categories[index]

    def delete(self, index: int):
        del self.categories[index]

    def update(self, index: int, category: str):
        if index < len(self.categories):
            if self.poisk_category(category):
                raise ValueError
            else:
                self.categories[index]=category
        else:
                if not self.poisk_category(category):
                    self.categories.append(category)
                else:
                    raise ValueError


my_categor = Category()
print(my_categor.add("88"))
print(my_categor.add("456"))
print(my_categor.categories)
print(my_categor.get(2))
my_categor.delete(2)
my_categor.update(3, "22")
print(my_categor.categories)
