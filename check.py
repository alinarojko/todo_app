import requests

def decode_secret_message(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
        return

    try:
        data = response.json()
    except ValueError:
        print("Error parsing JSON data.")
        return

    max_x = max(item['x'] for item in data) + 1
    max_y = max(item['y'] for item in data) + 1

    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    for item in data:
        x = item['x']
        y = item['y']
        char = item['char']
        grid[y][x] = char

    for row in grid:
        print(''.join(row))


url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
decode_secret_message(url)