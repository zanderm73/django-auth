{"filter":false,"title":"backends.py","tooltip":"/accounts/backends.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":32,"column":0},"end":{"row":32,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"11996628bf9d241cc0faad36e6ccabb00d9f48ae","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":35,"column":23},"action":"insert","lines":["from django.contrib.auth.models import User","","","class EmailAuth:","    \"\"\"Authenticate a user by an exact match on the email and password\"\"\"","","    def authenticate(self, username=None, password=None):","        \"\"\"","        Get an instance of `User` based off the email and verify the","        password","        \"\"\"","","        try:","            user = User.objects.get(email=username)","","            if user.check_password(password):","                return user","","            return None","        except User.DoesNotExist:","            return None","    ","    def get_user(self, user_id):","        \"\"\"","        Used by the Django authentiation system to retrieve a user instance","        \"\"\"","        ","        try:","            user = User.objects.get(pk=user_id)","","            if user.is_active:","                return user","","            return None","        except User.DoesNotExist:","            return None"],"id":1}]]},"timestamp":1568225563029}