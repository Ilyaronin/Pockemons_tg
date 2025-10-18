from random import randint

import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        
        self.hp = randint(20, 40)
        self.power = randint(5, 15)

        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
            else:
                if enemy.hp > self.power:
                    enemy.hp -= self.power
                    return f"Атака на покемона, здоровье вражеского покемона {enemy.hp}"
                else:
                    enemy.hp = 0
                    return f" Враг повержен"


    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def info(self):
        return f"Имя твоего покеомона: {self.name}, здоровье {self.hp}, атака: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Fighter(Pokemon):

    def attack(self, enemy):
        super_pow = randint(5,15)
        self.power += super_pow
        result = super().attack(enemy)
        self.сила -= super_pow
        return result + f"\nБоец применил супер-атаку силой:{result} "
    
    def info(self):
        return f"Имя твоего покеомона: {self.name}, здоровье {self.hp}, атака: {self.power}. У тебя покемон-боец"
    
class Wizard(Pokemon):
    

    def info(self):
        return f"Имя твоего покеомона: {self.name}, здоровье {self.hp}, атака: {self.power}. У тебя покемон-волшебник"
    
        

        

    



