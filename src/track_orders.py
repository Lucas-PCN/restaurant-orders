from src.analyze_log import (
    find_most_ordered_dish,
    which_dishes_never_ordered,
    which_days_never_visited,
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return find_most_ordered_dish(customer, self.orders)

    def get_never_ordered_per_customer(self, customer):
        return which_dishes_never_ordered(customer, self.orders)

    def get_days_never_visited_per_customer(self, customer):
        return which_days_never_visited(customer, self.orders)

    def get_busiest_day(self):
        days_count = dict()

        for _, _, day in self.orders:
            if day in days_count:
                days_count[day] += 1
            else:
                days_count[day] = 1

        return max(days_count, key=days_count.get)

    def get_least_busy_day(self):
        days_count = dict()

        for _, _, day in self.orders:
            if day in days_count:
                days_count[day] += 1
            else:
                days_count[day] = 1
        return min(days_count, key=days_count.get)
