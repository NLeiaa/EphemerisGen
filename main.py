import EphemerisGen_year
import EphemerisGen_month

def main():
    print(r'''
/*
 *      ______       _                              _      _____            
 *     |  ____|     | |                            (_)    / ____|           
 *     | |__   _ __ | |__   ___ _ __ ___   ___ _ __ _ ___| |  __  ___ _ __  
 *     |  __| | '_ \| '_ \ / _ \ '_ ` _ \ / _ \ '__| / __| | |_ |/ _ \ '_ \ 
 *     | |____| |_) | | | |  __/ | | | | |  __/ |  | \__ \ |__| |  __/ | | |
 *     |______| .__/|_| |_|\___|_| |_| |_|\___|_|  |_|___/\_____|\___|_| |_|
 *            | |                                                           
 *            |_|                                                           
 *                                                               
 *              Astrological Ephemeris Generator · v1.0 🌌
 */   ''')
    print("=" * 50)
    print("🌌 Welcome to EphemerisGen")
    print("👤 Author: NLeiaa")
    print("🔗 GitHub: https://github.com/NLeiaa")
    print("=" * 50)

    while True:
        option = input("\nConsult ephemeris by year or month? (y/m): ").strip().lower()

        if option == "y":
            EphemerisGen_year.consult()
        elif option == "m":
            EphemerisGen_month.consult()
        else:
            print("❌ Please choose a valid option: 'y' or 'm'.")
            continue

        again = input("\n🔁 Do you want to perform another consultation? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Goodbye! Clear skies!")
            break

if __name__ == "__main__":
    main()
