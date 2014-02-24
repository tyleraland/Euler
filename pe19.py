class Day:
    day = 1
    month = 1
    year = 1900
    weekday = 1
    def todayis(self):
        print("Day:     " + str(self.day))
        print("Month:   " + str(self.month))
        print("Year:    " + str(self.year))
        print("Weekday: " + str(self.weekday))
        print("\n")

    def inc(self):
        self.weekday = (self.weekday % 7) + 1
        if self.month == 2:
            if (self.year % 4 == 0) and (self.year % 100 > 0 or self.year % 400 == 0):
                self.day = (self.day % 29) + 1
            else:
                self.day = (self.day % 28) + 1
        elif self.month in [4,6,9,11]: # April, June, September, November
            self.day = (self.day % 30) + 1
        else:
            self.day = (self.day % 31) + 1
        if self.day == 1:
            self.month = (self.month % 12) + 1
            if (self.month % 12) == 1:
                self.year += 1
print("!!!!!!!")
cal = Day()
#cal.todayis()
cnt = 0
while cal.year < 2001:
    if cal.year >= 1901 and cal.day == 1 and cal.weekday == 7:
        cnt += 1
        cal.todayis()
    cal.inc()
print(cnt)
