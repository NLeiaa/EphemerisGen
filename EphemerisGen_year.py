import ephem
import datetime
import itertools
import math
import csv
import json

# Zodiac signs
ZODIAC = 'AR TA GE CN LE VI LI SC SG CP AQ PI'.split()

def format_zodiacal_longitude(longitude):
    """Format ecliptic longitude as zodiacal position (e.g., '00AR00')."""
    l = math.degrees(longitude.norm)
    degrees = int(l % 30)
    sign = ZODIAC[int(l / 30)]
    minutes = int(round((l % 1) * 60))
    return '{:02}{}{:02}'.format(degrees, sign, minutes)

def format_angle_as_time(angle):
    """Format angle as HH:MM:SS (for sidereal time)."""
    hours = math.degrees(angle) / 15.0
    h = int(hours)
    m = int((hours % 1) * 60)
    s = int(((hours * 60) % 1) * 60)
    return '{:02}:{:02}:{:02}'.format(h, m, s)

def get_ephemeris_for_date(date, bodies):
    """Return ephemeris data for a single date."""
    date = ephem.Date(date)
    dt = datetime.datetime(*date.tuple()[:3])
    day_of_week = dt.strftime('%A')[:2]
    day_of_month = f'{dt.day:02}'

    observer = ephem.Observer()
    observer.date = date
    sidereal_time = format_angle_as_time(observer.sidereal_time())

    positions = []
    for body in bodies:
        body.compute(date)
        positions.append(format_zodiacal_longitude(ephem.Ecliptic(body).long))

    return {
        'day_of_week': day_of_week,
        'day_of_month': day_of_month,
        'sidereal_time': sidereal_time,
        'bodies': positions
    }

def print_ephemeris_for_month(year, month, bodies):
    """Print ephemeris data for a specific month."""
    title = datetime.date(year, month, 1).strftime("%B %Y").upper()
    print(f'\n{title.center(14 + len(bodies) * 7)}\n')

    print('DATE  SID.TIME', end=' ')
    for body in bodies:
        print(f'{body.name[:6].upper():<7}', end=' ')
    print()

    month_data = []
    for day in itertools.count(1):
        try:
            datetuple = (year, month, day)
            datetime.date(*datetuple)  # Raises error if invalid
            ephemeris = get_ephemeris_for_date(datetuple, bodies)

            print(f"{ephemeris['day_of_week']} {ephemeris['day_of_month']} {ephemeris['sidereal_time']} ", end='')
            for position in ephemeris['bodies']:
                print(f'{position:<7}', end=' ')
            print()

            month_data.append(ephemeris)
        except ValueError:
            break

    return month_data

def print_ephemeris_for_year(year):
    """Print ephemeris for each month in a given year."""
    bodies = [ephem.Sun(), ephem.Moon(), ephem.Mercury(), ephem.Venus(),
              ephem.Mars(), ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(),
              ephem.Neptune(), ephem.Pluto()]

    year_data = []
    for month in range(1, 13):
        month_data = print_ephemeris_for_month(year, month, bodies)
        year_data.append({'year': year, 'month': month, 'data': month_data})
        print()

    return year_data

def export_to_json(data, bodies, filename="ephemeris.json"):
    """Export ephemeris data to a JSON file, grouped by month."""
    header = ['DATE', 'SID.TIME'] + [body.name[:6].upper() for body in bodies]
    json_output = {}

    for month_data in data:
        month_name = datetime.date(month_data['year'], month_data['month'], 1).strftime("%B %Y").upper()
        monthly_list = []

        for day_data in month_data['data']:
            row = {
                'DATE': f"{day_data['day_of_week']} {day_data['day_of_month']}",
                'SID.TIME': day_data['sidereal_time']
            }
            for i, body_name in enumerate(header[2:]):
                row[body_name] = day_data['bodies'][i]
            monthly_list.append(row)

        json_output[month_name] = monthly_list

    with open(filename, 'w') as json_file:
        json.dump(json_output, json_file, indent=4)

    print(f"\n✅ JSON export completed: {filename}")

def export_to_csv(data, bodies, filename="ephemeris.csv"):
    """Export ephemeris data to CSV file with terminal-style formatting."""
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')

        for month_data in data:
            month_name = datetime.date(month_data['year'], month_data['month'], 1).strftime("%B %Y").upper()
            writer.writerow([f"{month_name.center(50)}"])

            header = ['DATE', 'SID.TIME'] + [body.name[:6].upper() for body in bodies]
            writer.writerow(header)

            for day_data in month_data['data']:
                row = [f"{day_data['day_of_week']} {day_data['day_of_month']}", day_data['sidereal_time']] + day_data['bodies']
                writer.writerow(row)

    print(f"✅ CSV export completed: {filename}")

def consult():
    try:
        year = int(input("Enter year (e.g., 2025): ").strip())
    except ValueError:
        print("❌ Invalid year input.")
        return

    # Planetary bodies
    bodies = [ephem.Sun(), ephem.Moon(), ephem.Mercury(), ephem.Venus(),
              ephem.Mars(), ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(),
              ephem.Neptune(), ephem.Pluto()]

    data = print_ephemeris_for_year(year)

    export_option = input("Export data to JSON or CSV? (Type 'json' or 'csv'): ").strip().lower()
    if export_option == 'json':
        export_to_json(data, bodies)
    elif export_option == 'csv':
        export_to_csv(data, bodies)
    else:
        print("❌ Invalid option. No export performed.")


# -------- Main Program --------
if __name__ == "__main__":
    consult()