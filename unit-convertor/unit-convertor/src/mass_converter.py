class MassConverter:
    def grams_to_kilograms(self, grams):
        return grams / 1000

    def kilograms_to_grams(self, kilograms):
        return kilograms * 1000

    def grams_to_pounds(self, grams):
        return grams * 0.00220462

    def pounds_to_grams(self, pounds):
        return pounds / 0.00220462

    def kilograms_to_pounds(self, kilograms):
        return kilograms * 2.20462

    def pounds_to_kilograms(self, pounds):
        return pounds / 2.20462

    def convert(self, value, from_unit, to_unit):
        if from_unit == "Grams" and to_unit == "Kilograms":
            return self.grams_to_kilograms(value)
        elif from_unit == "Kilograms" and to_unit == "Grams":
            return self.kilograms_to_grams(value)
        elif from_unit == "Grams" and to_unit == "Pounds":
            return self.grams_to_pounds(value)
        elif from_unit == "Pounds" and to_unit == "Grams":
            return self.pounds_to_grams(value)
        elif from_unit == "Kilograms" and to_unit == "Pounds":
            return self.kilograms_to_pounds(value)
        elif from_unit == "Pounds" and to_unit == "Kilograms":
            return self.pounds_to_kilograms(value)
        else:
            return value  # If the units are the same or conversion is not defined