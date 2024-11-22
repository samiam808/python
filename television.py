class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__previous_volume = self.__volume

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            else:
                self.__muted = True
                self.__previous_volume = self.__volume
                self.__volume = 0

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'