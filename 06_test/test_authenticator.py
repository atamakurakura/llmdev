import pytest
from authenticator import Authenticator

def test_register_new_user():
    authn = Authenticator()
    authn.register("username1", "password1")
    assert "username1" in authn.users

def test_register_duplicated_user():
    authn = Authenticator()
    authn.register("username2", "password2")
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authn.register("username2", "another_password2")

def test_login_correct_password():
    authn = Authenticator()
    authn.register("username3", "password3")
    authn.login("username3", "password3")

def test_login_wrong_password():
    authn = Authenticator()
    authn.register("username4", "password4")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authn.login("username4", "wrong_password4")
