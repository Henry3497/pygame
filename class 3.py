# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:59:03 2020

@author: Henry
"""
from mcpi.minecraft import  Minecraft

mc = Minecraft.create()

position =mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
mc.grass(x, y, z, + 3,5)
