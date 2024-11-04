#Function with **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Example usage
print_info(name="Sehar", age="Kiu btaooun?")
# Output:
# name: Sehar