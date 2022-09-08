from flask import Flask, jsonify, request,  Response
import json
app =   Flask(__name__)
  

# Api lấy danh sách các bài viết theo các điều kiện tìm kiếm
@app.route('/mentions/detail', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        Authorization = request.args.get('keyword_necessary')
        keyword_necessary = request.args.get('keyword_necessary')
        keyword_required = request.args.get('keyword_required')
        keyword_excluded = request.args.get('keyword_excluded')
        sources = request.args.get('sources')
        limit = request.args.get('limit')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')


        data = {
            "status": True,
            "keyword_necessary": keyword_necessary,
            "keyword_required": keyword_required,
            "keyword_excluded": keyword_excluded,
            "data_count": 59080,
            "data": [
                {
                    "title":  "abcdxyz",
                    "sentiment_type": 1,
                    'influencer_score': 5,
                    "url": "https://abc.com/xyz",
                    "view": 100,
                    "content": "abcxyzabcxyzabcxyz",
                    "post_date": "2022-09-04 06:32:00",
                    "source": 1
                },
                {
                    "title":  "abcdxyz",
                    "sentiment_type": 1,
                    'influencer_score': 5,
                    "url": "https://abc.com/xyz",
                    "view": 100,
                    "content": "abcxyzabcxyzabcxyz",
                    "post_date": "2022-09-04 06:32:00",
                    "source": 1
                }
            ],
            "create_at": "2022-09-05 10:10:00",
            "update_at": "2022-09-05 10:10:00"
        }
        return jsonify(data)
  

app.config['PROPAGATE_EXCEPTIONS'] = True

#register 500 error handler
@app.errorhandler(Exception)
# handle all other exception
def all_exception_handler(error):
    res = {"error": str(error)}
    return Response(status=500, mimetype="application/json", response=json.dumps(res))


# handle 401 exception
def error_401_handler(error):
    res = {"errorCode":"Unauthorized", "message":"Not Authenticated"}
    return Response(status=401, mimetype="application/json", response=json.dumps(res))

# handle 403 exception
def error_403_handler(error):
    res = {"errorCode":"AccessDenied", "message":"You don't have access."}
    return Response(status=403, mimetype="application/json", response=json.dumps(res))

# handle 500 exception
def error_500_handler(error):
    res = {"errorCode":"InternalError", "message":"An internal error has occurred. Please try again."}
    return Response(status=500, mimetype="application/json", response=json.dumps(res))


# register error handler
app.register_error_handler(401, error_401_handler)
app.register_error_handler(403, error_403_handler)
app.register_error_handler(500, error_500_handler)

if __name__=='__main__':
    app.run(debug=True)