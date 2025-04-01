from abc import ABC, abstractmethod


class IDamageable(ABC):
    """
    IDamageable is an abstract class/interface meant to be used with Entity.
    Implementing IDamageable means the Entity can take damage.

    Attributes
    ----------
    current_health : int
        How much health the Entity currently has.
    max_health : int
        The maximum amount of health the Entity can have at once.

    Methods
    -------
    take_damage(damage_amount: int) -> None
        Should be called when this Entity takes damage. To be implemented by the subclass.
    on_health_depleted() -> None
        Should be called when this Entity's health goes to 0 or lower.To be implemented by
        the subclass.
    """

    def __init__(self, starting_health: int, max_health: int) -> None:
        """
        Constructor for the IDamageable interface.

        Parameters
        ----------
        starting_health: int
            The Entity's health to start with.
        max_health: int
            The maximum amount of health the Entity can have at once.
        """
        self.current_health : int = starting_health
        self.max_health : int = max_health
    

    @abstractmethod
    def take_damage(self, damage_amount: int) -> None:
        """
        Should be called when this Entity takes damage. To be implemented by the subclass.

        Parameters
        ----------
        damage_amount: int
            The amount of damage this Entity will take.
        """
        pass


    @abstractmethod
    def on_health_depleted(self):
        """
        Should be called when this Entity's health goes to 0 or lower.To be implemented by
        the subclass.
        """
        pass