from collections import namedtuple


class Month(object):
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales


def create_months():  # function that creates months
    created_months = []
    for month_name in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                       'november', "december"]:  # insert month in months
        build_month = Month(month_name, float(0))
        created_months.append(build_month)
    return created_months  # return the list of months


def record_data(months):  # function that records sales
    while True:
        while True:
            sale_value = float(input("Sale value: USD"))
            month_name = input("Month of sale: ").lower()
            for each_month in months:
                if month_name == each_month.name:
                    print(f"\nSuccessful.")
                    each_month.sales += sale_value
                    print(f"Addicted: USD{each_month.sales:.2f} in {each_month.name} month")
                    break
                else:
                    if months.index(each_month) == 11:
                        print("\nInvalid month. Try again!")
                        break
            break
        if input("Continue? (y/anything else): ").lower() != 'y':
            break


def show_sales(months):  # function that show months and sales in console
    for month in months:
        print(f"\n{month.name.capitalize()}")
        print(f"-> Sales: USD{month.sales:.2f}")
    print("Thanks for using!")


months = create_months()
record_data(months)
show_sales(months)
