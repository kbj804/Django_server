# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    #'http':search_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

'''
위의 root routing configuration 파일은 클라이언트와 Channels 개발 서버와 연결이 맺어질 때, ProtocolTypeRouter를 가장 먼저 조사하여 어떤 타입의 연결인지 구분합니다.
만약에 WebSocket 연결이라면, 이 연결은 AuthMiddlewareStack으로 이어집니다.

AuthMiddlewareStack은 현재 인증된 사용자에 대한 참조로 scope를 결정합니다. ( scope는 나중에 다루도록 하겠습니다. )
이는 Django에서 현재 인증된 사용자의 view 함수에서 request 요청을 결정하는 AuthenticationMiddleware와 유사한 방식이며, 그 결과 URLRouter로 연결됩니다.

URLRouter는 작성한 url 패턴을 기반으로, 특정 소비자의 라우트 연결 HTTP path를 조사합니다.
'''
