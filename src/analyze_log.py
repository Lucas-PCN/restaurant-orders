import csv


def open_file(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path}")
    
    try:
        data = []

        with open(path, "rt") as file:
            for row in csv.reader(file):
                data.append(row)
        
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path}")

def find_most_ordered_dish(person_name, orders):
    dishes_amounts = {}

    for customer, dish, _ in orders:
        if customer == person_name:
            if dish in dishes_amounts:
                dishes_amounts[dish] += 1
            else:
                dishes_amounts[dish] = 1

    most_ordered_dish = max(dishes_amounts.items(), key=lambda x: x[1])[0]

    return most_ordered_dish

def how_many_orders(person_name, dish, orders):
    times = {}

    for customer, dish, _ in orders:
        if customer == person_name:
            if dish in times:
                times[dish] += 1
            else:
                times[dish] = 1

    orders_amount = times[dish]

    return orders_amount


def which_dishes_never_ordered(person_name, orders):
    all_dishes = set()
    ordered_by_someone = set()

    for customer, dish, _ in orders:
        all_dishes.add(dish)

    for customer, dish, _ in orders:
        if customer == person_name:
            ordered_by_someone.add(dish)

    return all_dishes - ordered_by_someone


def which_days_never_visited(person_name, orders):
    all_days = set()
    days_visited_by_someone = set()

    for _, _, weekday in orders:
        all_days.add(weekday)

    for customer, _, day in orders:
        if customer == person_name:
            days_visited_by_someone.add(day)

    return all_days - days_visited_by_someone

def analyze_log(path_to_file):
    orders = open_file(path_to_file)
    most_ordered = find_most_ordered_dish("maria", orders)
    times_ordered = how_many_orders("arnaldo", "hamburguer", orders)
    unordered_dishes = which_dishes_never_ordered("joao", orders)
    unvisited_days = which_days_never_visited("joao", orders)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{most_ordered}\n")
        file.write(f"{times_ordered}\n")
        file.write(f"{unordered_dishes}\n")
        file.write(f"{unvisited_days}")
