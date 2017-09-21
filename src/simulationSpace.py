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
# Sep.21.2017 괜히 gitbook 과 연동시키다가 망했음

class System:

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

    def InitiateSystem(self, Population: int = 100, TaxRate: int = 0.1, LaborRatio: float = 0.3,  # System Value
                       Productivity: bool = False, Consume: bool = False,  # Player Control
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

        if type(style) is not str:
            raise TypeError

        pop = self.SystemValues['Population']
        NotNumber = 2
        columns = ['_id', 'isLabor', 'Productivity', 'ConsumeIndex', 'Income']
        labor = int(pop * (1 - self.SystemValues['LaborRatio']))
        labors = np.random.choice(pop, labor, replace=False)

        def GetRandoms(mu=0, sig=0.1, size=None, pos=True):
            if size is None:
                raise ValueError
            rs = np.random.RandomState(8)
            d = rs.normal(mu, sig, size=pop)
            if pos:
                d = np.add(d, abs(np.min(d)))
            return d

        if kwargs is not None:
            pass

        if style is "dict":
            pass

        if style is "Matrix" or style is "matrix":
            m = np.zeros((pop, len(columns)))
            m[:, :1] = np.matrix(np.arange(int(pop))).transpose()
            m[labors, 1] = 1
            m[:, m.shape[1]-NotNumber-1] = GetRandoms(size=(pop, m.shape[1]-NotNumber-1))
            PlayerData = m

        if style is "df":
            self.PlayerData = pd.DataFrame()

            df = pd.DataFrame(columns=columns)

            df['_id'] = np.arange(0, pop)
            df['Productivity'] = GetRandoms(size=pop)
            df['ConsumeIndex'] = GetRandoms(size=pop)
            df['isLabor'] = False
            df.loc[labors, 'isLabor'] = True
            df['Income'] = list(np.random.random(pop))
            PlayerData = df

        self.PlayerData = PlayerData

    def ResetPlayersData(self):
        self.PlayerData = None

    @staticmethod
    def GetDict():
        return 0

    @property
    def GetGini(self):

        """
        https://en.wikipedia.org/wiki/Gini_coefficient
        :param y: pd.DataFrame() or list() - Players Account Data
        :return: float() - Gini Coefficient of Current Epoch(Year, Time)
        """
        if isinstance(self.PlayerData, np.matrix):
            y = self.PlayerData.shape[0]

        if isinstance(self.PlayerData, pd.DataFrame):
            y = len(self.PlayerData)

        n = len(y)
        numerator = 2 * sum((i + 1) * y[i] for i in range(n))
        denominator = len(y) * sum(y[i] for i in range(n))
        g = numerator / denominator + (n + 1) / n

        return g

    @property
    def GetMatrix(self):
        if isinstance(self.PlayerData, pd.DataFrame):
            return self.PlayerData.as_matrix(columns=['Productivity', 'ConsumeIndex', 'Income'])

    def ShowChart(self, style="hist", x="Income", y=None, ):

        if style == "hist":
            sb.distplot(self.PlayerData[x], bins=20)


if __name__ == '__main__':
    n = 10 ** 5
    t = 0.1
    s = System()
    s.InitiateSystem(n)
