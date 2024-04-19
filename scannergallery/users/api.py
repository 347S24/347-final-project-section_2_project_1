from ninja import NinjaAPI
import requests

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    #  const searchResponse =
    #     await fetch(config.apiEndpoint + '/v1/mediaItems:search', {
    #       method: 'post',
    #       headers: {
    #         'Content-Type': 'application/json',
    #         'Authorization': 'Bearer ' + authToken
    #       },
    #       body: JSON.stringify(parameters)
    #     });
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token
          }
    
    # request.user is the currently loggedin user
    print('request.user.socialaccount_set')
    print(request.user.socialaccount_set.all())
    print(request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token)
    # request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token


    r = requests.post('https://photoslibrary.googleapis.com/v1/mediaItems:search', headers=headers)
    return r.json()
@api.get("/hello_upload")
def hello_upload(request):
    #  const searchResponse =
    #     await fetch(config.apiEndpoint + '/v1/mediaItems:search', {
    #       method: 'post',
    #       headers: {
    #         'Content-Type': 'application/json',
    #         'Authorization': 'Bearer ' + authToken
    #       },
    #       body: JSON.stringify(parameters)
    #     });
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token
          }
    
    # request.user is the currently loggedin user
    print('request.user.socialaccount_set')
    print(request.user.socialaccount_set.all())
    print(request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token)
    # request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token
    # read image from file
    with open("/home/pinkstacs/347-final-project-section_2_project_1/scannergallery/users/Picture1.png", "rb") as f:
        image_contents = f.read()

    # upload photo and get upload token
    response = requests.post(
        "https://photoslibrary.googleapis.com/v1/uploads", 
        headers=headers,
        data=image_contents)
    upload_token = response.text
    response2 = requests.post(
        'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate', 
        headers = headers,
        json={
            "newMediaItems": [{
                "description": "Test photo",
                "simpleMediaItem": {
                    "uploadToken": upload_token,
                    "fileName": "test.jpg"
                }
            }]
        }
    )
    print(response.text)