from creatureclass import Status


# create statuses
bleed = Status(
    name="Bleed",
    description="Bleeding",
    duration=3,
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
