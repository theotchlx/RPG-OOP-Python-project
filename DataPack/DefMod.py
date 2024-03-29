###################################################
# This module defines the functions used in-game
# Made by Théo Tchilinguirian, Saturday 08/02/2020
###################################################


# Imports # ------------------------------------------------------------------------------------------------------------

import os
import pickle
import random
# import pygame
# import tkinter


# Classes Definitions # ------------------------------------------------------------------------------------------------

class Player:

    def __init__(self, cls, lvl, mon, hp, atk, dfs, chp, klc, bhp, kcm):

        self.player_stats = {'CLASS': cls, 'LEVEL': lvl, 'MONEY': mon, 'HP': hp, 'ATTACK': atk, 'DEFENSE': dfs,
                              'CHAPTER': chp, 'KILLCOUNT': klc, 'BASEHP': bhp, 'KILLCOUNTMAX': kcm}

    def set_stat_value(self, stat_key, stat_new_value):

        self.player_stats[stat_key] = stat_new_value


    def get_player_stats(self):

        return self.player_stats


    def set_current_new_chapter(self, player_list, pseudonyme):

        current_chapter = self.player_stats['CHAPTER']

        if current_chapter == 'I: THE RUINS':
            new_chapter = 'II: DESOLATED LAND'

        elif current_chapter == 'II: DESOLATED LAND':
            new_chapter = 'III: CURSED TOWER'

        elif current_chapter == 'II: DESOLATED LAND':
            new_chapter = 'III: CURSED TOWER'

        elif current_chapter == 'III: CURSED TOWER':
            new_chapter = 'IV: MISTYC STAGE'

        self.set_stat_value('CHAPTER', new_chapter)

        player_entity = self
        player_list[pseudonyme][1] = player_entity

        return player_list, player_entity


    def player_level_up(self, player_list, pseudonyme):

        kill_count_max = self.player_stats['KILLCOUNTMAX']
        current_player_kill_count = self.player_stats['KILLCOUNT']

        if current_player_kill_count % kill_count_max == 0 and current_player_kill_count != 0:

            for stat_key, current_stat_value in self.player_stats.items():

                if stat_key == 'LEVEL':
                    self.set_stat_value(stat_key, current_stat_value + 1)

                elif stat_key == 'KILLCOUNTMAX':
                    self.set_stat_value(stat_key, current_stat_value + 3)  # VERY TIED to line 308 'ask_change_chapter' --> condition if ... and current_player_kill_count % kill_count_max == kill_count_max - 3(HERE) and ...

                elif stat_key == 'BASEHP':
                    new_stat_value = round(current_stat_value + (current_stat_value * 15) / 100)
                    self.set_stat_value(stat_key, new_stat_value)
                    self.set_stat_value('HP', new_stat_value)  # The player gets full hp every level

                elif stat_key == 'BASEMANA' or stat_key == 'BASEMANA' or stat_key == 'BASEVIGOR':
                    new_stat_value = round(current_stat_value + (current_stat_value * 15) / 100)
                    self.set_stat_value(stat_key, new_stat_value)
                    self.set_stat_value(stat_key[4:], new_stat_value)

                elif stat_key == 'ATTACK' or stat_key == 'DEFENSE':
                    new_stat_value = round(current_stat_value + (current_stat_value / 10))
                    self.set_stat_value(stat_key, new_stat_value)

            player_list[pseudonyme][1] = self

            current_level = self.player_stats['LEVEL']
            print("Congrats ! You are now level {}.".format(current_level))

        return player_list


class Warrior(Player):

    def __init__(self, vig = 80, bvg = 80):
        Player.__init__(self, cls = 'Warrior', lvl = 1, mon = 0, hp = 100, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 100, kcm = 5)
        self.set_stat_value('VIGOR', vig)
        self.set_stat_value('BASEVIGOR', bvg)


class Soldier(Player):

    def __init__(self, vig = 90, bvg = 90):
        Player.__init__(self, cls='Soldier', lvl = 1, mon = 0, hp = 90, atk = 40, dfs = 60, chp = 'I: THE RUINS', klc = 0, bhp = 90, kcm = 5)
        self.set_stat_value('VIGOR', vig)
        self.set_stat_value('BASEVIGOR', bvg)


class Gladiator(Player):

    def __init__(self, vig = 100, bvg = 100):
        Player.__init__(self, cls='Gladiator', lvl = 1, mon = 0, hp = 80, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 80, kcm = 5)
        self.set_stat_value('VIGOR', vig)
        self.set_stat_value('BASEVIGOR', bvg)


class Mage(Player):

    def __init__(self, mana = 90, bmn = 90):
        Player.__init__(self, cls='Mage', lvl = 1, mon = 0, hp = 100, atk = 25, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 100, kcm = 5)
        self.set_stat_value('MANA', mana)
        self.set_stat_value('BASEMANA', bmn)


class Sorcerer(Player):

    def __init__(self, mana = 80, bmn = 80):
        Player.__init__(self, cls='Sorcerer', lvl = 1, mon = 0, hp = 110, atk = 30, dfs = 30, chp = 'I: THE RUINS', klc = 0, bhp = 110, kcm = 5)
        self.set_stat_value('MANA', mana)
        self.set_stat_value('BASEMANA', bmn)



class Priest(Player):

    def __init__(self, mana = 110, bmn = 110):
        Player.__init__(self, cls='Priest', lvl = 1, mon = 0, hp = 75, atk = 20, dfs = 25, chp = 'I: THE RUINS', klc = 0, bhp = 75, kcm = 5)
        self.set_stat_value('MANA', mana)
        self.set_stat_value('BASEMANA', bmn)


# Ennemy Entities # ----------------------------------------------------------------------------------------------------

class Ennemy:

    def __init__(self, typ, hp, atk, dfs, chp, mnw):
        self.ennemy_stats = {'TYPE': typ, 'HP': hp, 'ATTACK': atk, 'DEFENSE': dfs, 'CHAPTER': chp, 'MONEYWORTH': mnw}


    def set_stat_value(self, stat_key, stat_new_value):
        self.ennemy_stats[stat_key] = stat_new_value


    def get_ennemy_stats(self):

        return self.ennemy_stats


class Bat(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Bat', hp = 5, atk = 3, dfs = 0, chp = 'I: THE RUINS', mnw = 1)


class Slime(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Slime', hp = 10, atk = 5, dfs = 0, chp = 'I: THE RUINS', mnw = 2)


class Spider(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Spider', hp = 15, atk = 8, dfs = 3, chp = 'I: THE RUINS', mnw = 4)


class RabidWolf(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Rabid Wolf', hp = 25, atk = 12, dfs = 5, chp = 'II: DESOLATED LAND', mnw = 5)


class DarkWizard(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Dark Wizard', hp = 50, atk = 20, dfs = 10, chp = 'II: DESOLATED LAND', mnw = 10)


class CorruptedSpirit(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Corrupted Spirit', hp = 75, atk = 25, dfs = 8, chp = 'II: DESOLATED LAND', mnw = 20)


class Skeleton(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Skeleton', hp = 40, atk = 10, dfs = 5, chp = 'III: CURSED TOWER', mnw = 15)


class Goblin(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Goblin', hp = 10, atk = 5, dfs = 8, chp = 'III: CURSED TOWER', mnw = 5)


class FallenWarrior(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Fallen Warrior', hp = 65, atk = 25, dfs = 15, chp = 'III: CURSED TOWER', mnw = 30)


class Dragon(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Dragon', hp = 250, atk = 45, dfs = 25, chp = 'IV: MISTYC STAGE', mnw = 500)


# File Manipulation Functions Definitions # ----------------------------------------------------------------------------

def charge_file():
    if os.path.exists('../DataPack/DataFile'):
        with open('../DataPack/DataFile', 'rb') as charge_file:
            file_depickler = pickle.Unpickler(charge_file)
            player_list = file_depickler.load()
    else:
        player_list = dict()

    return player_list


def save_file(player_list):
    with open('../DataPack/DataFile', 'wb') as save_file:
        file_pickler = pickle.Pickler(save_file)
        file_pickler.dump(player_list)


# Input/Print and Conditions Functions # -------------------------------------------------------------------------------

def check_answer_get_yes_no(question):
    answer = ""
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print(question)
        answer = input(">>> ")
        if answer.lower() != 'yes' and answer.lower() != 'no':
            print("Answer by 'yes' or 'no'.")

    return answer.lower()


def start_screen():
    print(100 * '-' + '\n' + "Welcome to... 'RPG-The Game' !!".center(100) + '\n' + (75 * '-').center(100) + '\n')


def welcome(pseudonyme, chapter):
    print(100 * '-' + '\n' + "Welcome, {}, to CHAPTER {} . . .".center(100).format(pseudonyme, chapter) + '\n' + (75 * '-').center(100) + '\n')


def show_player_list(player_list):
    print("Player list:")
    for players in player_list.keys():
        print(players)


def check_answer_get_class_stats():
    end = False
    while end == False:
        try:
            answer_class = int(input("""What class do you want to be ?
            EASY:
            1. Warrior
            2. Mage

            MEDIUM:
            3. Soldier
            4. Sorcerer

            HARD:
            5. Gladiator
            6. Priest
            >>> """))
            end = True

        except ValueError:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue

        if answer_class == 1:
            return 'Warrior'
        elif answer_class == 2:
            return 'Mage'
        elif answer_class == 3:
            return 'Soldier'
        elif answer_class == 4:
            return 'Sorcerer'
        elif answer_class == 5:
            return 'Gladiator'
        elif answer_class == 6:
            return 'Priest'
        else:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue


def ask_change_chapter(player_list, pseudonyme, player_entity):
    current_player_kill_count = player_entity.get_player_stats()['KILLCOUNT']
    kill_count_max = player_entity.get_player_stats()['KILLCOUNTMAX']
    player_current_level = player_entity.get_player_stats()['LEVEL']
    player_current_chapter = player_entity.get_player_stats()['CHAPTER']

    if player_current_level % 5 == 0 and current_player_kill_count % kill_count_max == kill_count_max - 3 and player_current_chapter != 'IV: MISTYC STAGE':

        answer = check_answer_get_yes_no("You are level {}. Do you want do go to the next chapter ?". format(player_current_level))
        if answer == 'yes':
            player_entity.set_current_new_chapter(player_list, pseudonyme)
            welcome(pseudonyme, player_entity.get_player_stats()['CHAPTER'])
        else:
            print("It will be harder next time...")


def get_menu_choice(player_entity, player_list, pseudonyme):
    end = False
    while end == False:
        try:
            print('\n' + (75 * '-').center(100) + '\n' + "GAME MENU".center(100) + '\n' + (75 * '-').center(100))
            answer_menu = int(input("""
            1. Return to battle
            2. Go to the Shop
            3. See your Stats
            4. Quit and Save the Game
            >>> """))
            print('\n')
            end = True

        except ValueError:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue

        if answer_menu == 1:
            current_ennemy = current_ennemy_entity_maker(player_list, pseudonyme)
            print("You roam around the battle field looking for an ennemy...")
            del_player = battle(player_list, pseudonyme, current_ennemy)

            if del_player == 'del player_list':
                return del_player

        elif answer_menu == 2:
            get_shop_choice(player_entity)
            end = True

        elif answer_menu == 3:
            show_player_stats(player_entity)
            end = True

        elif answer_menu == 4:

            return 'quit'

        else:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue

    return 'no quitting'


def get_shop_choice(player_entity):
    end = False
    while end == False:
        try:
            print('\n' + (75 * '-').center(100) + '\n' + "SHOP".center(100) + '\n' + (75 * '-').center(100) + '\n')
            print("You have {}$".format(player_entity.get_player_stats()['MONEY']))

            answer_shop = int(input("""Welcome to the shop, fellow adventurer !!
            What do you want to buy ? We have:
            1- Healing Potion (regens 20 hp) for 15$
            2- Restoration Potion (regens 20 mana or vigor) for 15$
            3- Armor (+ 5 DFS) for 25$
            4- Weapons (+ 5 ATK) for 25$
            5- Quit
            >>> """))
            end = True

        except ValueError:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue

        if answer_shop == 1:
            buy_item(answer_shop, player_entity, 15)
            continue

        elif answer_shop == 2:
            buy_item(answer_shop, player_entity, 15)
            continue

        elif answer_shop == 3:
            buy_item(answer_shop, player_entity, 25)
            continue

        elif answer_shop == 4:
            buy_item(answer_shop, player_entity, 25)
            continue

        elif answer_shop == 5:
            end = True

        else:
            print("Your answer is not correct. Choose a number between 1 and 5")
            continue


def show_player_stats(player_entity):
    print("Your Stats:")
    try:
        print("""    {0}/{2} --> {1}/{3}
    {4}/{6} --> {5}/{7}
    {16} --> {17}
    {18} --> {19}
    {8} --> {9}
    {10} --> {11}
    {12} --> {13}
    {14} --> {15}
        """.format("HP", player_entity.get_player_stats()['HP'],
                   "MAX HP", player_entity.get_player_stats()['BASEHP'],
                   "MANA", player_entity.get_player_stats()['MANA'],
                   "MAX MANA", player_entity.get_player_stats()['BASEMANA'],
                   "LEVEL", player_entity.get_player_stats()['LEVEL'],
                   "MONEY", player_entity.get_player_stats()['MONEY'],
                   "KILL COUNT", player_entity.get_player_stats()['KILLCOUNT'],
                   "KILLS TO NEXT LVL", player_entity.get_player_stats()['KILLCOUNTMAX'],
                   "ATTACK PTS", player_entity.get_player_stats()['ATTACK'],
                   "DEFENSE PTS", player_entity.get_player_stats()['DEFENSE']))

    except KeyError:
        print("""    {0}/{2} --> {1}/{3}
    {4}/{6} --> {5}/{7}
    {16} --> {17}
    {18} --> {19}
    {8} --> {9}
    {10} --> {11}
    {12} --> {13}
    {14} --> {15}
        """.format("HP", player_entity.get_player_stats()['HP'],
                   "MAX HP", player_entity.get_player_stats()['BASEHP'],
                   "VIGOR", player_entity.get_player_stats()['VIGOR'],
                   "MAX VIGOR", player_entity.get_player_stats()['BASEVIGOR'],
                   "LEVEL", player_entity.get_player_stats()['LEVEL'],
                   "MONEY", player_entity.get_player_stats()['MONEY'],
                   "KILL COUNT", player_entity.get_player_stats()['KILLCOUNT'],
                   "KILLS TO NEXT LVL", player_entity.get_player_stats()['KILLCOUNTMAX'],
                   "ATTACK PTS", player_entity.get_player_stats()['ATTACK'],
                   "DEFENSE PTS", player_entity.get_player_stats()['DEFENSE']))
    input()


def show_current_ennemy_stats(current_enemy):
    ennemy_type = current_enemy.get_ennemy_stats()['TYPE']
    print("{}'s Health:".format(ennemy_type))
    print("""{0} --> {1}
    """.format("HP", current_enemy.get_ennemy_stats()['HP']))
    input()

# Job Functions # ------------------------------------------------------------------------------------------------------

def mana_vigor_regeneration(player_entity, player_energy_class):
    if player_energy_class == 'MANA':
        new_player_mana = player_entity.get_player_stats()['MANA'] + 5
        player_entity.set_stat_value('MANA', new_player_mana)

    elif player_energy_class == 'VIGOR':
        new_player_vigor = player_entity.get_player_stats()['VIGOR'] + 5
        player_entity.set_stat_value('VIGOR', new_player_vigor)


def can_player_attack(player_entity, player_energy_class):
    if player_energy_class == 'MANA':
        player_mana = player_entity.get_player_stats()['MANA']

        if player_mana <= 0:

            return False

        else:

            return True

    elif player_energy_class == 'VIGOR':
        player_vigor = player_entity.get_player_stats()['VIGOR']

        if player_vigor <= 0:

            return False

        else:

            return True


def battle_check_player_first(player_list, pseudonyme, player_entity, current_ennemy, current_ennemy_type, player_energy_class, player_attack_points_on_ennemy, player_energy_used, current_ennemy_attack_points_on_player):

    while get_if_player_dead(player_entity) == False and get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy) == False:

        player_attack_on_ennemy(player_entity, player_attack_points_on_ennemy, current_ennemy, player_energy_class, player_energy_used)  # Prints 'You attack ennemy'
        print("You used {} {} but regenerated 5 {}".format(player_energy_used, player_energy_class, player_energy_class))
        show_current_ennemy_stats(current_ennemy)

        if get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy) == True and get_if_player_dead(player_entity) == False:
            print("{} is dead.".format(current_ennemy_type))

            return 'ennemy dead'

        elif can_player_attack(player_entity, player_energy_class) == False:
            print("You cannot attack yet, you are out of {}".format(player_energy_class.lower()))
            mana_vigor_regeneration(player_entity, player_energy_class)
            continue

        elif get_if_player_dead(player_entity) == True:
            print("You died. your name will forever be forgotten. May you and your miserable adventure go to the void and never return.")

            return 'player dead'

        ennemy_attack_on_player(current_ennemy_attack_points_on_player, player_entity, current_ennemy)
        show_player_stats(player_entity)

        if get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy) == True and get_if_player_dead(player_entity) == False:
            print("{} is dead.".format(current_ennemy_type))

            return 'ennemy dead'

        elif can_player_attack(player_entity, player_energy_class) == False:
            print("You cannot attack yet, you are out of {}".format(player_energy_class.lower()))
            mana_vigor_regeneration(player_entity, player_energy_class)
            continue

        elif get_if_player_dead(player_entity) == True:
            print("You died. your name will forever be forgotten. May you and your miserable adventure go to the void and never return.")

            return 'player dead'


def battle_check_ennemy_first(player_list, pseudonyme, player_entity, current_ennemy, current_ennemy_type, player_energy_class, player_attack_points_on_ennemy, player_energy_used, current_ennemy_attack_points_on_player):

    while get_if_player_dead(player_entity) == False and get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy) == False:

        ennemy_attack_on_player(current_ennemy_attack_points_on_player, player_entity, current_ennemy)
        show_player_stats(player_entity)

        if get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy) == True and get_if_player_dead(player_entity) == False:
            print("{} is dead.".format(current_ennemy_type))

            return 'ennemy dead'

        elif can_player_attack(player_entity, player_energy_class) == False:
            print("You cannot attack yet, you are out of {}".format(player_energy_class.lower()))
            mana_vigor_regeneration(player_entity, player_energy_class)
            continue

        elif get_if_player_dead(player_entity) == True:
            print("You died. your name will forever be forgotten. May you and your miserable adventure go to the void and never return.")

            return 'player dead'

        player_attack_on_ennemy(player_entity, player_attack_points_on_ennemy, current_ennemy, player_energy_class, player_energy_used)
        print("You used {} {} but regenerated 5 {}".format(player_energy_used, player_energy_class, player_energy_class))
        show_current_ennemy_stats(current_ennemy)

        if get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy) == True and get_if_player_dead(player_entity) == False:
            print("{} is dead.".format(current_ennemy_type))

            return 'ennemy dead'

        elif can_player_attack(player_entity, player_energy_class) == False:
            print("You cannot attack yet, you are out of {}".format(player_energy_class.lower()))
            mana_vigor_regeneration(player_entity, player_energy_class)
            continue

        elif get_if_player_dead(player_entity) == True:
            print("You died. your name will forever be forgotten. May you and your miserable adventure go to the void and never return.")

            return 'player dead'


def battle(player_list, pseudonyme, current_ennemy):
    player_entity = player_list[pseudonyme][1]
    current_ennemy_type = current_ennemy.get_ennemy_stats()['TYPE']
    player_energy_class, player_energy_used = get_player_mana_or_vigor_used_on_attack(player_entity)
    who_attacks_first = get_who_attacks_first()  # returns 'PLAYER' or 'ENNEMY'

    player_attack_points_on_ennemy = get_player_attack_points_on_ennemy(player_entity, current_ennemy)
    current_ennemy_attack_points_on_player = get_ennemy_attack_points_on_player(player_entity, current_ennemy)

    if who_attacks_first == 'PLAYER':
        print("You found a {} !".format(current_ennemy_type))
        show_current_ennemy_stats(current_ennemy)

        who_dead = battle_check_player_first(player_list, pseudonyme, player_entity, current_ennemy, current_ennemy_type, player_energy_class, player_attack_points_on_ennemy, player_energy_used, current_ennemy_attack_points_on_player)
        if who_dead == 'ennemy dead':
            del current_ennemy
            show_player_stats(player_entity)

        elif who_dead == 'player dead':
            return 'del player_list'

    elif who_attacks_first == 'ENNEMY':
        print("A {} found you !".format(current_ennemy_type))
        show_current_ennemy_stats(current_ennemy)

        who_dead = battle_check_ennemy_first(player_list, pseudonyme, player_entity, current_ennemy, current_ennemy_type, player_energy_class, player_attack_points_on_ennemy, player_energy_used, current_ennemy_attack_points_on_player)

        if who_dead == 'ennemy dead':
            del current_ennemy
            show_player_stats(player_entity)

        elif who_dead == 'player dead':
            return 'del player_list'


def get_set_is_ennemy_dead_and_add_player_money_if_it_is_dead(player_list, pseudonyme, current_ennemy):
    player_entity = player_list[pseudonyme][1]
    current_ennemy_hp = current_ennemy.get_ennemy_stats()['HP']
    current_ennemy_money_earnable = current_ennemy.get_ennemy_stats()['MONEYWORTH']
    player_kill_count = player_entity.get_player_stats()['KILLCOUNT']
    player_money = player_entity.get_player_stats()['MONEY']

    if current_ennemy_hp <= 0:
        player_entity.set_stat_value('KILLCOUNT', player_kill_count + 1)
        player_entity.set_stat_value('MONEY', player_money + current_ennemy_money_earnable)
        del current_ennemy

        return True

    else:

        return False


def get_if_player_dead(player_entity):
    player_hp = player_entity.get_player_stats()['HP']

    if player_hp <= 0:

        return True

    else:

        return False


def deduct_money(player_entity, price):
    current_money = player_entity.get_player_stats()['MONEY']

    if current_money <= 0:
        can_pay = 'no'
        new_money = 0
        player_entity.set_stat_value('MONEY', new_money)

    elif current_money >= price:
        can_pay = 'yes'
        new_money = current_money - price
        player_entity.set_stat_value('MONEY', new_money)

    elif current_money < price:
        can_pay = 'no'

    return can_pay


def buy_item(answer_shop, player_entity, price):
    current_money = player_entity.get_player_stats()['MONEY']

    if answer_shop == 1:
        if player_entity.get_player_stats()['HP'] == player_entity.get_player_stats()['BASEHP']:
            print("You have MAX HP")

        else:
            can_pay = deduct_money(player_entity, price)

            if can_pay == 'yes':
                player_entity.set_stat_value('HP', player_entity.get_player_stats()['HP'] + 20)
                print("You now have {} HP.".format(player_entity.get_player_stats()['HP']))

            else:
                print("You can't pay, you don't have enough money.")
                print("You have {} money".format(current_money))

    elif answer_shop == 2:
        try:
            if player_entity.get_player_stats()['MANA'] == player_entity.get_player_stats()['BASEMANA']:
                print("You have MAX MANA")

            else:
                can_pay = deduct_money(player_entity, price)

                if can_pay == 'yes':
                    player_entity.set_stat_value('MANA', player_entity.get_player_stats()['MANA'] + 20)
                    print("You now have {} MANA.".format(player_entity.get_player_stats()['MANA']))

                else:
                    print("You can't pay, you don't have enough money.")
                    print("You have {} money".format(current_money))

        except KeyError:
            if player_entity.get_player_stats()['VIGOR'] == player_entity.get_player_stats()['BASEVIGOR']:
                print("You have MAX VIGOR")

            else:
                can_pay = deduct_money(player_entity, price)

                if can_pay == 'yes':
                    player_entity.set_stat_value('VIGOR', player_entity.get_player_stats()['VIGOR'] + 20)
                    print("You now have {} VIGOR.".format(player_entity.get_player_stats()['VIGOR']))

                else:
                    print("You can't pay, you don't have enough money.")
                    print("You have {} money".format(current_money))

    elif answer_shop == 3:
        can_pay = deduct_money(player_entity, price)

        if can_pay == 'yes':
            player_entity.set_stat_value('DEFENSE', player_entity.get_player_stats()['DEFENSE'] + 5)
            print("You now have {} DEFENSE.".format(player_entity.get_player_stats()['DEFENSE']))

        else:
            print("You can't pay, you don't have enough money.")
            print("You have {} money".format(current_money))

    elif answer_shop == 4:
        can_pay = deduct_money(player_entity, price)

        if can_pay == 'yes':
            player_entity.set_stat_value('ATTACK', player_entity.get_player_stats()['ATTACK'] + 5)
            print("You now have {} ATTACK.".format(player_entity.get_player_stats()['ATTACK']))

        else:
            print("You can't pay, you don't have enough money.")
            print("You have {} money".format(current_money))


def player_entity_maker(player_list, pseudonyme, password):
    """
    Tied to 'check_answer_get_class_stats'
    adds a player with default settings to the player list
    """

    end = False
    while end == False:
        cls = check_answer_get_class_stats()
        if cls == 'Warrior':
            player_entity = Warrior()
            end = True
        elif cls == 'Mage':
            player_entity = Mage()
            end = True
        elif cls == 'Soldier':
            player_entity = Soldier()
            end = True
        elif cls == 'Sorcerer':
            player_entity = Sorcerer()
            end = True
        elif cls == 'Gladiator':
            player_entity = Gladiator()
            end = True
        elif cls == 'Priest':
            player_entity = Priest()
            end = True
        else:
            continue

    player_list[pseudonyme] = [password, player_entity]

    return player_list, pseudonyme, password, player_entity


def current_ennemy_entity_maker(player_list, pseudonyme):
    player_entity = player_list[pseudonyme][1]
    current_chapter = player_entity.get_player_stats()['CHAPTER']
    current_ennemy_spawned_type_range = random.randint(1, 100)

    if current_chapter == 'I: THE RUINS':
        if 0 < current_ennemy_spawned_type_range <= 40:  # 40% chances to appear
            current_ennemy = Slime()

        elif 40 < current_ennemy_spawned_type_range <= 75:
            current_ennemy = Bat()

        elif 75 < current_ennemy_spawned_type_range <= 100:
            current_ennemy = Spider()

    elif current_chapter == 'II: DESOLATED LAND':
        if 0 < current_ennemy_spawned_type_range <= 75:
            current_ennemy = RabidWolf()

        elif 75 < current_ennemy_spawned_type_range <= 90:
            current_ennemy = DarkWizard()

        elif 90 < current_ennemy_spawned_type_range <= 100:
            current_ennemy = CorruptedSpirit()

    elif current_chapter == 'III: CURSED TOWER':
        if 0 < current_ennemy_spawned_type_range <= 25:
            current_ennemy = Skeleton()

        elif 25 < current_ennemy_spawned_type_range <= 85:
            current_ennemy = Goblin()

        elif 85 < current_ennemy_spawned_type_range <= 100:
            current_ennemy = FallenWarrior()

    elif current_chapter == 'IV: MISTYC STAGE':  # 100% chances to appear
        current_ennemy = Dragon()

    return current_ennemy


def check_login(player_list, pseudonyme, password):
    if player_list[pseudonyme][0] == password:
        return True
    else:
        return False


def player_in_player_list(player_list, pseudonyme):
    if pseudonyme in player_list.keys():
        return True
    else:
        return False


def ennemy_entity_maker(Type, hp, ):
    pass
    # if Type == Undead and player.cls == "Priest":
    #     damage_done += damage_done / 10  # 10% more damage done by the priest on undead ennemies


def get_check_pseudonyme(pseudonyme):
    if len(pseudonyme) <= 4:
        print('')


def get_check_password(password):
    if len(password) <= 4:
        print('')


def get_player_attack_points_on_ennemy(player_entity, current_ennemy):
    player_attack_points = player_entity.get_player_stats()['ATTACK']
    current_ennemy_defense_points = current_ennemy.get_ennemy_stats()['DEFENSE']

    if player_attack_points > current_ennemy_defense_points:
        player_attack_points_on_ennemy = player_attack_points - current_ennemy_defense_points

    else:
        player_attack_points_on_ennemy = 1

    return player_attack_points_on_ennemy


def get_ennemy_attack_points_on_player(player_entity, current_ennemy):
    current_ennemy_attack_points = current_ennemy.get_ennemy_stats()['ATTACK']
    player_defense_points = player_entity.get_player_stats()['DEFENSE']

    if current_ennemy_attack_points > player_defense_points:
        current_ennemy_attack_points_on_player = current_ennemy_attack_points - player_defense_points

    else:
        current_ennemy_attack_points_on_player = 1

    return current_ennemy_attack_points_on_player


def get_player_mana_or_vigor_used_on_attack(player_entity):
    if 'MANA' in player_entity.get_player_stats():
        base_mana = player_entity.get_player_stats()['BASEMANA']
        mana_used = round(base_mana / 10)

        return 'MANA', mana_used

    elif 'VIGOR' in player_entity.get_player_stats():
        base_vigor = player_entity.get_player_stats()['BASEVIGOR']
        vigor_used = round(base_vigor / 10)

        return 'VIGOR', vigor_used


def player_attack_on_ennemy(player_entity, player_attack_points_on_ennemy, current_ennemy, player_energy_class, player_energy_used):

    current_ennemy_type = current_ennemy.get_ennemy_stats()['TYPE']
    print("You attack {} !".format(current_ennemy_type))

    current_ennemy_hp = current_ennemy.get_ennemy_stats()['HP']

    if can_player_attack(player_entity, player_energy_class) == True:
        if current_ennemy_hp <= player_attack_points_on_ennemy:
            current_ennemy_new_hp = 0

        else:
            current_ennemy_new_hp = current_ennemy_hp - player_attack_points_on_ennemy

        current_ennemy.set_stat_value('HP', current_ennemy_new_hp)

        if player_energy_class == 'MANA':
            player_mana = player_entity.get_player_stats()['MANA']
            new_player_mana = player_mana - player_energy_used
            player_entity.set_stat_value('MANA', new_player_mana)

        elif player_energy_class == 'VIGOR':
            player_vigor = player_entity.get_player_stats()['VIGOR']
            new_player_vigor = player_vigor - player_energy_used
            player_entity.set_stat_value('VIGOR', new_player_vigor)

        mana_vigor_regeneration(player_entity, player_energy_class)

    # Does not return anything, works directly on the ennemy object that stays changed even out of the function


def ennemy_attack_on_player(current_ennemy_attack_points_on_player, player_entity, current_ennemy):

    current_ennemy_type = current_ennemy.get_ennemy_stats()['TYPE']
    print("{} attacks you !".format(current_ennemy_type))

    player_hp = player_entity.get_player_stats()['HP']

    if player_hp <= current_ennemy_attack_points_on_player:
        player_new_hp = 0

    else:
        player_new_hp = player_hp - current_ennemy_attack_points_on_player

    player_entity.set_stat_value('HP', player_new_hp)

    # Does not return anything, works directly on the player object that stays changed even out of the function


def get_who_attacks_first():
    random_half = random.randint(1, 100)

    if 0 < random_half <= 100:
        return 'PLAYER'

    else:
        return 'ENNEMY'

# Main Functions # ------------------------------------------------------------------------------------------------------

def login(player_list):
    """
    This function is used by the 'player_entity_maker' function to create a new player
    It is the input function associated with the 'player_entity_maker'
    It is the first function runned after the start screen
    It allows to create players depending on conditions
    """

    if len(player_list) > 0:
        show_player_list(player_list)

    pseudonyme = input("""What is your pseudonyme ?
            >>> """)

    if player_in_player_list(player_list, pseudonyme) == False:

        if len(player_list) > 0:
            show_player_list(player_list)

            answer = check_answer_get_yes_no("Do you want to create a new player with the pseudonyme {} ?".format(pseudonyme))

            if answer == 'yes':
                password = input("""What is your password ?:
                        >>> """)

                player_list, pseudonyme, password, player_entity = player_entity_maker(player_list, pseudonyme, password)
                return player_list, pseudonyme, password, player_entity

            else:
                login(player_list)

        else:
            print("You have to create a player")
            answer = check_answer_get_yes_no("Do you want to create a new player with the pseudonyme {} ?".format(pseudonyme))

            if answer == 'yes':
                password = input("""What is your password ?:
                        >>> """)

                player_list, pseudonyme, password, player_entity = player_entity_maker(player_list, pseudonyme, password)
                return player_list, pseudonyme, password, player_entity

            else:
                login(player_list)

            password = input("""What is your password ?:
                    >>> """)

            player_list, pseudonyme, password, player_entity = player_entity_maker(player_list, pseudonyme, password)
            return player_list, pseudonyme, password, player_entity

    else:
        end = False
        while end == False:
            password = input("""What is your password ?:
                    >>> """)

            if check_login(player_list, pseudonyme, password) == True:
                end = True

            else:
                print("Wrong password")
                continue

        player_entity = player_list[pseudonyme][1]
        password = player_list[pseudonyme][0]
        return player_list, pseudonyme, password, player_entity


def main(player_list):
    start_screen()
    player_list, pseudonyme, password, player_entity = login(player_list)
    welcome(pseudonyme, player_entity.get_player_stats()['CHAPTER'])

    end = False
    while end == False:

        player_list = player_entity.player_level_up(player_list, pseudonyme)
        ask_change_chapter(player_list, pseudonyme, player_entity)
        do_quit = get_menu_choice(player_entity, player_list, pseudonyme)

        if do_quit == 'quit':
            answer_buy_again = check_answer_get_yes_no("Are you sure you want to quit ?")
            if answer_buy_again == 'yes':
                end = True

        if do_quit == 'del player_list':
            del player_list[pseudonyme]


player_list = charge_file()
main(player_list)
save_file(player_list)
