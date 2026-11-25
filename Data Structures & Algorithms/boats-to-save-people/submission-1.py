class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sort_people = sorted(people)

        light_weight = 0
        high_weight = len(people) - 1
        boats = 0

        while light_weight <= high_weight:

            if sort_people[light_weight] + sort_people[high_weight] <= limit:
                light_weight += 1
                high_weight -= 1

            else:
                high_weight -= 1

            boats += 1

        return boats