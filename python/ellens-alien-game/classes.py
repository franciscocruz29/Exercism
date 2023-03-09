"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created: int = 0

    def __init__(self, x: int, y: int, health=3):
        """Initialize the alien"""
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Record a hit to alien health"""
        if self.health > 0:
            self.health -= 1

    def is_alive(self) -> bool:
        """Check alien vitals"""
        return self.health > 0

    def teleport(self, new_x: int, new_y: int) -> None:
        """assign new alien coordinates"""
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, *args) -> None:
        """Future collision detection implementation."""
        pass

# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


def new_aliens_collection(positions: list) -> list:
    """
    Creates a list of aliens from a collection of starting positions.

    :param positions: list - collection of starting coordinates for each alien to be created.
    :return: list - collection of newly created aliens.
    """

    return [Alien(position[0], position[1]) for position in positions]
