class Version:
    """
    Representation of a package version number.

    This resembles a semver scheme but doesn't necessarily
    follow one.

    Args:
        input (str): Version in string form x.y.zzzz

    Attributes:
        major (int): Major version number
        minor (int): Minor version number
        patch (int): Path version number
    """

    def __init__(self, input: str | None = None) -> None:
        self.major = 0
        self.minor = 0
        self.patch = 0

        if input:
            self.read(input)

    def read(self, input: str):
        """Read the version details from the input string.

        String is of form x.y.zzzz (major.minor.patch)

        Args:
            input (str): Version in string form x.y.zzzz
        """

        major, minor, patch = input.split(".")
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
