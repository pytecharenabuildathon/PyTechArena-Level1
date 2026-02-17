def organize_scores(scores: list[int], descending: bool) -> list[int]:
    return sorted(scores, reverse=descending)
scores = list(map(int, input("Enter scores separated by space: ").split()))
order = input("Sort in descending order? (yes/no): ").strip().lower()
descending = True if order == "yes" else False
sorted_scores = organize_scores(scores, descending)
print("Original list:", scores)
print("Sorted list:", sorted_scores)
