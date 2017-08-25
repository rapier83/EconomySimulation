import numpy as np
import Exceptions as ex
import pandas as pd
# import matplotlib.pyplot as plt
import seaborn as sb

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

    class Player:

        def __init__(self):
            self.id = str()
            self.Income = None
            self.Consume = None

        def SetData(self, style="df"):
            pass

        def SetDataAsDataFrame(self, df):
            pass

        def SetDataAsDict(self, dic):
            self.Income = dic

        def GetData(self, style="df"):
            pass

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

            def GetRandoms(mu=0, sig=0.1, size=None, pos=True):
                if size is None:
                    raise ValueError
                rs = np.random.RandomState(8)
                s = rs.normal(mu, sig, size=pop)
                if pos:
                    s = np.add(s, abs(np.min(s)))
                return s

            PlayersDF['Productivity'] = GetRandoms(size=pop)
            PlayersDF['ConsumeIndex'] = GetRandoms(size=pop)

            labor = int(pop * (1 - self.SystemValues['LaborRatio']))
            labors = np.random.choice(pop, labor, replace=False)
            PlayersDF['isLabor'] = False
            PlayersDF.loc[labors, 'isLabor'] = True
            PlayersDF['Income'] = list(np.random.random(pop))

        self.PlayerData = PlayersDF

    def ResetPlayersData(self):
        self.PlayerData = None

    @staticmethod
    def GetDict():
        return 0

    def GetGini(self, y):

        """
        https://en.wikipedia.org/wiki/Gini_coefficient
        :param y: pd.DataFrame() or list() - Players Account Data
        :return: float() - Gini Coefficient of Current Epoch(Year, Time)
        """

        n = len(y)
        numerator = 2 * sum((i + 1) * y[i] for i in range(n))
        denominator = len(y) * sum(y[i] for i in range(n))
        g = numerator / denominator + (n + 1) / n

        return g

    def GetMatrix(self):
        if type(self.PlayerData) == type(pd.DataFrame()):
            return self.PlayerData.as_matrix(columns=['Productivity', 'ConsumeIndex', 'BizIncome', 'EarnedIncome'])

    def ShowChart(self, style="hist", x="Income", y="", ):

        if style == "hist":
            sb.distplot(self.PlayerData[x], bins=20)


if __name__ == '__main__':
    n = 10 ** 5
    t = 0.1
    s = System()
    s.InitiateSystem(n)
    s.DeployPlayers()
