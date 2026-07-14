# tuple.py
# Demonstrates tuple creation, indexing, and immutability

colors = ("red", "green", "blue")

print("First color:", colors[0])
print("Second color:", colors[1])
print("Last color:", colors[-1])

# Tuples cannot be modified once created — this raises a TypeError
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error caught:", e)