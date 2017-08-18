# import numpy as np

# 시스템의 변수들을 정의한다
# 플레이어들의 변수를 정의한다
# 각 반복마다 영향을 주는 변수를 정의한다
# 각 반복마다 변수들이 어떤 영향을 주고 받는지 정의한다


class Players:
    """
    `attributeOfPlayers` 변수가 1차원 이상인 경우 다음의 변수들을 선택하여 할당한다.
    1) id: Player 구분값
    2) 잔고: 남아있는 재산값(Account), 종속변수, Save = Income - Tax - consumption
    3) 수입: 매회 벌어들이는 재산값, 독립변수 통제가능, 생산성으로 통제한다.
    4) 근로소득 외: Player 중 일부는 재산이 일정 수준 이상이 되면 재산소득(이자, 지대 등)을 얻는다
    5) 사업소득: Player 중 일부는 사업소득을 받는다.
    """

    def __init__(self, _ID, \
                 isLabor=True, \
                 Productivity = 0.5, \
                 EarnedIncome = 0.5, \
                 Bizincome = 0.5, \
                 Consume = 0.5, \
                 TaxRate = 0.1):

        self._ID = _ID
        self.Productivity = Productivity
        self.isLabor = isLabor
        if self.isLabor == False or self.isLabor == 0:
            self.BizIncome = Bizincome
        self.EarnedIncome = EarnedIncome
        self.TotalIncome = self.EarnedIncome + self.BizIncome
        self.Account = self.TotalIncome * (1 - TaxRate) - Consume


class System:
    """
    1) Player의 수입 PLayers.Income 에서 차감하는 비율 System.Taxation을 정한다.
    2) System.Taxtion에 따라 가처분소득 Player.DisposableIncome 을 계산한다.
    """

    def __init__(self, Population, Taxation):
        try:
            if type(self.Population) != int:
                raise isInteger()
            self.Population = Population
        except Exception as Err:
            print(Err)

        try:
            if Taxation <= 0 or Taxation >= 1:
                raise isRate()
            self.Taxation = Taxation
        except Exception as Err:
            print(Err)

    def setup(self, pop=100, taxation=0.1):
        pass


class isInteger(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be An Integer."

    def __str__(self):
        return self.val


class isRate(Exception):

    def __init__(self):
        self.val = "[Setting Error]: This Value Must Be An Integer."

    def __str__(self):
        return self.val


Sys1 = System(0.1, 1)   # Raise Error
Sys2 = System(10, 0.1)  # No Errors