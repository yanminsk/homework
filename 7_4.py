class Category:
    categories = [
        {"name": "11", "is_published": False},
        {"name": "22", "is_published": False},
        {"name": "33", "is_published": False},
        {"name": "44", "is_published": False}
                  ]

    def poisk_category(self, category: str) -> bool:
        for i in range(len(self.categories)):
            if self.categories[i].get("name") == category:
                return True

    def add(self, category: str, is_published: bool):
        if self.poisk_category(category):
             raise ValueError
        else:
            self.categories.append({"name": category, "is_published": False})
            return self.categories.index({"name": category, "is_published": False})

    def get(self, index: int):
        if int(index) > len(self.categories):
            return IndexError
        return self.categories[index]

    def delete(self, index: int):
        del self.categories[index]

    def update(self, index: int, category: str, is_published: bool):
        if index < len(self.categories):
            if self.poisk_category(category):
                raise ValueError
            else:
                self.categories[index]={"name": category, "is_published": False}
        else:
                if not self.poisk_category(category):
                    self.categories.append({"name": category, "is_published": False})
                else:
                    raise ValueError

    def make_published(self, index: int):
        if index < len(self.categories):
            self.categories[index]={"name": self.categories[index].get("name"), "is_published": True}
        else:
            raise IndexError

    def make_unpublished(self, index: int):
        if index < len(self.categories):
            self.categories[index]={"name": self.categories[index].get("name"), "is_published": False}
        else:
            raise IndexError

my_categor = Category()
print(my_categor.add("78",False))
print(my_categor.categories)
print(my_categor.get(2))
my_categor.delete(2)
my_categor.update(9, "789", False)
my_categor.make_published(2)
print(my_categor.categories)
my_categor.make_unpublished(2)
print(my_categor.categories)

