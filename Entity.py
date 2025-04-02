class Entity:
    """
    Entity is an object that exists in the world. It has a position.

    Attributes
    ----------
    position : tuple[int, int]
        The location of the Entity in 2d space, represented as (x, y).

    Methods
    -------
    move(destination: tuple[int, int]) -> None
        Updates the Entity's location to a given destination, represented as (x, y).
    destroy() -> None
        Deletes the Entity.
    """

    def __init__(self, starting_position: tuple[int, int]=(0, 0)) -> None:
        """
        Parameters
        ----------
        starting_position: tuple[int, int]=(0, 0)
            The Entity's starting location in the world, represented as (x, y).
        """
        self.position : tuple[int, int] = starting_position
    

    def move(self, destination: tuple[int, int]) -> None:
        """
        Updates the Entity's location to a given destination, represented as (x, y).

        Parameters
        ----------
        destination: tuple[int, int]
            The location the Entity will move to.
        """
        self.position = destination
        print(f"{self} moved to {destination}")


    def destroy(self) -> None:
        """Deletes the Entity."""
        print(f"Destroying {self}!")
        del self
