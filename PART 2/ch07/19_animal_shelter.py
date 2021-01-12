# 7.7 연습문제
# 7.7.2 큐 - 큐와 동물 보호소
class Node(object):

    def __init__(self, animalName=None, animalKind=None, pointer=None):
        self.animalName = animalName    # 동물 이름
        self.animalKind = animalKind    # 동물 종류
        self.pointer = pointer          # 들어간 순서
        self.timestamp = 0


class AnimalShelter(object):

    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalNumber = 0

    def enqueue(self, animalName, animalKind):
        self.animalNumber += 1
        newAnimal = Node(animalName, animalKind)
        newAnimal.timestamp = self.animalNumber

        if animalKind == "cat":
            if not self.headCat:
                self.headCat = newAnimal
            if self.tailCat:
                self.tailCat.pointer = newAnimal
            self.tailCat = newAnimal

        elif animalKind == "dog":
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    def dequeueDog(self):
        if self.headDog:
            newAnimal = self.headDog
            self.headDog = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            print("개가 없습니다!")

    def dequeueCat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            print("고양이가 없습니다!")

    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif self.headDog and not self.headCat:
            return self.dequeueDog()
        elif self.headDog and self.headCat:
            if self.headDog.timestamp < self.headCat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            print("동물이 없습니다.")

    def _print(self):
        print("고양이: ")
        cats = self.headCat
        while cats:
            print("\t{0}".format(cats.animalName))
            cats = cats.pointer

        print("개: ")
        dogs = self.headDog
        while dogs:
            print("\t{0}".format(dogs.animalName))
            dogs = dogs.pointer


if __name__ == '__main__':
    qs = AnimalShelter()
    qs.enqueue("밥", "cat")
    qs.enqueue("미아", "cat")
    qs.enqueue("요다", "dog")
    qs.enqueue("울프", "dog")
    qs._print()

    print("하나의 개와 고양이에 대해서 dequeue를 실행합니다.")
    qs.dequeueDog()
    qs.dequeueCat()
    qs._print()
