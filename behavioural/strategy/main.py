from strategy import *


def main():
    class Order:
        def __init__(self, weight: float, dist: float):
            self.weight = weight
            self.dist = dist

    order = Order(weight=10, dist=50)

    flat_rate_strategy = FlatRateShipping(rate=15.0)
    weight_based_strategy = WeightBasedShipping(rate_per_kg=2.0)
    distance_based_strategy = DistanceBasedShipping(rate_per_km=0.5)


    print("Flat Rate Shipping")
    shipping_service = ShippingCostService(strategy=flat_rate_strategy)
    cost = shipping_service.calculate_shipping(order)
    print(f"Total Shipping Cost: {cost}\n")

    print("Weight Based Shipping")
    shipping_service.set_strategy(weight_based_strategy)
    cost = shipping_service.calculate_shipping(order)
    print(f"Total Shipping Cost: {cost}\n")


    print("Distance Based Shipping")
    shipping_service.set_strategy(distance_based_strategy)
    cost = shipping_service.calculate_shipping(order)
    print(f"Total Shipping Cost: {cost}\n")


if __name__ == "__main__":
    main()