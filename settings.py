# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# World map

WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

# ui colors
HEALTH_COLOR = 'Color or the health'
ENERGY_COLOR = 'Color of the energy'
UI_BORDER_COLOR_ACTIVE = 'gold'

# Weapons
weapon_data = {
'sword':{'cooldown':100,'damage':15,'graphic':'PATH OF THE SWORD HERE'},
'lance':{'cooldown':400,'damage':30,'graphic':'PATH OF THE LANCE HERE'},
'axe':{'cooldown':300,'damage':20,'graphic':'PATH OF THE AXE HERE'},
'rapier':{'cooldown':50,'damage':8,'graphic':'PATH OF THE RAPIER HERE'},
'sai':{'cooldown':80,'damage':10,'graphic':'PATH OF THE SAI HERE'},
}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic':'PATH OF THE MAGIC '}
    'heal': {'strength': 20, 'cost': 10, 'graphic':'PATH OF THE MAGIC '}
}

# enemy
monster_data = {
    'squid': {'health': 100,'exp': 100,'damage': 20,'attack_type':'slash','attack_sound':'PATH AUDIO MONSTER', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360}
    'raccoon': {'health': 300,'exp': 250,'damage': 40,'attack_type':'claw','attack_sound':'PATH AUDIO MONSTER', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400}
    'spirit': {'health': 100,'exp': 110,'damage': 8,'attack_type':'thunder','attack_sound':'PATH AUDIO MONSTER', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350}
    'bamboo': {'health': 70,'exp': 120,'damage': 6,'attack_type':'leaf_attack','attack_sound':'PATH AUDIO MONSTER', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius':300}
}