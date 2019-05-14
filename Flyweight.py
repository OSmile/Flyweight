#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json
from typing import Dict

#Хранение общей части состояния, которая принадлежит 
#нескольким элементам
class Flyweight():
    def __init__(self, sharedState: str) -> None:
        self._sharedState = sharedState

    def operation(self, uniqueState: str) -> None:
        s = json.dumps(self._sharedState) 
        u = json.dumps(uniqueState)
        print(f"Element ({s}) and owner ({u})", end="")

#Создание объектов и управление ими
class FlyweightFactory():

    flyweightsDict: Dict[str, Flyweight] = {}
        
    #Функция для возвращения хеша строки состояния    
    def getKey(self, state: Dict) -> str:
        return " ".join(sorted(state))    

    def __init__(self, initialFlyweights: Dict) -> None:
        for state in initialFlyweights:
            self.flyweightsDict[self.getKey(state)] = Flyweight(state)

    
    #Возвращение существующего объекта или создание нового
    def getFlyweight(self, sharedState: Dict) -> Flyweight:
        key = self.getKey(sharedState)
        if not self.flyweightsDict.get(key):
            print("Creating new book")
            self.flyweightsDict[key] = Flyweight(sharedState)
        else:
            print("Already exist")
        return self.flyweightsDict[key]
    
    #Подсчет количества книг и их вывод
    def listFlyweights(self) -> None:
        count = len(self.flyweightsDict)
        print(f"There are {count} books in the library:")
        print("\n".join(map(str, self.flyweightsDict.keys())), end="")


#Добавление объектов в библиотеку        
def libraryObjects(
    factory: FlyweightFactory, owner: str,
    name: str, author: str, year: str) -> None:
    print("\n\nAdd a new book to the library:")
    flyweight = factory.getFlyweight([name, author, year])
    # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает
    # его методам легковеса.
    flyweight.operation([owner])


if __name__ == "__main__":
    #Добавим несколько уже существующих кник в библиотеке
    factory = FlyweightFactory([
        ["\"Brave new world\"", "Aldous Huxley", "1932"],
        ["\"The Da Vinci Cod\"", "Dan Brown", "2003"],
        ["\"To kill a mockingbird\"", "Harper Li", "1960"],
    ])
    
    #Вывод существующих книг на экран
    factory.listFlyweights()

    #Добаваление книг в библиотеку. Одна уже существующая, другая новая. 
    libraryObjects(
        factory, "Bob Marley", "\"A clockwork orange\"", "Anthony Burgess", "2011")

    libraryObjects(
        factory, "Prince Charles", "\"Brave new world\"", "Aldous Huxley", "1932")

    print("\n")

    factory.listFlyweights()

