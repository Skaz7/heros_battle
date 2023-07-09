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
    available_directions=["Town", "Plains", "Ruins"],
    enemies=["Goblin", "Orc"],
    treasures=["Small chest"],
    npcs=["Old Man"],
    visited=False,
)
town = Area(
    name="Town",
    description="A Town with many people.",
    available_directions=["Forest", "Plains", "Ruins"],
    enemies=None,
    treasures=None,
    npcs=["Merchant"],
    visited=False,
)

areas = {
    "Forest": forest,
    "Town": town,
    "Plains": None,
    "Ruins": None,
}
