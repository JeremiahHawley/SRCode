from PIL import Image


def create_SR_Code(Filepath, outpath):
  with open(Filepath, 'r') as file:
    rgb_values = file.read().strip().split('\n')

  rgb_data = []
  for row in rgb_values:
    row_values = []
    for value_str in row.split('),'):
      value_str = value_str.strip('()')
      values = value_str.split(',')
      if len(values) == 3:
        r, g, b = [int(x) for x in values]
        row_values.append((r, g, b))
    rgb_data.append(row_values)

  print(rgb_data)

  # Create a new image from the RGB data
  width = len(rgb_data[0])
  height = len(rgb_data)
  image = Image.new("RGB", (width, height))

  # Set the pixel values of the image
  for y in range(height):
    for x in range(width):
      image.putpixel((x, y), rgb_data[y][x])
  image.save(outpath)

create_SR_Code("test_toimg.txt", "test.png")


