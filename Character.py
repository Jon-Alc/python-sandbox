from Entity import Entity
from IDamageable import IDamageable


class Character(Entity, IDamageable):
    """
    Character is an Entity that can take damage.

    Attributes
    ----------
    position : tuple[int, int]
        The location of the Character in 2d space, represented as (x, y).
    current_health : int
        How much health the Character currently has.
    max_health : int
        The maximum amount of health the Character can have at once.

    Methods
    -------
    move(destination: tuple[int, int]) -> None
        Updates the Character's location to a given destination, represented as (x, y).
        (From Entity superclass)
    destroy() -> None
        Deletes the Character.
        (From Entity superclass)
    take_damage(damage_amount: int) -> None
        Decreases the Character's current health by a given amount. If the Character's
        health hits 0, on_health_depleted() is called.
    on_health_depleted() -> None
        Calls destroy() when the Character's current health reaches 0.
    """

    def __init__(self,
                starting_position: tuple[int, int],
                starting_health: int,
                max_health: int) -> None:
        """
        Constructor for the Character class.

        Parameters
        ----------
        starting_position: tuple[int, int]=(0, 0)
            The Character's starting location in the world, represented as (x, y).
        starting_health: int
            The Character's health to start with.
        max_health: int
            The maximum amount of health the Character can have at once.
        """
        self.position : tuple[int, int] = starting_position
        self.current_health : int = starting_health
        self.max_health : int = max_health
    

    def take_damage(self, damage_amount: int):
        """
        Decreases the Character's current health by a given amount. If the Character's
        health hits 0, on_health_depleted() is called.

        Parameters
        ----------
        damage_amount: int
            The amount to subtract from the Character's current health.
        """
        self.current_health -= damage_amount
        if self.current_health <= 0:
            self.on_health_depleted()
    

    def on_health_depleted(self):
        """
        Calls destroy() when the Character's current health reaches 0.
        """
        self.destroy()