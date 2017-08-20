import numpy as np
import Exceptions as ec

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

        self.attr = PlayerData
        self.attr.update(kwargs)
        # TODO: kwargs 판단 후 TotalIncome 에 포함함 추후 작성

        self.attr.update({'TotalIncome': self.attr['BizIncome'] + self.attr['EarnedIncome']})
        self.attr.update(dict(Account=self.attr['TotalIncome'] * (1 - self.attr['TaxRate'] - self.attr['Consume'])))


class System:
    
    """
    1.Player 의 수입 Player.Income 에서 차감하는 비율 System.Taxation 을 정한다.
    2.System.Taxation 에 따라 가처분소득 Player.DisposableIncome 을 계산한다.
    """

    def __init__(self, Population: int=100, Taxation: int=0.1, LaborRate: float=0.3, Productivity: bool=False, Consume: bool=False, **kwargs: dict()):

        """
        By kwarg, Include additional attributes of Player
        :type kwargs: dict()
        """
        self.Players = list()
        self.attr = kwargs
        self.Productivity = Productivity
        self.Consume = Consume
        
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

        if LaborRate is not None:
            self.BizCandidate = list(np.random.randint(self.Population, size=int(self.Population * LaborRate)))

    def DeployPlayers(self, **kwargs):

        for i in range(self.Population):
            each = {}

            if self.Productivity:
                each.update(dict(Productivity=np.random.random()))
            if self.Consume:
                each.update(dict(Consume=np.random.random()))
            if i in self.BizCandidate:
                each.update(dict(isLabor=False))
                each.update(dict(BizIncome=np.random.random()))
            else:
                each.update({'isLabor': False})
                each.update(dict(EarnedIncome=np.random.random()))

            self.attr = {
                'isLabor': np.random.random(),
                'EarnedIncome': np.random.random(),
                'Productivity': np.random.random(),
                'ConsumeRate': np.random.random()
            }

            PlayerData = Player(str(i), each, **kwargs)
            self.Players.append(PlayerData.__dict__)

    def StartOperation(self, n):
        pass

    def GetData(self):
        return self.__dict__


if __name__ == '__main__':
    s = System()
