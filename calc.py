class HousingBenefit:
    """ Class used to calculate the housing benefit (Wohngeld) for Germany.
    """

    def __init__(self, rent, considered_house_members, income, rent_level):
        self.considered_house_members = considered_house_members
        self.rent_level = rent_level
        self.income = self.get_accountable_monthly_income(income)
        self.rent = self.get_maximum_rent(rent)+self.get_heating_costs()

    def get_maximum_rent(self, rent):
        # calculates maximum accountable rent by given rent, housing members
        # and rent level of current location
        if self.considered_house_members == 1:
            if self.rent_level == 1:
                return 338 if rent > 338 else rent
            if self.rent_level == 2:
                return 381 if rent > 381 else rent
            if self.rent_level == 3:
                return 426 if rent > 426 else rent
            if self.rent_level == 4:
                return 478 if rent > 478 else rent
            if self.rent_level == 5:
                return 525 if rent > 525 else rent
            if self.rent_level == 6:
                return 575 if rent > 575 else rent
            if self.rent_level == 7:
                return 633 if rent > 633 else rent
        if self.considered_house_members == 2:
            if self.rent_level == 1:
                return 409 if rent > 409 else rent
            if self.rent_level == 2:
                return 461 if rent > 461 else rent
            if self.rent_level == 3:
                return 516 if rent > 516 else rent
            if self.rent_level == 4:
                return 579 if rent > 579 else rent
            if self.rent_level == 5:
                return 636 if rent > 636 else rent
            if self.rent_level == 6:
                return 697 if rent > 697 else rent
            if self.rent_level == 7:
                return 767 if rent > 767 else rent
        # MAYBE(pierre): add for 3,4,5 etc house members.

    def get_heating_costs(self):
        # returns specific heating costs for the considered house member count
        # source: https://www.sozialgesetzbuch-sgb.de/wogg/12.html
        if self.considered_house_members == 1:
            return 14.40
        if self.considered_house_members == 2:
            return 18.60
        # MAYBE(pierre): add for 3,4,5 etc house members.

    def get_housing_benefit_constants(self):
        # returns constants required for calculating the benefit amount.
        # constants depend on housing_level
        # source: https://www.sozialgesetzbuch-sgb.de/wogg/anlage-2.html
        a, b, c = 0, 0, 0
        if self.considered_house_members == 1:
            a = 4
            b = 5.8
            c = 1.18
        if self.considered_house_members == 2:
            a = 3
            b = 4.05
            c = 8.8
        # MAYBE(pierre): add for 3,4,5 etc house members.
        return [a * 10 ** - 2, b * 10 ** - 4, c * 10 ** -4]

    def get_accountable_monthly_income(self, monthly_brutto):
        # returns accountable monthyl income. Housing benefit is calculated
        # with neither brutto nor netto income. It's mostly 90% of brutto
        # income.
        # source: https://www.sozialgesetzbuch-sgb.de/wogg/16.html
        return monthly_brutto * 9 / 10

    def get_monthly_housing_benefit(self):
        # returns expected monthly housing beneftig value in euro
        constants = self.get_housing_benefit_constants()
        cost = 1.15 * (self.rent - (constants[0] + constants[1] * self.rent
                       + constants[2] * self.income) * self.income)
        return round(cost, 2)


if __name__ == '__main__':
    # logic source: https://www.sozialgesetzbuch-sgb.de/wogg/1.html

    # ADAPT THESE FOUR VALUES TO MATCH YOUR OWN.
    rent = 400
    considered_house_members = 1
    brutto_monthly_income = 600
    rent_level = 4

    # MAYBE(pierre): calc rent_level based on given city.
    # TODO(pierre): write some calc unit tests.
    housing_benefit = HousingBenefit(rent, considered_house_members,
                                     brutto_monthly_income, rent_level)
    print(f"Your monthly rent is {rent}")
    print(f"Amount of considered house members: {considered_house_members}")
    print(f"Brutto monthly income: {brutto_monthly_income}")
    print(f"Rent level for your city: {rent_level}")
    print("Your calculated monthly housing benefit is: " +
          str(housing_benefit.get_monthly_housing_benefit())
          + "€.")
