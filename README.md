# housing benefit (Wohngeld) calculator
- Can be used to calculate the estimated housing benefit you will be granted.
- Most pages used to calculate housing benefit were terribly annoying. Therefore I decided to write this to calculate the possible amounts.
- Based on the WoGG(Wohngeldgesetz) got most from here: https://www.sozialgesetzbuch-sgb.de/wogg/1.html

# prerequisites
- python3 installed

# quickstart
- open calc.py with an editor.
- adapt these four values at the bottom of the calc.py file:
```python
    rent = 400
    considered_house_members = 1
    brutto_monthly_income = 600
    rent_level = 4
```
to match your specific values.
- run calc.py
```python
python3 calc.py
```
- expected output for default values in this script:
```
Your monthly rent is 400
Amount of considered house members: 1
Brutto monthly income: 600
Rent level for your city: 4
Your calculated monthly housing benefit is: 262.89€.
```
