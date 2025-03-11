# Task 2: Demonstrate List Slicing

def demonstrate_list_slicing():
    # Original list of numbers from 1 to 10
    original_list = list(range(1, 11))

    # Extract the first five elements
    extracted_list = original_list[:5]

    # Reverse the extracted elements
    reversed_list = extracted_list[::-1]

    # Print the results
    print("Original list:", original_list)
    print("Extracted first five elements:", extracted_list)
    print("Reversed extracted elements:", reversed_list)

# Main program
if __name__ == "__main__":
    demonstrate_list_slicing()