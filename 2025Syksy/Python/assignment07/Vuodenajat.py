kuukaudenVuodenaika = {
    1:"winter",
    2:"winter",
    3:"spring",
    4:"spring",
    5:"spring",
    6:"summer",
    7:"summer",
    8:"summer",
    9:"autumn",
    10:"autumn",
    11:"autumn",
    12:"winter" }
def get_season(kk):
    if 0 < kk < 13:
        print(f"The season is {kuukaudenVuodenaika[kk]}")
    else:
        print("Please enter a number between 1 and 12.")
kuukausi = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {kuukausi}")
get_season(kuukausi)