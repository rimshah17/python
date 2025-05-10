class LengthConverter:
    def meters_to_kilometers(self, meters):
        return meters / 1000

    def kilometers_to_meters(self, kilometers):
        return kilometers * 1000

    def miles_to_feet(self, miles):
        return miles * 5280

    def feet_to_miles(self, feet):
        return feet / 5280

    def convert(self, value, from_unit, to_unit):
        if from_unit == "Meters" and to_unit == "Kilometers":
            return self.meters_to_kilometers(value)
        elif from_unit == "Kilometers" and to_unit == "Meters":
            return self.kilometers_to_meters(value)
        elif from_unit == "Miles" and to_unit == "Feet":
            return self.miles_to_feet(value)
        elif from_unit == "Feet" and to_unit == "Miles":
            return self.feet_to_miles(value)
        else:
            return value  # If the units are the same or conversion is not defined