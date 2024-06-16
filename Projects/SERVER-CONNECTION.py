class Execution:
    def __init__(self, Name: str, Roll: int) -> None:
        self.name = Name
        self.roll = Roll

    def __publishName(self) -> str:
        return self.name

    def __publishRoll(self) -> int:
        return self.roll

    def Publish(self) -> None:
        try:
            if ((roll := self.__publishRoll()) == 30 and (name := self.__publishName()) == 'ARNAB'):
                print(f'NAME IS {name}')
                print(f'ROLL IS {roll}')
            else:
                raise Exception('User not Validted...!')

        except Exception as err:
            status: str = 'is'
            if err:
                status = 'is Not'
                print(f'Server {status} Connected...!')

            print(err)

        finally:
            print('Execution Completed...!')


def main(name: str, roll: int) -> None:
    obj = Execution(name, roll)
    obj.Publish()


if __name__ == '__main__':
    main('ARNAB',30)
