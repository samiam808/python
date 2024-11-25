class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        Creates a new television item

        sets the default states for the television
        status - TV is off
        muted - TV is not muted
        volume - MIN_VOLUME
        channel - MIN_CHANNEL
        previous_volume - MIN_VOLUME
        '''
        self.__status = False
        self.__muted = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__previous_volume: int = self.__volume

    def power(self) -> None:
        '''
        Turns the TV on and off
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        Mutes or unmutes the TV

        If the TV is on:
        - If muted, unmute the TV and restore the previous volume.
        - If not muted, mute the TV and set the volume to 0.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume: int = self.__previous_volume
            else:
                self.__muted = True
                self.__previous_volume: int = self.__volume
                self.__volume: int = 0

    def channel_up(self) -> None:
        '''
        Increase the channel number by 1.

        If the TV is on:
        - Increment the channel.
        - If the channel exceeds MAX_CHANNEL, wrap around to MIN_CHANNEL.
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel: int = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Decrease the channel number by 1.

        If the TV is on:
        - Decrement the channel.
        - If the channel goes below MIN_CHANNEL, wrap around to MAX_CHANNEL.

        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel: int = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Increase the volume by 1.

        If the TV is on:
        - Unmute the TV if it was muted and restore the previous volume.
        - Increment the volume.
        - If the volume exceeds MAX_VOLUME, do nothing.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume: int = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Decrease the volume by 1.

        If the TV is on:
        - Unmute the TV if it was muted and restore the previous volume.
        - Decrement the volume.
        - If the volume goes below MIN_VOLUME, do nothing.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume: int = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns a string with current TV details

        :return: str: A string 'Power = [status], Channel = [channel], Volume = [volume]'
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'