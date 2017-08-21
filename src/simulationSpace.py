import numpy as np
import Exceptions as ex
import pandas as pd

__doc__ = """
        # 시스템의 변수들을 정의한다
        # 플레이어들의 변수를 정의한다
        # 각 반복마다 영향을 주는 변수를 정의한다
        # 각 반복마다 변수들이 어떤 영향을 주고 받는지 정의한다
        """


class System:

    SystemValue = dict()
    AdditionalValue = dict()

    """
    1.Player 의 수입 Player.Income 에서 차감하는 비율 System.TaxRate 을 정한다.
    2.System.TaxRate 에 따라 가처분소득 Player.DisposableIncome 을 계산한다.
    """

    def __init__(self):
        self.SystemValues = dict()
        self.AdditionalValues = dict()
        self.PlayerData = None

    def InitiateSystem(self, Population: int=100, TaxRate: int=0.1, LaborRatio: float=0.3,  # System Value
                       Productivity: bool=False, Consume: bool=False,                       # Player Control
                       **kwargs):
        print(f'System Initiating | Population: {Population}, Tax Rate: {TaxRate}\n\r')

        try:
            if type(Population) != int:
                raise ex.isInteger()
        except ex.isInteger as err:
            print(f'{err}: Population.')

        try:
            if TaxRate <= 0 or TaxRate >= 1:
                raise ex.isRate()
        except ex.isRate as Err:
            print(f'{Err}: TaxRate.')

        self.SystemValues = {
            'Population': Population,
            'TaxRate': TaxRate,
            'ProductivityControl': Productivity,
            'ConsumeIndexControl': Consume,
            'LaborRatio': LaborRatio,
        }

        self.AdditionalValues = {
            'Name': None,
            'Date': None,
            'System Description': None,
        }
        self.AdditionalValues.update(kwargs)

    def DeployPlayers(self, style="df", **kwargs):

        if self.PlayerData is not None:
            raise ex.isNotEmpty

        if kwargs is not None:
            pass

        if style == "class":
            pass

        if style == "df":
            self.PlayerData = pd.DataFrame()
            pop = self.SystemValues['Population']

            columns = ['_id', 'isLabor', 'Productivity', 'ConsumeIndex', 'Income']

            PlayersDF = pd.DataFrame(columns=columns)

            PlayersDF['_id'] = np.arange(0, pop)
            PlayersDF['Productivity'] = np.random.random(pop)
            PlayersDF['ConsumeIndex'] = np.random.random(pop)

            labor = int(pop * (1 - self.SystemValues['LaborRatio']))
            labors = np.random.choice(pop, labor, replace=False)
            PlayersDF['isLabor'] = False
            PlayersDF.loc[labors, 'isLabor'] = True
            PlayersDF['Income'] = list(np.random.random(pop))

        self.PlayerData = PlayersDF

    def ResetPlayersData(self):
        self.PlayerData = None

    @staticmethod
    def GetDict(self):
        return self.__dict__

    def GetMatrix(self):
        if type(self.PlayerData) == type(pd.DataFrame()):
            return self.PlayerData.as_matrix(columns=['Productivity', 'ConsumeIndex', 'BizIncome', 'EarnedIncome'])


if __name__ == '__main__':
    n = 10 ** 5
    t = 0.1
    s = System()
    s.InitiateSystem()
    s.DeployPlayers()
