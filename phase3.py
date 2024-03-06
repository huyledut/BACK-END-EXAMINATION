def num_of_islands(image_of_the_ocean):
    if not image_of_the_ocean:
        return 0

    def checker(longitude, latitude):
        if longitude < 0 or latitude < 0 or longitude >= len(image_of_the_ocean) or latitude >= len(image_of_the_ocean[0]) or image_of_the_ocean[longitude][latitude] == "0":
            return

        image_of_the_ocean[longitude][latitude] = "0"

        checker(longitude + 1, latitude)
        checker(longitude - 1, latitude)
        checker(longitude, latitude + 1)
        checker(longitude, latitude - 1)

    num_islands = 0

    for i in range(len(image_of_the_ocean)):
        for j in range(len(image_of_the_ocean[0])):
            if image_of_the_ocean[i][j] == "1":
                num_islands += 1
                checker(i, j)

    return num_islands


image_of_the_ocean_1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

image_of_the_ocean_2 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["1", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "0"]
]

print(num_of_islands(image_of_the_ocean_1))
print(num_of_islands(image_of_the_ocean_2))