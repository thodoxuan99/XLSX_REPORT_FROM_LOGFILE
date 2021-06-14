import re
import json
line = "asd{\"STT\":6,\"TIME\":1.02}asd"
z = re.search("{\"STT\":\d+[,]\"TIME\":\d+[.]\d+}", line)
print(z.group())