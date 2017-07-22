import falcon
import json
import pafy


def serialize_audio_stream(stream):
    result = {
        'bitrate': stream.bitrate,
        'extension': stream.extension,
        'filesize': stream.get_filesize(),
        'stream_url': stream.url,
    }
    return result

class HomeResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('templates/index.html', 'r') as f:
            resp.body = f.read()

class YoutubeResource:
    def on_get(self, req, resp):
        video_id = req.params.get('v', None)
        result = []

        if video_id:
            video_url = "https://www.youtube.com/watch?v={}".format(video_id)
            video = pafy.new(video_url)
            audiostreams = video.audiostreams
            result = {
                'video': {
                    'id': video_id,
                    'thumbnail_url': 'https://img.youtube.com/vi/{}/0.jpg'.format(video_id),
                    'title': video.title,
                    'length': video.length,
                    'duration': video.duration,
                },
                'audio_streams': [serialize_audio_stream(s) for s in audiostreams]
            }

        resp.body = json.dumps(result)
 
api = falcon.API()
api.add_route('/', HomeResource())
api.add_route('/youtube', YoutubeResource())