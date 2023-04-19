def calculate_force(m1, m2, distance):
    """Calculates the gravitational force between two objects."""
    G = 6.67430 * 10**-11
    return G * ((m1 * m2) / distance**2)

def main():
    print("Welcome to Gravity Calculator!")
    m1 = float(input("Enter mass of first object (in kg): "))
    m2 = float(input("Enter mass of second object (in kg): "))
    distance = float(input("Enter distance between the objects (in meters): "))
    force = calculate_force(m1, m2, distance)
    print(f"\nThe gravitational force between the objects is {force} N.")

if __name__ == "__main__":
    main()
