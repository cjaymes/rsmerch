import sqlite3
import sys

conn = sqlite3.connect('rs.sqlite')

c = conn.cursor()

locations = []
# id, name, url
loc = 0

npcs = []
# id, name, url
npc = 0

shops = []
# id, name, url, owner, location
shop = 0

stock = []
# shop, item, qty, sell_price, buy_price

# NOTE: skipped only bought or non-tradeable items

locations.append((loc, 'Kedagrim', 'https://runescape.wikia.com/wiki/Keldagrim'))
npcs.append((npc, 'Stonemason', 'https://runescape.wikia.com/wiki/Stonemason'))

shops.append((shop, 'Kedagrim Stonemason', 'https://runescape.wikia.com/wiki/Keldagrim_Stonemason', npc, loc))
stock.append((shop, 3420, 500, 21, 7)) # 'Limestone brick'
stock.append((shop, 8786, 30, 325000, 108333)) # 'Marble block'
stock.append((shop, 8784, 30, 130000, 43333)) # 'Gold leaf'
stock.append((shop, 8788, 30, 975000, 325000)) # 'Magic stone'

npc+=1
npcs.append((npc, 'Gunslik', 'https://runescape.wikia.com/wiki/Gunslik'))

shop+=1
shops.append((shop, "Gunslik's Assorted Items", 'https://runescape.wikia.com/wiki/Gunslik%27s_Assorted_Items', npc, loc))
stock.append((shop, 1935, 10, 1, 1)) # 'Jug'
stock.append((shop, 1925, 30, 2, 1)) # 'Bucket'
stock.append((shop, 590, 10, 1, 1)) # 'Tinderbox'
stock.append((shop, 1755, 10, 14, 4)) # 'Chisel'
stock.append((shop, 2347, 10, 13, 4)) # 'Hammer'
stock.append((shop, 36, 10, 3, 1)) # 'Candle'
stock.append((shop, 596, 10, 4, 1)) # 'Unlit torch'
stock.append((shop, 973, 10, 45, 15)) # 'Charcoal'
stock.append((shop, 1059, 10, 6, 2)) # 'Leather gloves'
stock.append((shop, 229, 300, 5, 1)) # 'Vial'
stock.append((shop, 233, 10, 4, 1)) # 'Pestle and mortar'
stock.append((shop, 954, 10, 18, 6)) # 'Rope'

npc+=1
npcs.append((npc, 'Vigr', 'https://runescape.wikia.com/wiki/Vigr'))

shop+=1
shops.append((shop, "Vigr's Warhammers", 'https://runescape.wikia.com/wiki/Vigr%27s_Warhammers', npc, loc))
stock.append((shop, 1337, 10, 61, 20)) # 'Bronze warhammer'
stock.append((shop, 25779, 10, 61, 20)) # 'Off-hand bronze warhammer'
stock.append((shop, 1335, 10, 224, 74)) # 'Iron warhammer'
stock.append((shop, 25781, 10, 224, 74)) # 'Off-hand iron warhammer'
stock.append((shop, 1339, 10, 832, 277)) # 'Steel warhammer'
stock.append((shop, 25783, 10, 832, 277)) # 'Off-hand steel warhammer'
stock.append((shop, 1341, 8, 1274, 424)) # 'Black warhammer'
stock.append((shop, 25785, 8, 1274, 424)) # 'Off-hand black warhammer'
stock.append((shop, 1343, 5, 2158, 719)) # 'Mithril warhammer'
stock.append((shop, 25787, 8, 2158, 719)) # 'Off-hand mithril warhammer'
stock.append((shop, 1345, 2, 5356, 1785)) # 'Adamant warhammer'
stock.append((shop, 25789, 2, 5356, 1785)) # 'Off-hand adamant warhammer'
stock.append((shop, 29534, 1, 200000, 60000)) # 'Dragon warhammer'
stock.append((shop, 29537, 1, 50000, 15000)) # 'Off-hand dragon warhammer'

npc+=1
npcs.append((npc, 'Saro', 'https://runescape.wikia.com/wiki/Saro'))

shop+=1
shops.append((shop, "Quality Armour Shop", 'https://runescape.wikia.com/wiki/Quality_Armour_Shop', npc, loc))
stock.append((shop, 1105, 10, 750, 225)) # 'Steel chainbody'
stock.append((shop, 1107, 8, 1440, 432)) # 'Black chainbody'
stock.append((shop, 1109, 5, 1940, 585)) # 'Mithril chainbody'
stock.append((shop, 1111, 2, 4800, 1440)) # 'Adamant chainbody'
stock.append((shop, 1141, 10, 300, 90)) # 'Steel helm'
stock.append((shop, 1151, 8, 576, 173)) # 'Black helm'
stock.append((shop, 1159, 5, 780, 234)) # 'Mithril helm'
stock.append((shop, 1161, 2, 1920, 576)) # 'Adamant helm'
stock.append((shop, 1177, 10, 600, 180)) # 'Steel sq shield'
stock.append((shop, 1195, 8, 2121, 636)) # 'Black kiteshield'
stock.append((shop, 30028, 10, 500000, 150000)) # 'Reinforcing plate'

npc+=1
npcs.append((npc, 'Santiri', 'https://runescape.wikia.com/wiki/Santiri'))

shop+=1
shops.append((shop, "Quality Weapons Shop", 'https://runescape.wikia.com/wiki/Quality_Weapons_Shop', npc, loc))
stock.append((shop, 1365, 10, 650, 216)) # 'Steel battleaxe'
stock.append((shop, 1369, 10, 1690, 563)) # 'Mithril battleaxe'
stock.append((shop, 1285, 10, 845, 281)) # 'Mithril sword'
stock.append((shop, 1287, 10, 2080, 693)) # 'Adamant sword'
stock.append((shop, 1325, 10, 400, 133)) # 'Steel scimitar'
stock.append((shop, 1297, 10, 960, 320)) # 'Black longsword'
stock.append((shop, 1303, 10, 32000, 10666)) # 'Rune longsword'
stock.append((shop, 853, 10, 400, 133)) # 'Maple shortbow'
stock.append((shop, 851, 10, 640, 192)) # 'Maple shieldbow'
stock.append((shop, 888, 100, 76, 25)) # Mithril arrow
stock.append((shop, 890, 20, 172, 57)) # 'Adamant arrow'
stock.append((shop, 29540, 1, 200000, 60000)) # 'Dragon battlestaff'

npc+=1
npcs.append((npc, 'Tati', 'https://runescape.wikia.com/wiki/Tati'))

shop+=1
shops.append((shop, "Pickaxe-Is-Mine", 'https://runescape.wikia.com/wiki/Pickaxe-Is-Mine', npc, loc))
stock.append((shop, 1265, 10, 1, 1)) # 'Bronze pickaxe'
stock.append((shop, 1267, 10, 140, 42)) # 'Iron pickaxe'
stock.append((shop, 1269, 10, 500, 166)) # 'Steel pickaxe'
stock.append((shop, 1273, 5, 1300, 433)) # 'Mithril pickaxe'
stock.append((shop, 1271, 2, 3200, 1066)) # 'Adamant pickaxe'
stock.append((shop, 1275, 1, 32000, 10666)) # 'Rune pickaxe'

npc+=1
npcs.append((npc, 'Agmundi', 'https://runescape.wikia.com/wiki/Agmundi'))

shop+=1
shops.append((shop, "Agmundi Quality Clothes", 'https://runescape.wikia.com/wiki/Agmundi_Quality_Clothes', npc, loc))
stock.append((shop, 5050, 10, 715, 214)) # Skirt (lilac)
stock.append((shop, 5052, 10, 812, 243)) # Skirt (blue)
stock.append((shop, 5038, 10, 910, 273)) # Trousers (lilac) item #?
stock.append((shop, 5040, 10, 975, 292)) # Trousers (blue) item #?
stock.append((shop, 5044, 10, 468, 140)) # Shorts (tan) item #?
stock.append((shop, 5046, 10, 507, 152)) # Shorts (blue)
stock.append((shop, 5026, 10, 812, 243)) # Woven top (tan) item #?
stock.append((shop, 5028, 10, 845, 253)) # Woven top (blue) item #?
stock.append((shop, 5032, 10, 780, 234)) # Shirt (tan) item #?
stock.append((shop, 5034, 10, 812, 243)) # Shirt (lilac) item #?

npc+=1
npcs.append((npc, 'Vermundi', 'https://runescape.wikia.com/wiki/Vermundi'))

shop+=1
shops.append((shop, "Vermundi's Clothes Stall", 'https://runescape.wikia.com/wiki/Vermundi%27s_Clothes_Stall', npc, loc))
stock.append((shop, 5048, 10, 455, 151)) # Skirt (brown) item #?
stock.append((shop, 5036, 10, 715, 238)) # Trousers (brown) item #?
stock.append((shop, 5042, 10, 364, 121)) # Shorts (brown) item #?
stock.append((shop, 5024, 10, 650, 216)) # Woven top (brown) item #?
stock.append((shop, 5030, 10, 585, 195)) # Shirt (brown) item #?
stock.append((shop, 950, 10, 55, 18)) # Silk

npc+=1
npcs.append((npc, 'Hirko', 'https://runescape.wikia.com/wiki/Hirko'))

shop+=1
shops.append((shop, "Crossbow Shop (Keldagrim)", 'https://runescape.wikia.com/wiki/Crossbow_Shop_(Keldagrim)', npc, loc))
stock.append((shop, 877, 60, 3, 1)) # Bronze bolts
stock.append((shop, 9140, 50, 2, 1)) # Iron bolts
stock.append((shop, 9141, 40, 8, 2)) # Steel bolts
stock.append((shop, 9142, 30, 20, 6)) # Mithril bolts
stock.append((shop, 9143, 20, 58, 17)) # Adamant bolts
stock.append((shop, 9144, 10, 300, 90)) # Runite bolts
stock.append((shop, 9440, 10, 20, 12)) # Wooden stock
stock.append((shop, 9442, 10, 27, 16)) # Oak stock
stock.append((shop, 9444, 10, 53, 15)) # Willow stock
stock.append((shop, 9446, 10, 77, 46)) # Teak stock
stock.append((shop, 9448, 5, 100, 60)) # Maple stock
stock.append((shop, 9450, 2, 133, 31)) # Mahogany stock
stock.append((shop, 9452, 1, 167, 100)) # Yew stock
stock.append((shop, 9420, 10, 20, 12)) # Bronze limbs
stock.append((shop, 9423, 10, 70, 42)) # Iron limbs
stock.append((shop, 9425, 10, 250, 150)) # Steel limbs
stock.append((shop, 9427, 5, 650, 390)) # Mithril limbs
stock.append((shop, 9429, 2, 1600, 960)) # Adamantite limbs
stock.append((shop, 9431, 1, 16000, 9600)) # Runite limbs
stock.append((shop, 9174, 10, 73, 21)) # Bronze crossbow
stock.append((shop, 9177, 10, 157, 47)) # Iron crossbow
stock.append((shop, 9179, 10, 360, 108)) # Steel crossbow
stock.append((shop, 9181, 5, 783, 234)) # Mithril crossbow
stock.append((shop, 9183, 2, 1767, 530)) # Adamant crossbow
stock.append((shop, 9185, 1, 16200, None)) # Rune crossbow
stock.append((shop, 25881, 10, 73, 21)) # Off-hand bronze crossbow
stock.append((shop, 25883, 10, 157, 47)) # Off-hand Iron crossbow
stock.append((shop, 25885, 10, 360, 108)) # Off-hand Steel crossbow
stock.append((shop, 25887, 5, 783, 234)) # Off-hand Mithril crossbow
stock.append((shop, 25889, 2, 1767, 530)) # Off-hand Adamant crossbow
stock.append((shop, 25891, 1, 16200, None)) # Off-hand Rune crossbow
stock.append((shop, 25919, 10, 73, 21)) # Bronze 2h crossbow
stock.append((shop, 25921, 10, 157, 47)) # Iron 2h crossbow
stock.append((shop, 25923, 10, 360, 108)) # Steel 2h crossbow
stock.append((shop, 25925, 5, 783, 234)) # Mithril 2h crossbow
stock.append((shop, 25927, 2, 1767, 530)) # Adamant 2h crossbow
stock.append((shop, 25929, 1, 16200, None)) # Rune 2h crossbow

npc+=1
npcs.append((npc, 'Nolar', 'https://runescape.wikia.com/wiki/Nolar'))

shop+=1
shops.append((shop, "Carefree Crafting Stall", 'https://runescape.wikia.com/wiki/Carefree_Crafting_Stall', npc, loc))
stock.append((shop, 1755, 10, 14, 4)) # Chisel
stock.append((shop, 1592, 10, 5, 1)) # Ring mould
stock.append((shop, 1597, 10, 5, 1)) # Necklace mould
stock.append((shop, 1733, 10, 1, 1)) # Needle
stock.append((shop, 1734, 1000, 4, 1)) # Thread
stock.append((shop, 1759, 100, 5, 1)) # Ball of wool

npc+=1
npcs.append((npc, 'Hervi', 'https://runescape.wikia.com/wiki/Hervi'))

shop+=1
shops.append((shop, "Green Gemstone Gems", 'https://runescape.wikia.com/wiki/Green_Gemstone_Gems', npc, loc))

npc+=1
npcs.append((npc, 'Randivor', 'https://runescape.wikia.com/wiki/Randivor'))

shop+=1
shops.append((shop, "Keldagrim's Best Bread", 'https://runescape.wikia.com/wiki/Keldagrim%27s_Best_Bread', npc, loc))
stock.append((shop, 2309, 10, 24, 8)) # Bread
stock.append((shop, 1891, 10, 50, 16)) # Cake
stock.append((shop, 1901, 10, 30, 10)) # Chocolate slice

npc+=1
npcs.append((npc, 'Gulldamar', 'https://runescape.wikia.com/wiki/Gulldamar'))

shop+=1
shops.append((shop, "Silver Cog Silver Stall", 'https://runescape.wikia.com/wiki/Silver_Cog_Silver_Stall', npc, loc))
stock.append((shop, 1714, 10, 200, 60)) # Unstrung symbol

npc+=1
npcs.append((npc, 'Jorzik', 'https://runescape.wikia.com/wiki/Jorzik'))

shop+=1
shops.append((shop, "Armour Store", 'https://runescape.wikia.com/wiki/Armour_Store', npc, loc))

npc+=1
npcs.append((npc, 'Ordan', 'https://runescape.wikia.com/wiki/Ordan'))

shop+=1
shops.append((shop, "Ore Seller", 'https://runescape.wikia.com/wiki/Ore_Seller', npc, loc))
stock.append((shop, 436, 100, 20, 6)) # Copper ore
stock.append((shop, 438, 100, 20, 6)) # Tin ore
stock.append((shop, 440, 100, 17, 5)) # Iron ore
stock.append((shop, 447, 100, 162, 54)) # Mithril ore
stock.append((shop, 442, 100, 75, 25)) # Silver ore
stock.append((shop, 444, 100, 150, 50)) # Gold ore
stock.append((shop, 453, 100, 45, 15)) # Coal

npc+=1
npcs.append((npc, 'Kjut', 'https://runescape.wikia.com/wiki/Kjut'))

shop+=1
shops.append((shop, "Kjut's Kebabs", 'https://runescape.wikia.com/wiki/Kjut%27s_Kebabs', npc, loc))
stock.append((shop, 1971, float('Inf'), 1, None)) # Kebab

loc+=1
locations.append((loc, 'Catherby', 'https://runescape.wikia.com/wiki/Catherby'))

npc+=1
npcs.append((npc, 'Arhein', 'https://runescape.wikia.com/wiki/Arhein'))

shop+=1
shops.append((shop, "Arhein's Store", 'https://runescape.wikia.com/wiki/Arhein%27s_Store', npc, loc))
stock.append((shop, 401, 80, 160, None)) # Seaweed
stock.append((shop, 2114, 40, 80, None)) # Pineapple
stock.append((shop, 1925, 30, 2, 1)) # Bucket
stock.append((shop, 1265, 10, 1, 1)) # Bronze pickaxe
stock.append((shop, 1923, 10, 4, 1)) # Bowl
stock.append((shop, 1887, 10, 10, 3)) # Cake tin
stock.append((shop, 590, 10, 1, 1)) # Tinderbox
stock.append((shop, 1755, 10, 14, 4)) # Chisel
stock.append((shop, 2347, 10, 13, 3)) # Hammer
stock.append((shop, 954, 10, 18, 5)) # Rope
stock.append((shop, 1931, 30, 1, 1)) # Empty pot
stock.append((shop, 946, 10, 25, 7)) # Knife

npc+=1
npcs.append((npc, 'Candle-Maker', 'https://runescape.wikia.com/wiki/Candle-Maker'))

shop+=1
shops.append((shop, "Candle Shop", 'https://runescape.wikia.com/wiki/Candle_Shop', npc, loc))
stock.append((shop, 36, 10, 3, 1)) # Candle

npc+=1
npcs.append((npc, 'Harry', 'https://runescape.wikia.com/wiki/Harry'))

shop+=1
shops.append((shop, "Harry's Fishing Shop", 'https://runescape.wikia.com/wiki/Harry%27s_Fishing_Shop', npc, loc))
stock.append((shop, 303, 10, 40, 13)) # Small fishing net
stock.append((shop, 307, 10, 5, 1)) # Fishing rod
stock.append((shop, 311, 1000, 45, 15)) # Harpoon
stock.append((shop, 301, 10, 20, 6)) # Lobster pot
stock.append((shop, 313, 1000, 3, 1)) # Fishing bait
stock.append((shop, 305, 10, 20, 6)) # Big fishing net

npc+=1
npcs.append((npc, 'Hickton', 'https://runescape.wikia.com/wiki/Hickton'))

shop+=1
shops.append((shop, "Hickton's Archery Emporium", 'https://runescape.wikia.com/wiki/Hickton%27s_Archery_Emporium', npc, loc))
stock.append((shop, 877, 60, 3, 1)) # Bronze bolts
stock.append((shop, 9140, 50, 2, 1)) # Iron bolts
stock.append((shop, 9141, 40, 8, 2)) # Steel bolts
stock.append((shop, 9142, 30, 20, 6)) # Mithril bolts
stock.append((shop, 9143, 20, 58, 17)) # Adamant bolts
stock.append((shop, 9144, 10, 300, 90)) # Runite bolts
stock.append((shop, 882, 60, 7, 2)) # Bronze arrpws
stock.append((shop, 884, 50, 20, 6)) # Iron arrpws
stock.append((shop, 886, 40, 46, 15)) # Steel arrpws
stock.append((shop, 888, 30, 76, 25)) # Mithril arrpws
stock.append((shop, 890, 20, 172, 57)) # Adamant arrpws
stock.append((shop, 892, 10, 510, 153)) # Rune arrpws
stock.append((shop, 39, 20, 10, 3)) # Bronze arrpwheads
stock.append((shop, 40, 20, 26, 8)) # Iron arrpwheads
stock.append((shop, 41, 20, 36, 12)) # Steel arrpwheads
stock.append((shop, 42, 15, 68, 22)) # Mithril arrpwheads
stock.append((shop, 43, 10, 160, 53)) # Adamant arrpwheads
stock.append((shop, 44, 5, 460, 153)) # Rune arrpwheads
stock.append((shop, 4827, 1, 180, 60)) # Comp ogre bow

npc+=1
npcs.append((npc, 'Vanessa', 'https://runescape.wikia.com/wiki/Vanessa'))

shop+=1
shops.append((shop, "Vanessa's Farming Shop", 'https://runescape.wikia.com/wiki/Vanessa%27s_Farming_Shop', npc, loc))
stock.append((shop, 6032, 300, 20, 6)) # Compost
stock.append((shop, 5341, 10, 6, 2)) # Rake
stock.append((shop, 5325, 10, 12, 4)) # Gardening trowel
stock.append((shop, 6036, 10, 40, 13)) # Plant cure
stock.append((shop, 5343, 10, 6, 2)) # Seed dibber
stock.append((shop, 5331, 30, 8, 2)) # Watering can
stock.append((shop, 5329, 10, 5, 1)) # Secateurs
stock.append((shop, 952, 10, 3, 1)) # Spade
stock.append((shop, 5350, 1100, 1, 1)) # Plant pot 100 + 1000 from pack
stock.append((shop, 5376, 60, 1, 1)) # Basket 10 + 50 from pack
stock.append((shop, 1925, 100, 2, 1)) # Bucket
stock.append((shop, 5418, 60, 1, 1)) # Empty sack 10 + 50 from pack
stock.append((shop, 12622, 10, 200, 66)) # Amulet of farming (8)

loc+=1
locations.append((loc, 'Charter Ship locations', 'https://runescape.wikia.com/wiki/Charter_Ship'))

npc+=1
npcs.append((npc, 'Trader_Stan', 'https://runescape.wikia.com/wiki/Trader_Stan'))

shop+=1
shops.append((shop, "Trader Stan's Trading Post", 'https://runescape.wikia.com/wiki/Trader_Stan%27s_Trading_Post', npc, loc))
stock.append((shop, 1931, 30, 1, 1)) # Empty pot
stock.append((shop, 1935, 10, 1, 1)) # Jug
stock.append((shop, 1735, 10, 1, 1)) # Shears
stock.append((shop, 1925, 30, 2, 1)) # Bucket
stock.append((shop, 1923, 10, 4, 1)) # Bowl
stock.append((shop, 1887, 10, 10, 3)) # Cake Tin
stock.append((shop, 590, 10, 1, 1)) # Tinderbox
stock.append((shop, 1755, 10, 14, 4)) # Chisel
stock.append((shop, 2347, 10, 13, 4)) # Hammer
stock.append((shop, 550, 10, 1, 1)) # Newcomer map
stock.append((shop, 9003, 10, 2, 1)) # Security book
stock.append((shop, 954, 10, 18, 6)) # Rope
stock.append((shop, 946, 10, 25, 8)) # Knife
stock.append((shop, 1963, 10, 2, 1)) # Banana
stock.append((shop, 1785, 10, 16, 5)) # Glassblowing pipe
stock.append((shop, 301, 10, 20, 6)) # Lobster pot
stock.append((shop, 307, 10, 5, 1)) # Fishing rod
stock.append((shop, 1941, 10, 31, 10)) # Swamp paste
stock.append((shop, 9629, 10, 1265, 421)) # Tyras helm
stock.append((shop, 3226, 10, 67, 22)) # Raw rabbit
stock.append((shop, 1025, 10, 2, 1)) # Eye patch

loc+=1
locations.append((loc, 'Lumbridge', 'https://runescape.wikia.com/wiki/Lumbridge'))

npc+=1
npcs.append((npc, 'Shopkeeper', 'https://runescape.wikia.com/wiki/Shopkeeper'))

shop+=1
shops.append((shop, "Lumbridge General Store", 'https://runescape.wikia.com/wiki/Lumbridge_General_Store', npc, loc))
stock.append((shop, 590, 1, 0, 0)) # Tinderbox
stock.append((shop, 2347, 1, 0, 0)) # Hammer
stock.append((shop, 1205, 1, 0, 0)) # Bronze dagger
stock.append((shop, 1931, 30, 1, 0)) # Empty pot
stock.append((shop, 1935, 10, 1, 0)) # Jug
stock.append((shop, 1735, 10, 1, 0)) # Shears
stock.append((shop, 1925, 30, 2, 0)) # Bucket
stock.append((shop, 1923, 10, 4, 1)) # Bowl
stock.append((shop, 1887, 10, 10, 4)) # Cake tin
stock.append((shop, 590, 10, 1, 0)) # Tinderbox
stock.append((shop, 1755, 10, 14, 5)) # Chisel
stock.append((shop, 2347, 10, 13, 5)) # Hammer
stock.append((shop, 550, 10, 1, 0)) # Newcomer map
stock.append((shop, 9003, 10, 2, 0)) # Security book

npc+=1
npcs.append((npc, 'Bob', 'https://runescape.wikia.com/wiki/Bob'))

shop+=1
shops.append((shop, "Bob's Brilliant Axes", 'https://runescape.wikia.com/wiki/Bob%27s_Brilliant_Axes', npc, loc))
stock.append((shop, 1265, 1, 0, 0)) # Bronze pickaxe
stock.append((shop, 1351, 1, 0, 0)) # Bronze hatchet
stock.append((shop, 1375, 1, 0, 0)) # Bronze battleaxe
stock.append((shop, 25761, 1, 0, 0)) # Off-hand bronze battleaxe
stock.append((shop, 800, 1, 0, 0)) # Bronze throwing axe
stock.append((shop, 25903, 1, 0, 0)) # Off-hand bronze throwing axe
stock.append((shop, 1267, 10, 140, 42)) # Iron pickaxe
stock.append((shop, 1349, 10, 56, 16)) # Iron hatchet
stock.append((shop, 1363, 10, 182, 54)) # Iron battleaxe
stock.append((shop, 25763, 10, 182, 54)) # Off-hand iron battleaxe
stock.append((shop, 801, 10, 13, 3)) # Iron throwing axe
stock.append((shop, 25904, 10, 13, 3)) # Off-hand iron throwing axe
stock.append((shop, 1269, 1, 500, 150)) # Steel pickaxe
stock.append((shop, 1353, 10, 200, 60)) # Steel hatchet
stock.append((shop, 1365, 10, 650, 195)) # Steel battleaxe
stock.append((shop, 25765, 10, 650, 195)) # Off-hand steel battleaxe
stock.append((shop, 802, 12, 38, 11)) # Steel throwing axe
stock.append((shop, 25905, 12, 38, 11)) # Off-hand steel throwing axe
stock.append((shop, 1273, 5, 1300, 390)) # Mithril pickaxe
stock.append((shop, 1355, 5, 520, 156)) # Mithril hatchet
stock.append((shop, 1369, 5, 1690, 507)) # Mithril battleaxe
stock.append((shop, 25769, 5, 1690, 507)) # Off-hand mithril battleaxe
stock.append((shop, 1271, 2, 3200, 960)) # Adamant pickaxe
stock.append((shop, 1357, 2, 1280, 384)) # Adamant hatchet
stock.append((shop, 1371, 2, 4160, 1248)) # Adamant battleaxe
stock.append((shop, 25771, 2, 4160, 1248)) # Off-hand adamant battleaxe
stock.append((shop, 804, 4, 262, 78)) # Adamant throwing axe
stock.append((shop, 25907, 4, 262, 78)) # Off-hand adamant throwing axe

npc+=1
npcs.append((npc, 'Hank', 'https://runescape.wikia.com/wiki/Hank'))

shop+=1
shops.append((shop, "Lumbridge Fishing Supplies", 'https://runescape.wikia.com/wiki/Lumbridge_Fishing_Supplies', npc, loc))
stock.append((shop, 303, 1, 0, 0)) # Small fishing net
stock.append((shop, 13431, 1, 0, 0)) # Crayfish cage
stock.append((shop, 303, 5, 40, 12)) # Small fishing net
stock.append((shop, 307, 10, 5, 3)) # Fishing rod
stock.append((shop, 309, 10, 5, 3)) # Fly fishing rod
stock.append((shop, 13431, 10, 20, 6)) # Crayfish cage
stock.append((shop, 313, 1000, 3, 1)) # Fishing bait
stock.append((shop, 314, 1000, 6, 3)) # Feather

npc+=1
npcs.append((npc, 'None', None))

shop+=1
shops.append((shop, "Culinaromancer's Chest", 'https://runescape.wikia.com/wiki/Culinaromancer%27s_Chest', npc, loc))
stock.append((shop, 1973, 300, 20, 6)) # Chocolate bar
stock.append((shop, 1982, 10, 14, 4)) # Tomato
stock.append((shop, 1987, 5, 1, 1)) # Grapes
stock.append((shop, 2283, 1, 4, 1)) # Pizza base
stock.append((shop, 1927, 10, 12, 4)) # Bucket of milk
stock.append((shop, 6697, 10, 4, 1)) # Pat of butter
stock.append((shop, 2313, 10, 3, 1)) # Pie dish
stock.append((shop, 1923, 10, 4, 1)) # Bowl
stock.append((shop, 1931, 10, 1, 1)) # Empty pot
stock.append((shop, 1925, 10, 2, 1)) # Bucket
stock.append((shop, 19858, 10, 8, 2)) # Cheese
stock.append((shop, 1955, 50, 36, 12)) # Cooking apple
stock.append((shop, 1933, 100, 14, 4)) # Pot of flour
stock.append((shop, 1944, 10, 4, 1)) # Egg
stock.append((shop, 2130, 10, 19, 6)) # Pot of cream
stock.append((shop, 2007, 10, 230, 76)) # Spice
stock.append((shop, 1887, 10, 10, 3)) # Cake tin
stock.append((shop, 1935, 10, 1, 1)) # Jug
stock.append((shop, 1980, 10, 2, 1)) # EMpty cup
stock.append((shop, 7433, 10, 35, None)) # Wooden spoon
stock.append((shop, 7435, 10, 50, None)) # Egg whisk
stock.append((shop, 7437, 10, 325, None)) # Spork
stock.append((shop, 7439, 10, 1920, None)) # Spatula
stock.append((shop, 7441, 10, 1660, None)) # Frying pan
stock.append((shop, 7443, 10, 3200, None)) # Skewer
stock.append((shop, 7445, 10, 14400, None)) # Rolling pin
stock.append((shop, 7447, 10, 8000, None)) # Kitchen knife
stock.append((shop, 7449, 10, 41500, None)) # Meat tenderiser
stock.append((shop, 7451, 10, 25600, None)) # Cleaver

loc+=1
locations.append((loc, 'Burthorpe', 'https://runescape.wikia.com/wiki/Burthorpe'))

npc+=1
npcs.append((npc, 'Gnome Shopkeeper', 'https://runescape.wikia.com/wiki/Gnome_Shopkeeper'))

shop+=1
shops.append((shop, "Gnome Shopkeeper's Armoury", 'https://runescape.wikia.com/wiki/Gnome_Shopkeeper%27s_Armoury', npc, loc))
stock.append((shop, 1277, 1, 0, 7)) # Bronze sword
stock.append((shop, 19830, 1, 0, 20)) # Chargebow
stock.append((shop, 1379, 1, 0, 4)) # Staff
stock.append((shop, 1139, 10, 25, 7)) # Bronze helm
stock.append((shop, 1117, 10, 160, 48)) # Bronze platebody
stock.append((shop, 1103, 10, 60, 18)) # Bronze chainbody
stock.append((shop, 1075, 10, 80, 24)) # Bronze platelegs
stock.append((shop, 1087, 10, 80, 24)) # Bronze plateskirt
stock.append((shop, 1173, 10, 48, 14)) # Bronze sq shield
stock.append((shop, 1101, 10, 210, 63)) # Iron chainbody
stock.append((shop, 1137, 10, 84, 25)) # Iron helm
stock.append((shop, 1115, 10, 560, 168)) # Iron platebody
stock.append((shop, 1067, 10, 280, 84)) # Iron platelegs
stock.append((shop, 1081, 10, 280, 84)) # Iron plateskirt
stock.append((shop, 1175, 10, 168, 50)) # Iron sq shield
stock.append((shop, 1063, 10, 18, 6)) # Leather vambraces
stock.append((shop, 1061, 10, 6, 1)) # Leather boots
stock.append((shop, 1167, 10, 24, 7)) # Leather cowl
stock.append((shop, 1129, 10, 21, 6)) # Leather body
stock.append((shop, 1095, 10, 20, 6)) # Leather chaps
stock.append((shop, 25806, 10, 68, 20)) # Leather shield
stock.append((shop, 25875, 10, 200, 60)) # Hard leather gloves
stock.append((shop, 25821, 10, 200, 60)) # Hard leather boots
stock.append((shop, 41208, 10, 100, 30)) # Hard leather cowl
stock.append((shop, 1131, 10, 170, 51)) # Hard leather body
stock.append((shop, 41210, 10, 170, 51)) # Hard leather chaps
stock.append((shop, 25808, 10, 238, 71)) # Hard leather shield
stock.append((shop, 25873, 10, 100, 30)) # Wizard gloves
stock.append((shop, 41225, 10, 100, 30)) # Wizard boots
stock.append((shop, 579, 10, 2, 1)) # Wizard hat (blue)
stock.append((shop, 577, 10, 15, 4)) # Wizard robe top
stock.append((shop, 1011, 10, 2, 1)) # Wizard robe skirt
stock.append((shop, 41200, 10, 100, 30)) # Wizard shield
stock.append((shop, 25851, 10, 100, 30)) # Imphide gloves
stock.append((shop, 25853, 10, 100, 30)) # Imphide boots
stock.append((shop, 25845, 10, 200, 60)) # Imphide hood
stock.append((shop, 25847, 10, 500, 150)) # Imphide robe top
stock.append((shop, 25849, 10, 200, 60)) # Imphide robe bottom
stock.append((shop, 25855, 10, 100, 30)) # Imphide shield
stock.append((shop, 25761, 10, 52, 15)) # Bronze battleaxe
stock.append((shop, 1363, 10, 182, 54)) # Iron battleaxe
stock.append((shop, 1309, 10, 280, 84)) # Iron 2h sword
stock.append((shop, 882, 30, 7, 2)) # Bronze arrow
stock.append((shop, 877, 30, 3, 1)) # Bronze bolts
stock.append((shop, 847, 1, 320, 96)) # Willow shieldbow
stock.append((shop, 25919, 1, 73, 21)) # Bronze 2h crossbow
stock.append((shop, 9177, 1, 157, 47)) # Iron crossbow
stock.append((shop, 25883, 1, 157, 47)) # Off-hand iron crossbow
stock.append((shop, 1389, 10, 200, 60)) # Magic staff
stock.append((shop, 25646, 10, 100, 30)) # Wizard wand
stock.append((shop, 25656, 10, 100, 30)) # Wizard book
stock.append((shop, 25642, 10, 250, 75)) # Imp horn wand
stock.append((shop, 25662, 10, 250, 75)) # Imphide book

npc+=1
npcs.append((npc, 'Apprentice Clara', 'https://runescape.wikia.com/wiki/Apprentice_Clara'))

shop+=1
shops.append((shop, "Carwen Essencebinder Magical Runes Shop", 'https://runescape.wikia.com/wiki/Carwen_Essencebinder_Magical_Runes_Shop', npc, loc))
stock.append((shop, 1438, 1, 0, None)) # Air talisman (free)
stock.append((shop, 1448, 1, 0, None)) # Mind talisman (free)
stock.append((shop, 556, 30, 0, None)) # Air rune (free)
stock.append((shop, 558, 30, 0, None)) # Mind rune (free)
stock.append((shop, 554, 100, 17, 5)) # Fire rune
stock.append((shop, 555, 100, 17, 5)) # Water rune
stock.append((shop, 556, 300, 17, 5)) # Air rune
stock.append((shop, 557, 300, 17, 5)) # Earth rune
stock.append((shop, 558, 300, 17, 5)) # Mind rune
stock.append((shop, 559, 100, 16, 4)) # Body rune
stock.append((shop, 562, 30, 140, 42)) # Chaos rune
stock.append((shop, 560, 10, 310, 93)) # Death rune

npc+=1
npcs.append((npc, 'Helemos', 'https://runescape.wikia.com/wiki/Helemos'))

shop+=1
shops.append((shop, "Happy Heroes' H'emporium", 'https://runescape.wikia.com/wiki/Happy_Heroes%27_H%27emporium', npc, loc))
stock.append((shop, 1377, 4, 200000, 110000)) # Dragon battleaxe
stock.append((shop, 25776, 4, 200000, 110000)) # Off-hand dragon battleaxe
stock.append((shop, 1434, 4, 50000, 27500)) # Dragon mace
stock.append((shop, 25689, 4, 50000, 27500)) # Off-hand dragon mace

npc+=1
npcs.append((npc, 'Gaius', 'https://runescape.wikia.com/wiki/Gaius'))

shop+=1
shops.append((shop, "Gaius's Two-Handed Shop", 'https://runescape.wikia.com/wiki/Gaius%27s_Two-Handed_Shop', npc, loc))
stock.append((shop, 1307, 10, 80, 24)) # Bronze 2h sword
stock.append((shop, 1309, 10, 280, 84)) # Iron 2h sword
stock.append((shop, 1311, 10, 1000, 300)) # Steel 2h sword
stock.append((shop, 1313, 8, 1920, 576)) # Black 2h sword
stock.append((shop, 1315, 5, 2600, 780)) # Mithril 2h sword
stock.append((shop, 1317, 2, 6400, 1920)) # Adamant 2h sword

loc+=1
locations.append((loc, 'Taverley', 'https://runescape.wikia.com/wiki/Taverley'))

npc+=1
npcs.append((npc, 'Alfred Stonemason', 'https://runescape.wikia.com/wiki/Alfred_Stonemason'))

shop+=1
shops.append((shop, "Alfred Stonemason's Construction Shop", 'https://runescape.wikia.com/wiki/Alfred_Stonemason%27s_Construction_Shop', npc, loc))
stock.append((shop, 2347, 10, 13, 3)) # Hammer
stock.append((shop, 8794, 10, 13, 3)) # Saw

npc+=1
npcs.append((npc, 'Alison Elmshaper', 'https://runescape.wikia.com/wiki/Alison_Elmshaper'))

shop+=1
shops.append((shop, "Alison Elmshaper's Flying Arrow Fletching Shop", 'https://runescape.wikia.com/wiki/Alison_Elmshaper%27s_Flying_Arrow_Fletching_Shop', npc, loc))
stock.append((shop, 314, 15, 0, 0)) # Feather
stock.append((shop, 39, 15, 0, 0)) # Bronze arrowhead
stock.append((shop, 1777, 1, 0, 0)) # Bowstring
stock.append((shop, 946, 10, 25, 7)) # Knife
stock.append((shop, 314, 100, 6, 1)) # Feather
stock.append((shop, 39, 15, 10, 3)) # Bronze arrowhead
stock.append((shop, 1777, 15, 100, 30)) # Bowstring

npc+=1
npcs.append((npc, 'Ayleth Beaststalker', 'https://runescape.wikia.com/wiki/Ayleth_Beaststalker'))

shop+=1
shops.append((shop, "Ayleth Beaststalker's Hunting Supplies Shop", 'https://runescape.wikia.com/wiki/Ayleth_Beaststalker%27s_Hunting_Supplies_Shop', npc, loc))
stock.append((shop, 10006, 1, 0, 0)) # Bird snare
stock.append((shop, 10010, 10, 24, 7)) # Butterfly net
stock.append((shop, 10012, 300, 1, 1)) # Butterfly jar
stock.append((shop, 10150, 10, 4, 1)) # Noose wand
stock.append((shop, 10006, 30, 6, 1)) # Bird snare

npc+=1
npcs.append((npc, 'Head Farmer Jones', 'https://runescape.wikia.com/wiki/Head_Farmer_Jones'))

shop+=1
shops.append((shop, "Head Farmer Jones's Farming Shop", 'https://runescape.wikia.com/wiki/Head_Farmer_Jones%27s_Farming_Shop', npc, loc))
stock.append((shop, 5318, 3, 0, 0)) # Potato seed
stock.append((shop, 1942, 1, 0, 0)) # Raw potato
stock.append((shop, 5318, 10, 8, 2)) # Potato seed
stock.append((shop, 5319, 10, 10, 3)) # Onion seed
stock.append((shop, 5324, 10, 25, 7)) # Cabbage seed
stock.append((shop, 5322, 10, 4, 1)) # Tomato seed
stock.append((shop, 5320, 10, 8, 2)) # Sweetcorn seed
stock.append((shop, 5323, 10, 18, 6)) # Strawberry seed
stock.append((shop, 5331, 30, 8, 2)) # Watering can
stock.append((shop, 6032, 300, 20, 6)) # Compost
stock.append((shop, 5350, 100, 1, 1)) # Plant pot
stock.append((shop, 5343, 10, 6, 2)) # Seed dibber
stock.append((shop, 5325, 10, 12, 4)) # Gardening trowel
stock.append((shop, 952, 10, 3, 1)) # Spade
stock.append((shop, 5329, 10, 5, 1)) # Secateurs
stock.append((shop, 5341, 10, 6, 2)) # Rake
stock.append((shop, 5345, 10, 25, 8)) # Gardening boots
stock.append((shop, 1925, 100, 2, 1)) # Bucket
stock.append((shop, 5418, 60, 1, 1)) # Empty sack 10 + 50 from pack
stock.append((shop, 5376, 60, 1, 1)) # Basket 10 + 50 from pack
stock.append((shop, 6036, 10, 40, 13)) # Plant cure
stock.append((shop, 12608, 10, 200, 66)) # Amulet of farming (1) ???tradeable???
stock.append((shop, 12622, 10, 200, 66)) # Amulet of farming (8)
stock.append((shop, 1735, 20, 1, 1)) # Shears

npc+=1
npcs.append((npc, 'Jack Oval', 'https://runescape.wikia.com/wiki/Jack_Oval'))

shop+=1
shops.append((shop, "Jack Oval's crafting Shop", 'https://runescape.wikia.com/wiki/Jack_Oval%27s_crafting_Shop', npc, loc))
stock.append((shop, 1734, 10, 0, 0)) # Thread
stock.append((shop, 1925, 1, 0, 0)) # Bucket
stock.append((shop, 1931, 1, 0, 0)) # Empty pot
stock.append((shop, 1755, 14, 14, 4)) # Chisel
stock.append((shop, 1733, 10, 1, 1)) # Needle
stock.append((shop, 1734, 5, 4, 1)) # Thread
stock.append((shop, 1925, 10, 2, 1)) # Bucket
stock.append((shop, 1735, 10, 1, 1)) # Shears
stock.append((shop, 1592, 1, 5, 1)) # Ring mould
stock.append((shop, 1595, 1, 5, 1)) # Amulet mould
stock.append((shop, 1597, 1, 5, 1)) # Necklace mould
stock.append((shop, 11065, 1, 5, 1)) # Bracelet mould
stock.append((shop, 1599, 1, 5, 1)) # Holy mould
stock.append((shop, 5523, 1, 100, 33)) # Tiara mould
stock.append((shop, 2976, 10, 10, 3)) # Sickle mould
stock.append((shop, 9434, 10, 25, 8)) # Bolt mould

npc+=1
npcs.append((npc, 'Marcus Everburn', 'https://runescape.wikia.com/wiki/Marcus_Everburn'))

shop+=1
shops.append((shop, "Marcus Everburn's Firemaking Shop", 'https://runescape.wikia.com/wiki/Marcus_Everburn%27s_Firemaking_Shop', npc, loc))
stock.append((shop, 596, 10, 4, 1)) # Unlit torch
stock.append((shop, 590, 10, 1, 1)) # Tinderbox

npc+=1
npcs.append((npc, 'Martin Steelweaver', 'https://runescape.wikia.com/wiki/Martin_Steelweaver'))

shop+=1
shops.append((shop, "Martin Steelweaver's Smithing Supplies Shop", 'https://runescape.wikia.com/wiki/Martin_Steelweaver%27s_Smithing_Supplies_Shop', npc, loc))
stock.append((shop, 2347, 10, 13, 3)) # Hammer

npc+=1
npcs.append((npc, 'Nicholas Angle', 'https://runescape.wikia.com/wiki/Nicholas_Angle'))

shop+=1
shops.append((shop, "Nicholas Angle's Fishing Shop", 'https://runescape.wikia.com/wiki/Nicholas_Angle%27s_Fishing_Shop', npc, loc))
stock.append((shop, 313, 10, 0, 0)) # Fishing bait
stock.append((shop, 13431, 10, 20, 6)) # Crayfish cage
stock.append((shop, 303, 40, 40, 12)) # Small fishing net
stock.append((shop, 307, 10, 5, 1)) # Fishing rod
stock.append((shop, 313, 10, 3, 1)) # Fishing bait

npc+=1
npcs.append((npc, 'Poletax', 'https://runescape.wikia.com/wiki/Poletax'))

shop+=1
shops.append((shop, "Poletax's Herblore Shop", 'https://runescape.wikia.com/wiki/Poletax%27s_Herblore_Shop', npc, loc))
stock.append((shop, 227, 1, 0, 0)) # Vial of water
stock.append((shop, 221, 1, 0, 0)) # Eye of newt
stock.append((shop, 199, 1, 0, 0)) # Grimy guam
stock.append((shop, 229, 310, 5, 1)) # Vial, 10 + 6*50 from packs
stock.append((shop, 227, 2020, 10, 3)) # Vial of water, 20 + 40*50 from packs
stock.append((shop, 233, 10, 4, 1)) # Pestle and mortar
stock.append((shop, 221, 1010, 3, 1)) # Eye of newt, 10 + 20*50
stock.append((shop, 235, 5, 20, 6)) # Unicorn horn dust
stock.append((shop, 225, 5, 7, 2)) # Limpwurt root
stock.append((shop, 239, 5, 10, 3)) # White berries
stock.append((shop, 1951, 5, 3, 1)) # Redberries
stock.append((shop, 1470, 5, 4, 1)) # Red bead
stock.append((shop, 1472, 5, 4, 1)) # Yellow bead
stock.append((shop, 1474, 5, 4, 1)) # Black bead
stock.append((shop, 1476, 5, 4, 1)) # White bead
stock.append((shop, 948, 5, 10, 3)) # Bear fur

npc+=1
npcs.append((npc, 'Tobias Bronzearms', 'https://runescape.wikia.com/wiki/Tobias_Bronzearms'))

shop+=1
shops.append((shop, "Tobias Bronzearms's Mining Supplies Shop", 'https://runescape.wikia.com/wiki/Tobias_Bronzearms%27s_Mining_Supplies_Shop', npc, loc))
stock.append((shop, 1265, 10, 1, 1)) # Bronze pickaxe

npc+=1
npcs.append((npc, 'Will Oakfeller', 'https://runescape.wikia.com/wiki/Will_Oakfeller'))

shop+=1
shops.append((shop, "Will Oakfeller's Woodcutting Supplies Shop", 'https://runescape.wikia.com/wiki/Will_Oakfeller%27s_Woodcutting_Supplies_Shop', npc, loc))
stock.append((shop, 1351, 10, 16, 5)) # Bronze hatchet
stock.append((shop, 1349, 10, 56, 18)) # Iron hatchet
stock.append((shop, 1353, 10, 200, 66)) # Steel hatchet



c.execute('''DELETE FROM location''')
c.executemany('''INSERT INTO location (id, name, url) VALUES (?, ?, ?)''', locations)
conn.commit()

c.execute('''DELETE FROM npc''')
c.executemany('''INSERT INTO npc (id, name, url) VALUES (?, ?, ?)''', npcs)
conn.commit()

c.execute('''DELETE FROM shop''')
c.executemany('''INSERT INTO shop (id, name, url, owner, location) VALUES (?, ?, ?, ?, ?)''', shops)
conn.commit()

c.execute('''DELETE FROM stock''')
c.executemany('''INSERT INTO stock (shop, item, qty, sell_price, buy_price) VALUES (?, ?, ?, ?, ?)''', stock)
conn.commit()

conn.close()
