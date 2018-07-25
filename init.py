import sqlite3
import sys

conn = sqlite3.connect('rs.sqlite')

c = conn.cursor()

c.execute('''CREATE TABLE "category" (
    `id` INTEGER NOT NULL,
    `name` TEXT NOT NULL,
    PRIMARY KEY(`id`) )''')
c.execute('''CREATE TABLE "item" (
    `id` INTEGER NOT NULL,
    `name` TEXT NOT NULL,
    `description` TEXT NOT NULL,
    `icon` TEXT NOT NULL,
    `icon_large` TEXT NOT NULL,
    `category` INTEGER NOT NULL,
    `members` BOOLEAN NOT NULL,
    `current_price` INTEGER NOT NULL,
    PRIMARY KEY(`id`) )''')
c.execute('''CREATE TABLE "location" (
    `id` INTEGER NOT NULL, 
    `name` TEXT NOT NULL,
    `url` TEXT,
    PRIMARY KEY(`id`) )''')
c.execute('''CREATE TABLE "npc" (
    `id` INTEGER NOT NULL,
    `name` TEXT NOT NULL,
    `url` TEXT,
    PRIMARY KEY(`id`) )''')
c.execute('''CREATE TABLE "shop" (
    `id` INTEGER NOT NULL,
    `name` TEXT NOT NULL,
    `url` TEXT NOT NULL,
    `owner` INTEGER NOT NULL,
    `location` INTEGER NOT NULL,
    PRIMARY KEY(`id`) )''')
c.execute('''CREATE TABLE "stock" (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `shop` INTEGER NOT NULL,
    `item` INTEGER NOT NULL,
    `qty` INTEGER NOT NULL,
    `sell_price` INTEGER NOT NULL,
    `buy_price` INTEGER )''')
c.execute('''CREATE UNIQUE INDEX `shop_item_sell_price` ON `stock` ( `shop`, `item`, `sell_price` )''')

conn.commit()

conn.close()
