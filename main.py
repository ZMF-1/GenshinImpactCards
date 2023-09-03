# IMPORT
import random
import os
import nasTools as nt

# CHECK LIB
remod = nt.require(['random', 'os', 'hashlib', 'ftplib'])
nt.nprint('检测到有模块缺失: {}, '.format(remod))
pu = nt.pause('安装', True)
if pu == True:
    nt.usePipInstallWithList(remod)
else:
    nt.pause()

# START
os.system('cls')
print("-- -- -- 卡牌对决 -- -- --\n\n")

# CARDS
card1 = {"名称": "纳西妲", "攻击力": 2990, "防御力": 2300, "敏捷": 10}
card2 = {"名称": "胡桃", "攻击力": 1064, "防御力": 1700, "敏捷": 16}
card3 = {"名称": "雷电将军", "攻击力": 3370, "防御力": 2789, "敏捷": 12}
card4 = {"名称": "宵宫", "攻击力": 3230, "防御力": 2615, "敏捷": 11}
card5 = {"名称": "神里绫华", "攻击力": 3200, "防御力": 1840, "敏捷": 13}
card6 = {"名称": "八重神子", "攻击力": 2400, "防御力": 1569, "敏捷": 10}
card7 = {"名称": "魈", "攻击力": 3000, "防御力": 2340, "敏捷": 13}
card8 = {"名称": "甘雨", "攻击力": 3350, "防御力": 2630, "敏捷": 9}
card9 = {"名称": "达达利亚", "攻击力": 3297, "防御力": 2807, "敏捷": 13}

# RULES
rules = """规则：
1、双方初始血量：10000
2、对决之前，双方随即获得3张卡牌
3、每回合双方派出1张卡牌出战，对决后，出战卡牌消失，并重新抽取1张卡牌
4、敏捷高的一方进行攻击，对方根据自身卡牌的防御力，扣除血量
5、接着敏捷低的一方进行反击，对方根据自身卡牌的防御力，扣除血量
6、血量低于零的一方输掉比赛
"""
print(rules)
eula = input('\n我看完了(ENTER)')
os.system("cls")
print("-- -- -- 卡牌对决 -- -- --\n\n")

# VALUE
playerHP = 10000
enemyHP = 10000
playerCards = []
enemyCards = []
win = -1
setKYGift = 0
set77Gift = 0

# CARD POOL
cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9]

# RANDOM PLAYER CARDS
for i in range(3):
    playerCards.append(cards[random.randint(0, len(cards) - 1)])

# RANDOM ENEMY CARDS
for i in range(3):
    enemyCards.append(cards[random.randint(0, len(cards) - 1)])

# SHOW CARDS
print("恭喜你，获得了卡牌：")
print("名称     ", end='')
for i in playerCards:
    print(str(i["名称"]) + "     ", end='')
print()
print("攻击力    ", end='')
for i in playerCards:
    print(str(i["攻击力"]) + "       ", end='')
print()
print("防御力    ", end='')
for i in playerCards:
    print(str(i["防御力"]) + "       ", end='')
print()
print("敏捷     ", end='')
for i in playerCards:
    print(str(i["敏捷"]) + "         ", end='')
eula = input('\n我看完了(ENTER)')

while True:
    # GUI
    os.system("cls")
    print("-- -- -- 卡牌对决 -- -- --\n\n")
    print("敌方    血量 {}".format(enemyHP))
    print("\n\n\n\n\n\n\n")
    print("我方    血量 {}".format(playerHP))
    eula = input('\n我看完了(ENTER)')

    # PLAYER
    os.system('cls')
    print("-- -- -- 卡牌对决 -- -- --\n\n")
    print("敌方    血量 {}".format(enemyHP))
    print("\n\n\n")
    for i in playerCards:
        print(i)
    playerSelect = input("请派出卡牌：")
    print("我方    血量 {}".format(playerHP))
    os.system('cls')
    print("-- -- -- 卡牌对决 -- -- --\n\n")
    print("敌方    血量 {}".format(enemyHP))
    print("\n\n\n")
    playerC = playerCards[int(playerSelect) - 1]
    print("我方派出了 {}".format(playerC["名称"]))
    print("\n\n")
    print("我方    血量 {}".format(playerHP))
    eula = input('\n我看完了(ENTER)')

    # ENEMY
    os.system("cls")
    print("-- -- -- 卡牌对决 -- -- --\n\n")
    print("敌方    血量 {}".format(enemyHP))
    print("\n\n")
    enemySelect = random.randint(0, len(enemyCards) - 1)
    enemyC = enemyCards[int(enemySelect)]
    print("敌方派出了 {}".format(enemyC))
    print("\n\n\n")
    print("我方    血量 {}".format(playerHP))
    eula = input('\n我看完了(ENTER)')

    # RESET
    os.system('cls')
    print("-- -- -- 卡牌对决 -- -- --\n\n")

    # KILL
    if playerC["敏捷"] > enemyC["敏捷"]:
        playerHurt = playerC["攻击力"] - enemyC["防御力"]
        if playerHurt < 0:
            playerHurt = 0
        enemyHP -= playerHurt
        print("敌方    血量 {}".format(enemyHP))
        print("\n\n")
        if enemyHP <= 0:
            playerHurt += enemyHP
            enemyHP = 0
            win = 0
        print("我方发动攻击！\n造成 {} 点伤害".format(playerHurt))
        print("\n\n")
        print("我方    血量 {}".format(playerHP))
        eula = input('\n我看完了(ENTER)')
        if win == 0:
            os.system('cls')
            print("-- -- -- 卡牌对决 -- -- --\n\n")
            print("敌方    血量 {}".format(enemyHP))
            print("\n\n\n")
            print("我方获胜！！！")
            print("\n\n")
            print("我方    血量 {}".format(playerHP))
            break
        elif win == 1:
            os.system('cls')
            print("-- -- -- 卡牌对决 -- -- --\n\n")
            print("敌方    血量 {}".format(enemyHP))
            print("\n\n")
            print("敌方获胜！！！")
            print("\n\n\n")
            print("我方    血量 {}".format(playerHP))
            break
        else:
            os.system('cls')
            print("-- -- -- 卡牌对决 -- -- --\n\n")
            enemyHurt = enemyC["攻击力"] - playerC["防御力"]
            if enemyHurt < 0:
                enemyHurt = 0
            playerHP -= enemyHurt
            print("敌方    血量 {}".format(enemyHP))
            print("\n\n")
            if enemyHP <= 0:
                enemyHurt += playerHP
                playerHP = 0
                win = 1
            print("敌方发动反击！\n造成 {} 点伤害".format(enemyHurt))
            print("\n\n")
            print("我方    血量 {}".format(playerHP))
            eula = input('\n我看完了(ENTER)')
            if win == 0:
                os.system('cls')
                print("-- -- -- 卡牌对决 -- -- --\n\n")
                print("敌方    血量 {}".format(enemyHP))
                print("\n\n\n")
                print("我方获胜！！！")
                print("\n\n")
                print("我方    血量 {}".format(playerHP))
                break
            elif win == 1:
                os.system('cls')
                print("-- -- -- 卡牌对决 -- -- --\n\n")
                print("敌方    血量 {}".format(enemyHP))
                print("\n\n")
                print("敌方获胜！！！")
                print("\n\n\n")
                print("我方    血量 {}".format(playerHP))
                break
    elif playerC["敏捷"] < enemyC["敏捷"]:
        enemyHurt = enemyC["攻击力"] - playerC["防御力"]
        if enemyHurt < 0:
            enemyHurt = 0
        playerHP -= enemyHurt
        print("敌方    血量 {}".format(enemyHP))
        print("\n\n")
        if enemyHP <= 0:
            enemyHurt += playerHP
            playerHP = 0
            win = 1
        print("敌方发动攻击！\n造成 {} 点伤害".format(enemyHurt))
        print("\n\n")
        print("我方    血量 {}".format(playerHP))
        eula = input('\n我看完了(ENTER)')
        if win == 0:
            os.system('cls')
            print("-- -- -- 卡牌对决 -- -- --\n\n")
            print("敌方    血量 {}".format(enemyHP))
            print("\n\n\n")
            print("我方获胜！！！")
            print("\n\n")
            print("我方    血量 {}".format(playerHP))
            break
        elif win == 1:
            os.system('cls')
            print("-- -- -- 卡牌对决 -- -- --\n\n")
            print("敌方    血量 {}".format(enemyHP))
            print("\n\n")
            print("敌方获胜！！！")
            print("\n\n\n")
            print("我方    血量 {}".format(playerHP))
            break
        else:
            os.system('cls')
            print("-- -- -- 卡牌对决 -- -- --\n\n")
            playerHurt = playerC["攻击力"] - enemyC["防御力"]
            if playerHurt < 0:
                playerHurt = 0
            enemyHP -= playerHurt
            print("敌方    血量 {}".format(enemyHP))
            print("\n\n")
            if enemyHP <= 0:
                playerHurt += enemyHP
                enemyHP = 0
                win = 0
            print("我方发动反击！\n造成 {} 点伤害".format(playerHurt))
            print("\n\n")
            print("我方    血量 {}".format(playerHP))
            eula = input('\n我看完了(ENTER)')
            if win == 0:
                os.system('cls')
                print("-- -- -- 卡牌对决 -- -- --\n\n")
                print("敌方    血量 {}".format(enemyHP))
                print("\n\n\n")
                print("我方获胜！！！")
                print("\n\n")
                print("我方    血量 {}".format(playerHP))
                break
            elif win == 1:
                os.system('cls')
                print("-- -- -- 卡牌对决 -- -- --\n\n")
                print("敌方    血量 {}".format(enemyHP))
                print("\n\n")
                print("敌方获胜！！！")
                print("\n\n\n")
                print("我方    血量 {}".format(playerHP))
                break
    else:
        os.system('cls')
        print("-- -- -- 卡牌对决 -- -- --\n\n")
        print("敌方    血量 {}".format(enemyHP))
        print("\n\n")
        print("敌我敏捷抵消")
        print("不发动攻击")
        print("\n\n")
        print("我方    血量 {}".format(playerHP))
        eula = input('\n我看完了(ENTER)')

    # AGAIN
    playerCards.remove(playerC)
    enemyCards.remove(enemyC)
    new = random.randint(0, len(cards) - 1)
    playerCards.append(cards[new])
    enemyCards.append(cards[random.randint(0, len(cards) - 1)])

    # YS POOL
    if random.randint(1, 4) == 4:
        os.system('cls')
        print("-- -- -- 卡牌对决 -- -- --\n\n")
        print("原始人，启动!")
        magic = random.randint(1, 2)
        if magic == 1:
            print("恭喜你抽到了 空月祝福，你的新卡牌攻击力增加2000")
            setKYGift = 1
        else:
            print("恭喜你抽到了 七七诅咒，你的新卡牌所有属性清零")
            set77Gift = 1
    eula = input('\n我看完了(ENTER)')

    # SHOW CARDS
    os.system('cls')
    print("-- -- -- 卡牌对决 -- -- --\n\n")
    if setKYGift == 1:
        print("恭喜你，获得了卡牌：")
        nk = cards[new]
        nk['攻击力'] += 200
        print(str(nk["名称"]) + "     ", end='')
        print()
        print("攻击力    ", end='')
        print(str(nk["攻击力"]) + "       ", end='')
        print()
        print("防御力    ", end='')
        print(str(nk["防御力"]) + "       ", end='')
        print()
        print("敏捷     ", end='')
        print(str(nk["敏捷"]) + "         ", end='')
        eula = input('\n我看完了(ENTER)')
    elif set77Gift == 1:
        print("恭喜你，获得了卡牌：")
        nk = cards[random.randint(0, len(cards) - 1)]
        nk['攻击力'] = 0
        nk['防御力'] = 0
        nk['敏捷'] = 0
        print(str(nk["名称"]) + "     ", end='')
        print()
        print("攻击力    ", end='')
        print(str(nk["攻击力"]) + "       ", end='')
        print()
        print("防御力    ", end='')
        print(str(nk["防御力"]) + "       ", end='')
        print()
        print("敏捷     ", end='')
        print(str(nk["敏捷"]) + "         ", end='')
        eula = input('\n我看完了(ENTER)')
    else:
        print("恭喜你，获得了卡牌：")
        nk = cards[new]
        print(str(nk["名称"]) + "     ", end='')
        print()
        print("攻击力    ", end='')
        print(str(nk["攻击力"]) + "       ", end='')
        print()
        print("防御力    ", end='')
        print(str(nk["防御力"]) + "       ", end='')
        print()
        print("敏捷     ", end='')
        print(str(nk["敏捷"]) + "         ", end='')
        eula = input('\n我看完了(ENTER)')