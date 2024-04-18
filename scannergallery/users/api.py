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