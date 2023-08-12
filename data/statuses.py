from creatureclass import Status


# create statuses
bleed = Status(
    name="Bleed",
    description="Bleeding",
    duration=10,
    attribute_to_change="health",
    modification_value=5,
)

burn = Status(
    name="Burn",
    description="Burning",
    duration=3,
    attribute_to_change="health",
    modification_value=10,
)

poison = Status(
    name="Poison",
    description="Causes poison for 4 turns",
    duration=4,
    attribute_to_change="health",
    modification_value=2,
)
