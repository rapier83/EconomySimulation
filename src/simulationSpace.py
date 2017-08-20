import numpy as np
import Exceptions as ec
import pandas as pd

__doc__ = """
        # 시스템의 변수들을 정의한다
        # 플레이어들의 변수를 정의한다
        # 각 반복마다 영향을 주는 변수를 정의한다
        # 각 반복마다 변수들이 어떤 영향을 주고 받는지 정의한다
        """


class Player:
    """
    `attributeOfPlayer` 변수가 1차원 이상인 경우 다음의 변수들을 선택하여 할당한다.
    1.id: Player 구분값
    2.잔고: 남아있는 재산값(Account), 종속변수, Save = Income - Tax - consumption
    3.수입: 매회 벌어들이는 재산값, 독립변수 통제가능, 생산성으로 통제한다.
    4.근로소득 외: Player 중 일부는 재산이 일정 수준 이상이 되면 재산소득(이자, 지대 등)을 얻는다
    5.사업소득: Player 중 일부는 사업소득을 받는다.
    6.기타(**kwarg, key word argument): 비율인지 값인지 판단 한 후 비율 * 값 의 결과를 PlayerData 에 포함시킨다.
    """

    def __init__(self, _id, PlayerData, **kwargs):
        self.id = _id
        self.PersonalData = {
            'Productivity': PlayerData['Productivity'],
            'EarnIncome': PlayerData['EarnedIncome'],
        }
        self.AddtionalArgs = dict().update(kwargs)
        # TODO: kwargs 판단 후 TotalIncome 에 포함함 추후 작성

        self.Account = {'TotalIncome': self.attr['BizIncome'] + self.attr['EarnedIncome'],
                        'DisposableIncome': self.Account['TotalIncome'] * (1 - PlayerData['TaxRate'] - PlayerData['ConsumeIndex'])}



class System:
    
    """
    1.Player 의 수입 Player.Income 에서 차감하는 비율 System.Taxation 을 정한다.
    2.System.Taxation 에 따라 가처분소득 Player.DisposableIncome 을 계산한다.
    """

    def __init__(self, Population: int=100, Taxation: int=0.1, LaborRatio: float=0.3, Productivity: bool=False, Consume: bool=False, **kwargs: dict()):

        """
        By kwarg, Include additional attributes of Player
        :type kwargs: dict()
        """
        try:
            if type(Population) != int:
                raise ec.isInteger()
            self.Population = Population

        except ec.isInteger as Err:
            print(f'{Err}: Population.')

        try:
            if Taxation <= 0 or Taxation >= 1:
                raise ec.isRate()
            self.Taxation = Taxation
        except ec.isRate as Err:
            print(f'{Err}: Taxation.')

        try:
            if kwargs.values() != type(bool):
                raise ec.isBool()
            self.attr = dict(kwargs)
        except ec.isBool as Err:
            print(f'{Err} : Additional argument.')

        self.SystemValues = {
            'Population': Population,
            'TaxRate': Taxation,
            'ProductivityControl': Productivity,
            'ConsumeIndexControl': Consume,
            'LaborRatio': LaborRatio
        }
        # self.Players = pd.DataFrame

        self.AdditionalValues = kwargs
        # TODO: 판단 후 계산 시행

    def DeployPlayers(self, **kwargs):
        self.Players = pd.DataFrame
        pop = self.SystemValues['Population']
        labor = int(pop * (1 - self.SystemValues['LaborRatio']))
        labors = np.random.choice(pop, labor, replace=False)
        columns = ['_id', 'isLabor', 'Productivity', 'ConsumeIndex', 'BizIncome', 'EarnedIncome']
        self.Players = pd.DataFrame(columns=columns)
        self.Players['_id'] = np.arange(0, pop)
        self.Players['isLabor'] = False
        self.Players.loc[labors, 'isLabor'] = True
        self.Players['Productivity'] = np.random.random(pop)
        self.Players['ConsumeIndex'] = np.random.random(pop)
        self.Players.loc[self.Players['isLabor'] == False, 'BizIncome'] = np.random.random(pop - labor)
        self.Players.loc[self.Players['isLabor'] == True, 'EarnedIncome'] = np.random.random(labor)
        if kwargs:
            pass

    def StartOperation(self, n):
        pass

    def GetData(self):
        return self.__dict__


if __name__ == '__main__':
    n = 10 ** 5
    s = System(n)
    s.DeployPlayers()
