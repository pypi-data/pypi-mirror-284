"""A module containing the GameVersion class."""
from typing import Any


class GameVersion:
    """A class to represent a game version."""

    def __init__(self, game_version: int):
        """Initializes a new instance of the GameVersion class.

        Args:
            game_version (int): Game version as an integer. e.g 120102 for 12.1.2
        """
        self.game_version = game_version

    def to_string(self) -> str:
        """Converts the game version to a string.

        Returns:
            str: Game version as a string. e.g 12.1.2
        """
        split_gv = str(self.game_version).zfill(6)
        split_gv = [str(int(split_gv[i : i + 2])) for i in range(0, len(split_gv), 2)]
        return ".".join(split_gv)

    def get_parts_zfill(self) -> list[str]:
        """Gets the parts of the game version as a list of strings with leading zeros.

        Returns:
            list[str]: Game version parts as strings with leading zeros. e.g ["12", "01", "02"]
        """
        return [part.zfill(2) for part in self.to_string().split(".")]

    def get_parts(self) -> list[int]:
        """Gets the parts of the game version as a list of integers.

        Returns:
            list[int]: Game version parts as integers. e.g [12, 1, 2]
        """
        return [int(part) for part in self.get_parts_zfill()]

    def format(self) -> str:
        """Formats the game version as a string with leading zeros.

        Returns:
            str: Game version as a string with leading zeros. e.g 12.01.02
        """
        parts = self.get_parts_zfill()
        string = ""
        for part in parts:
            string += f"{part}."
        return f"{string[:-1]}"

    def __str__(self) -> str:
        """Converts the game version to a string.

        Returns:
            str: Game version as a string. e.g 12.1.2
        """
        return self.to_string()

    def __repr__(self) -> str:
        """Converts the game version object to a string.

        Returns:
            str: Game version object as a string. e.g game_version(120102) 12.1.2
        """
        return f"game_version({self.game_version}) {self.to_string()}"

    @staticmethod
    def from_string(game_version: str) -> "GameVersion":
        """Converts a string to a GameVersion object.

        Args:
            game_version (str): Game version as a string. e.g 12.1.2

        Returns:
            GameVersion: Game version as a GameVersion object.
        """
        split_gv = game_version.split(".")
        if len(split_gv) == 2:
            split_gv.append("0")
        final = ""
        for split in split_gv:
            final += split.zfill(2)
        return GameVersion(int(final))

    def __eq__(self, other: Any) -> bool:
        """Checks if the game version is equal to another object.

        Args:
            other (Any): Object to compare to.

        Returns:
            bool: True if the game version is equal to the other object, False otherwise.
        """
        if isinstance(other, GameVersion):
            return self.game_version == other.game_version
        elif isinstance(other, int):
            return self.game_version == other
        elif isinstance(other, str):
            return self.game_version == GameVersion.from_string(other).game_version
        else:
            return False

    def __ne__(self, other: Any) -> bool:
        """Checks if the game version is not equal to another object.

        Args:
            other (Any): Object to compare to.

        Returns:
            bool: True if the game version is not equal to the other object, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other: Any) -> bool:
        """Checks if the game version is less than another object.

        Args:
            other (Any): Object to compare to.

        Returns:
            bool: True if the game version is less than the other object, False otherwise.
        """
        if isinstance(other, GameVersion):
            return self.game_version < other.game_version
        elif isinstance(other, int):
            return self.game_version < other
        elif isinstance(other, str):
            return self.game_version < GameVersion.from_string(other).game_version
        else:
            return False

    def __le__(self, other: Any) -> bool:
        """Checks if the game version is less than or equal to another object.

        Args:
            other (Any): Object to compare to.

        Returns:
            bool: True if the game version is less than or equal to the other object, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: Any) -> bool:
        """Checks if the game version is greater than another object.

        Args:
            other (Any): Object to compare to.

        Returns:
            bool: True if the game version is greater than the other object, False otherwise.
        """
        return not self.__le__(other)

    def __ge__(self, other: Any) -> bool:
        """Checks if the game version is greater than or equal to another object.

        Args:
            other (Any): Object to compare to.

        Returns:
            bool: True if the game version is greater than or equal to the other object, False otherwise.
        """
        return not self.__lt__(other)
