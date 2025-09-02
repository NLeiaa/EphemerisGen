import ephem
import datetime
import math
import json
import csv

# Zodiac abbreviations
ZODIAC = 'AR TA GE CN LE VI LI SC SG CP AQ PI'.split()

def format_zodiacal_longitude(longitude):
    """Format ecliptic longitude as zodiac position (e.g., 15VI24)."""
    l = math.degrees(longitude.norm)
    degrees = int(l % 30)
    sign = ZODIAC[int(l / 30)]
    minutes = int(round((l % 1) * 60))
    return '{:02}{}{:02}'.format(degrees, sign, minutes)

def format_angle_as_time(angle):
    """Convert angle to sidereal time format HH:MM:SS."""
    hours = math.degrees(angle) / 15.0
    h = int(hours)
    m = int((hours % 1) * 60)
    s = int(((hours * 60) % 1) * 60)
    return '{:02}:{:02}:{:02}'.format(h, m, s)

def generate_monthly_ephemeris(year, month, bodies):
    """
    Generate ephemeris data for all days in a given month.
    Returns a list of dictionaries structured for export and printing.
    """
    # Calculate number of days in the given month
    days_in_month = (datetime.date(year + int(month / 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)).day

    month_data = {
        'year': year,
        'month': month,
        'data': []
    }

    for day in range(1, days_in_month + 1):
        date = ephem.Date((year, month, day))
        dt = datetime.datetime(*date.tuple()[:3])
        observer = ephem.Observer()
        observer.date = date
        sidereal = format_angle_as_time(observer.sidereal_time())

        body_positions = []
        for body in bodies:
            body.compute(date)
            pos = format_zodiacal_longitude(ephem.Ecliptic(body).long)
            body_positions.append(pos)

        day_record = {
            'day_of_week': dt.strftime('%A')[:2],
            'day_of_month': f"{day:02}",
            'sidereal_time': sidereal,
            'bodies': body_positions
        }

        month_data['data'].append(day_record)

    return [month_data]

def print_ephemeris_to_terminal(data, body_labels):
    """Display ephemeris data as a formatted table in the terminal."""
    for month_data in data:
        month_name = datetime.date(month_data['year'], month_data['month'], 1).strftime("%B %Y").upper()
        print(f"\n{'-' * 80}")
        print(f"{month_name.center(80)}")
        print(f"{'-' * 80}")
        header = f"{'DATE':<6} {'SID.TIME':<9} " + " ".join([f"{name[:6].upper():>7}" for name in body_labels])
        print(header)
        print('-' * len(header))

        for day_data in month_data['data']:
            row = f"{day_data['day_of_week']} {day_data['day_of_month']}  {day_data['sidereal_time']}  "
            row += " ".join([f"{pos:>7}" for pos in day_data['bodies']])
            print(row)
        print('-' * len(header))

def export_to_json(data, bodies, filename="ephemeris.json"):
    """Export ephemeris data to a JSON file."""
    header = ['DATE', 'SID.TIME'] + [body.name[:6].upper() for body in bodies]
    json_output = {}

    for month_data in data:
        month_name = datetime.date(month_data['year'], month_data['month'], 1).strftime("%B %Y").upper()
        monthly_list = []

        for day_data in month_data['data']:
            row_dict = {
                'DATE': f"{day_data['day_of_week']} {day_data['day_of_month']}",
                'SID.TIME': day_data['sidereal_time']
            }
            for i, body_name in enumerate(header[2:]):
                row_dict[body_name] = day_data['bodies'][i]
            monthly_list.append(row_dict)

        json_output[month_name] = monthly_list

    with open(filename, 'w') as json_file:
        json.dump(json_output, json_file, indent=4)
    print(f"\n✅ JSON export complete: {filename}")

def export_to_csv(data, bodies, filename="ephemeris.csv"):
    """Export ephemeris data to a CSV file."""
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

    print(f"✅ CSV export complete: {filename}")

def consult():
    try:
        # Input
        month = int(input('Month (1-12): '))
        year = int(input('Year (e.g., 2025): '))
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
    except ValueError as e:
        print(f"❌ Invalid input: {e}")
        return

    planet_names = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars',
                    'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    planet_bodies = [ephem.Sun(), ephem.Moon(), ephem.Mercury(), ephem.Venus(), ephem.Mars(),
                     ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(), ephem.Neptune(), ephem.Pluto()]

    ephemeris_data = generate_monthly_ephemeris(year, month, planet_bodies)

    print_ephemeris_to_terminal(ephemeris_data, planet_names)

    export_choice = input("Export data? (y/n): ").strip().lower()
    if export_choice == 'y':
        filetype = input("Format (csv/json): ").strip().lower()
        if filetype == 'csv':
            export_to_csv(ephemeris_data, planet_bodies)
        elif filetype == 'json':
            export_to_json(ephemeris_data, planet_bodies)
        else:
            print("❌ Invalid format. Skipping export.")


# -------- Main Program --------
if __name__ == '__main__':
    consult()