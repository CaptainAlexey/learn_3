import ephem
import datetime

user_text = "Mars"
date = datetime.date.today()
date = str(date)
planet = getattr(ephem, user_text)
planet_now = planet(date)
constel = ephem.constellation(planet_now)
print(constel)