def flatten_generator(nested_list):
    """
    Generator function that yields items from a nested list one by one.
    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item

def main():
    nested = ['a', ['b', ['c', 'd']], 'e']
    flat_list = list(flatten_generator(nested))

    print("Original Nested List:", nested)
    print("Flattened Normal List:", flat_list)

if __name__ == "__main__":
    main()