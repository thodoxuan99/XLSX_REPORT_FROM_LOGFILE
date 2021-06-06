import re
import json
line = "asd{\"STT\":6,\"TIME\":100}asd"
z = re.search("{\"STT\":\d+[,]\"TIME\":\d+}", line)
print(z.group())