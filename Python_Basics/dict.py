# part one: Check if a key exists in a dictionary and return its value or None

def check_key(my_dict, key):
    '''Check if a key exists in the dictionary and return its value or None'''
    if key in my_dict:
        # Key exists
        return my_dict[key]
    else:
        # Key does not exist
        return None
    
if __name__ == "__main__":
    # Example usage
    my_dict = {'name': 'Alice'}
    # Check for a key that exists
    Key_value = check_key(my_dict, 'name1')
    print(f"Part one - Value for key 'name1' in my_dict : {Key_value}")
    
    #Part two
    # Using setdefault to get the value of a key or set it to a default if it doesn't exist
    x = my_dict.setdefault('name1', 'Unknown')
    print("Part two - Default key value is set to :", x)
    