class UserPower:
    def __init__(self, ) -> None:
        """
        self.user_power =>  Literal[0,1,2] 0权限最高 2权限最低
        """
        self.powers = {
            "LOGIN": True,  # 是否有权登陆

        }
        # self.user_power=powerLevel

    @property
    def user_power(self) -> int:
        # self.user_power = 0
        return self._user_power

    @user_power.setter
    def user_power(self, value: int) -> None:
        if value in [0, 1, 2]:
            self._user_power = value
        else:
            raise ValueError("user_power must be in [0,1,2]")


class ShaidenPower_UserPower(UserPower):
    def __init__(self) -> None:
        super().__init__()
        self.user_power = 0

    def __str__(self) -> str:
        return "admin"


class ShaidenPower_UserPower_int(int):
    def __init__(self) -> None:
        super().__init__()
        self.user_power = 0

    def __int__(self):
        return self.user_power
