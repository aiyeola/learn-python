import converter
#  or
from converter import lbs_to_kg, find_max

numbers = [10, 13, 2]
max = find_max(numbers)
print(max)

ans = converter.kg_to_lbs(22.5)
print(ans)

ann = lbs_to_kg(50)
print(ann)
