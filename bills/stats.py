# Write your imports here



class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        # Write here your code
        counter = defaultdict(int)

        for bill in self.bills:
            for product in bill.products:
                counter[product] += 1

        if not counter:
            return None

        product = max(counter, key=counter.get)
        return product, counter[product]

    def find_top_two_sellers(self) -> list:
        # Write here your code
        totals = defaultdict(float)

        for bill in self.bills:
            totals[bill.seller] += bill.calculate_total()

        sorted_sellers = sorted(totals.items(),
                                key=lambda x: x[1],
                                reverse=True)

        return [s[0] for s in sorted_sellers[:2]]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
        totals = defaultdict(float)

        for bill in self.bills:
            totals[bill.buyer] += bill.calculate_total()

        buyer = min(totals, key=totals.get)
        return buyer, totals[buyer]

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        for bill in self.bills:
            for product in bill.products:
                tuples.append((product, product.calculate_total_taxes()))

        reverse = order_type == OrderType.DESC

        tuples.sort(key=lambda x: x[1], reverse=reverse)

        return tuples

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
