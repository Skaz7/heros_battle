from areas import *
from classes import TreasureChest
from data.objects import life_potion
from data.weapons import excalibur
from data.characters import thomas


small_chest = TreasureChest(
    name="Red Chest",
    description="A red chest with a gold key inside.",
    size=1,
    items=[excalibur, life_potion],
    trapped=True,
    opened=False,
)

forest = Area(
    name="Forest",
    description="A dark old forest.",
    available_directions=["Town", "Clearing", "Cliff"],
    enemies=["Goblin", "Orc"],
    treasure=small_chest,
    npc=None,
    visited=False,
)
town = Area(
    name="Town",
    description="A Town with many people.",
    available_directions=["Forest", "Coast", "Ruins", "Plains"],
    enemies=None,
    treasure=None,
    npc=thomas,
    store=Shop(),
    visited=False,
)
ruins = Area(
    name="Ruins",
    description="A ruined castle.",
    available_directions=["Town", "Clearing", "Swamp"],
    enemies=["Dragon"],
    treasure=small_chest,
    npc=None,
    visited=False,
)
plains = Area(
    name="Plains",
    description="A plains.",
    available_directions=["Docks", "Town", "Swamp"],
    enemies=["Thief"],
    treasure=None,
    npc=None,
    visited=False,
)

cliff = Area(
    name="Cliff",
    description="A Cliff.",
    available_directions=["Coast", "Forest"],
    enemies=["Pirate"],
    treasure=None,
    npc=None,
    visited=False,
)

coast = Area(
    name="Coast",
    description="A Coast.",
    available_directions=["Docks", "Town", "Cliff"],
    enemies=["Pirate"],
    treasure=None,
    npc=None,
    visited=False,
)

docks = Area(
    name="Docks",
    description="A Docks.",
    available_directions=["Docks", "Plains"],
    enemies=["Robber"],
    treasure=None,
    npc=None,
    store=Blacksmith(),
    visited=False,
)

clearing = Area(
    name="Clearing",
    description="A Clearing.",
    available_directions=["Ruins", "Forest"],
    enemies=None,
    treasure=None,
    npc=None,
    visited=False,
)

swamp = Area(
    name="Swamp",
    description="A Swamp.",
    available_directions=["Plains", "Ruins"],
    enemies=["Dragon"],
    treasure=None,
    npc=None,
    store=Temple(),
    visited=False,
)

areas = {
    "Forest": forest,
    "Town": town,
    "Plains": plains,
    "Ruins": ruins,
    "Docks": docks,
    "Cliff": cliff,
    "Coast": coast,
    "Clearing": clearing,
    "Swamp": swamp,
}
