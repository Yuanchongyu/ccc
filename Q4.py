import sys

def max_consecutive_sunshine():
    N = int(sys.stdin.readline().strip())
    weather_data = []
    for _ in range(N):
        weather_data.append(sys.stdin.readline().strip())
    max_sun = 0
    max_possible_sun = 0
    current_sun = 0
    prev_sun_lengths = []
    
    for day in weather_data:
        if day == "S":
            current_sun += 1
        else:
            max_sun = max(max_sun, current_sun)
            prev_sun_lengths.append(current_sun)
            current_sun = 0

    max_sun = max(max_sun, current_sun)
    prev_sun_lengths.append(current_sun)
    print(max_sun)
    print(prev_sun_lengths)
    if "P" in weather_data:
        for i in range(len(prev_sun_lengths) - 1):
            max_possible_sun = max(max_possible_sun, prev_sun_lengths[i] + 1 + prev_sun_lengths[i + 1])

    print(max(max_sun, max_possible_sun))


if __name__ == "__main__":
    max_consecutive_sunshine()
