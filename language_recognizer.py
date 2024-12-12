import time
import sys

def recognize_strings_equal(s1, s2):
    """ Simulates recognizer for string equality"""
    compare = [f"Comparing '{s1}' with '{s2}'"]
    
    if s1 == s2:
        compare.append("ACCEPT: Strings Match!")
        return "accept", compare
        
    compare.append("LOOP: Strings Are Different.")
    return "loop", compare

def recognize_strings_unequal(s1, s2):
    """Simulates recognizer for string inequality"""
    compare = [f"Comparing '{s1}' with '{s2}'"]
    
    if s1 != s2:
        compare.append("ACCEPT: Strings are Different!")
        return "accept", compare
        
    compare.append("LOOP: Strings Match.")
    return "loop", compare

print("Recognizable vs Co-Recognizable Languages:")
print("-" * 40)

with open(sys.argv[1]) as f:
    for i, line in enumerate(f,1):
        s1, s2 = line.strip().split()
        start = time.time()
        
        print(f"\nTest Case {i}: '{s1}' vs '{s2}'")
        
        # Test equality recognizer
        result, compare = recognize_strings_equal(s1, s2)
        print("\nEquality recognizer:")
        for step in compare:
            print(f"  {step}")
        print(f"Result: {result}")
        
        # Test inequality recognizer
        result, compare = recognize_strings_unequal(s1, s2)
        print("\nInequality recognizer:")
        for step in compare:
            print(f"  {step}")
        print(f"Result: {result}")
        
        total_time = time.time() - start
        print(f"\nTime: {total_time:.4f} seconds")
        print("-" * 40)

