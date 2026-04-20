class Soz:
    def __init__(self, soz):
        self.soz = soz

class Saralash:
    def __init__(self, sozlarni):
        self.sozlarni = sozlarni

    def saralash(self):
        return sorted(self.sozlarni, key=lambda x: len(x.soz))

sozlarni = [Soz("apple"), Soz("banana"), Soz("cherry"), Soz("date"), Soz("elderberry")]
saralash = Saralash(sozlarni)
print([soz.soz for soz in saralash.saralash()])
```

```python
class Soz:
    def __init__(self, soz):
        self.soz = soz

class Saralash:
    def __init__(self, sozlarni):
        self.sozlarni = sozlarni

    def saralash(self):
        return sorted(self.sozlarni, key=lambda x: len(x.soz), reverse=True)

sozlarni = [Soz("apple"), Soz("banana"), Soz("cherry"), Soz("date"), Soz("elderberry")]
saralash = Saralash(sozlarni)
print([soz.soz for soz in saralash.saralash()])
