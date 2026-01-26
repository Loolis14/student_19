def healing_potion():
    from .elements import create_fire, create_water
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    from .elements import create_fire, create_earth
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    from alchemy.elements import create_water, create_air
    return (f"Invisibility potion brewed "
            f"with {create_air()} and {create_water()}")


def wisdom_potion():
    import alchemy.elements as f
    return (f"Wisdompotion brewed with all elements: "
            f"{f.create_fire(), f.create_water()}"
            f"{f.create_air(), f.create_earth()}")
