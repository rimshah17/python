class TimeConverter:
    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_seconds(self, minutes):
        return minutes * 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def hours_to_minutes(self, hours):
        return hours * 60

    def hours_to_days(self, hours):
        return hours / 24

    def days_to_hours(self, days):
        return days * 24

    def convert(self, value, from_unit, to_unit):
        if from_unit == "Seconds" and to_unit == "Minutes":
            return self.seconds_to_minutes(value)
        elif from_unit == "Minutes" and to_unit == "Seconds":
            return self.minutes_to_seconds(value)
        elif from_unit == "Minutes" and to_unit == "Hours":
            return self.minutes_to_hours(value)
        elif from_unit == "Hours" and to_unit == "Minutes":
            return self.hours_to_minutes(value)
        elif from_unit == "Hours" and to_unit == "Days":
            return self.hours_to_days(value)
        elif from_unit == "Days" and to_unit == "Hours":
            return self.days_to_hours(value)
        elif from_unit == "Seconds" and to_unit == "Hours":
            return self.seconds_to_minutes(self.minutes_to_hours(value))
        elif from_unit == "Hours" and to_unit == "Seconds":
            return self.hours_to_minutes(self.minutes_to_seconds(value))
        elif from_unit == "Seconds" and to_unit == "Days":
            return self.seconds_to_minutes(self.minutes_to_hours(self.hours_to_days(value)))
        elif from_unit == "Days" and to_unit == "Seconds":
            return self.days_to_hours(self.hours_to_minutes(self.minutes_to_seconds(value)))
        elif from_unit == "Minutes" and to_unit == "Days":
            return self.minutes_to_hours(self.hours_to_days(value))
        elif from_unit == "Days" and to_unit == "Minutes":
            return self.days_to_hours(self.hours_to_minutes(value))
        else:
            return value  # If the units are the same or conversion is not defined

# Add more conversion functions as needed