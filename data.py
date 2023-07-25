from world import Area

weaknesses = [
    "slash",
    "blunt",
    "stab",
    "fire",
    "water",
    "wind",
    "ice",
    "poison",
    "electric",
]
resistances = [
    "slash",
    "blunt",
    "stab",
    "fire",
    "water",
    "wind",
    "ice",
    "poison",
    "electric",
]

states = [
    "frozen",
    "burn",
    "poisoned",
    "shocked",
    "scared",
    "sleep",
    "blind",
]


forest = Area(
    name="Forest",
    description="A dark old forest.",
    available_directions=["Town", "Clearing", "Cliff"],
    enemies=["Goblin", "Orc"],
    treasures=["Small chest"],
    npcs=["Old Man"],
    visited=False,
)
town = Area(
    name="Town",
    description="A Town with many people.",
    available_directions=["Forest", "Coast", "Ruins", "Plains"],
    enemies=None,
    treasures=None,
    npcs=["Merchant"],
    visited=False,
)
ruins = Area(
    name="Ruins",
    description="A ruined castle.",
    available_directions=["Town", "Clearing", "Swamp"],
    enemies=["Dragon"],
    treasures=["Small chest"],
    npcs=None,
    visited=False,
)
plains = Area(
    name="Plains",
    description="A plains.",
    available_directions=["Docks", "Town", "Swamp"],
    enemies=["Thief"],
    treasures=None,
    npcs=None,
    visited=False,
)

cliff = Area(
    name="Cliff",
    description="A Cliff.",
    available_directions=["Coast", "Forest"],
    enemies=["Pirate"],
    treasures=None,
    npcs=None,
    visited=False,
)

coast = Area(
    name="Coast",
    description="A Coast.",
    available_directions=["Docks", "Town", "Cliff"],
    enemies=["Pirate"],
    treasures=None,
    npcs=None,
    visited=False,
)

docks = Area(
    name="Docks",
    description="A Docks.",
    available_directions=["Docks", "Plains"],
    enemies=["Robber"],
    treasures=None,
    npcs=None,
    visited=False,
)

clearing = Area(
    name="Clearing",
    description="A Clearing.",
    available_directions=["Ruins", "Forest"],
    enemies=None,
    treasures=None,
    npcs=None,
    visited=False,
)

swamp = Area(
    name="Swamp",
    description="A Swamp.",
    available_directions=["Plains", "Ruins"],
    enemies=["Dragon"],
    treasures=None,
    npcs=None,
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
