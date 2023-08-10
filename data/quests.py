from classes import Quest


find_dog = Quest(
    name="Find dog",
    description="""My daughter lost her beloved dog in the woods.
                 If you can find it, I'll reward you with 100 gold and one item.""",
    reward={"gold": 100},
    completed=False,
)
