class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        """Add any object to the pouch_contents list."""
        self.pouch_contents.append(item)

    def __str__(self):
        # Return string representation of Kangaroo and its pouch contents
        contents_strings = []
        for item in self.pouch_contents:
            if isinstance(item, Kangaroo):
                # Represent contained Kangaroo by its id or simple label
                contents_strings.append(f"<Kangaroo object at {id(item)}>")
            else:
                contents_strings.append(str(item))
        contents = ', '.join(contents_strings)
        return f"Kangaroo with pouch contents: [{contents}]"

# Test code
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(kanga)  # Should show roo inside kanga's pouch
print(roo)    # Should show empty pouch