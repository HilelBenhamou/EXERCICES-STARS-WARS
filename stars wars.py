# EXO STARS WARS
import random


class ForceWielder:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 15)
        self.wisdom = random.randint(1, 15)

    def train(self):
        raise NotImplementedError

    def is_jedi(self):
        raise NotImplementedError

    def fight(self, ennemy):
        # if isinstance(ennemy, self.__class__):
        jedix = 2 / ((1 / self.power) + (1 / self.wisdom))
        ennemyx = 2 / ((1 / ennemy.power) + (1 / ennemy.wisdom))
        print(
            f' Jedi : {self.name}:\n power : {self.power}, wisdom : {self.wisdom}, lightsaber : {self.lightsaber}, Harmonic Mean : {jedix}')
        print(
            f' Sith: {ennemy.name}:\n power : {ennemy.power}, wisdom : {ennemy.wisdom}, lightsaber : {ennemy.lightsaber}, Harmonic Mean : {ennemyx}')

        if jedix > ennemyx:
            print(f'{self.name} wins ! BABAAM ! Jedi Power !')
            self.train()

        elif jedix < ennemyx:
            print(f'{ennemy.name} wins ! Dark power ! Brrrrr')
            ennemy.train()
        # else:
        #     print('error')


class Jedi(ForceWielder):
    def __init__(self, name):
        super().__init__(name)
        self.wisdom += 10

        if self.power > self.wisdom:
            self.lightsaber = 'green'
        elif self.power < self.wisdom:
            self.lightsaber = 'blue'
        elif self.wisdom == self.power:
            self.lightsaber = 'violet'

    def train(self):
        self.wisdom = self.wisdom + random.randint(10, 20)
        self.power = self.power + random.randint(5, 15)

    def is_jedi(self):
        return True


class Sith(ForceWielder):
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Dark ' + self.name
        self.lightsaber = 'red'
        self.power += 10

    def train(self):
        self.power = self.wisdom + random.randint(10, 20)
        self.wisdom = self.power + random.randint(5, 15)

    def is_jedi(self):
        return False


jedis = [Jedi('Anakin'), Jedi('Obiwan Kenobi'), Jedi('Master Yoda')]
siths = [Sith('Vador'), Sith('Robot'), Sith('Fouchi')]

for jedi in jedis:
    for sith in siths:
        jedi.fight(sith)