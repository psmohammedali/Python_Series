import requests  # to get image from the web
import shutil  # to save it locally
import os


def working_function(url, path):
    filename = path + "/" + url.split("/")[-1]

    r = requests.get(url, stream=True)
    print(r)
    if r.status_code == 200:

        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image successfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retrieved')


path = "../../convocation_photos"
basic_url = "http://info.vit.ac.in/37thconvocation/DAY2/SITE/photos/DSCF"
start = 3294
end = 4634
for i in range(start, end + 1, 1):
    current_url = basic_url + str(i) + ".JPG"
    working_function(current_url, path)
