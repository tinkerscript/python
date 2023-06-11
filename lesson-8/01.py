class Date:
    value = None

    def __init__(self, date):
        self.value = date

    @classmethod
    def parse(cls, date):
        return date.value.split('-')

    @staticmethod
    def validate(date):
        result = True

        try:
            date, month, year = [int(fragment) for fragment in date.value.split('-')]

            if month < 1 or month > 12:
                result = False
        except TypeError as e:
            result = False

        return result


x = Date('19-01-2020')

print(Date.parse(x))
print(Date.validate(x))

y = Date('19-25-2020')

print(Date.validate(y))
