import re

text = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
pattern = r'^(https:\/\/)?(www.)?youtube.com\/watch\?v=([\w]+)$'

match = re.search(pattern, text)
if match:
    print("Video youtube")
    print(match.group(3))
else:
    print("Pas une video")