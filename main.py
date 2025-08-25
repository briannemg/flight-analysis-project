from flight_analysis.data_loader import load_flight_data
from flight_analysis.task1 import plot_coach_price_distribution

def main():
    # Load data
    flight = load_flight_data("data/flight.csv")

    # Run Task 1
    plot_coach_price_distribution(flight, benchmark=500)


if __name__ == "__main__":
    main()