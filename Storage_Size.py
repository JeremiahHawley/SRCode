import math


def SR_CODE_SIZE(File_Size, Block_Size, Number_of_Colors):
  return Block_Size * int(
      math.ceil(math.sqrt(math.log(File_Size, Number_of_Colors))))


def SR_STORAGE_SIZE(Image_Size, Block_Size, Number_of_Colors):
  Number_of_Blocks = (Image_Size / Block_Size)**2
  return Number_of_Colors**Number_of_Blocks