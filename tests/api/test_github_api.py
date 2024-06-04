import pytest
import requests
import  math

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user ["login"] == "defunkt"

@pytest.mark.api
def test_user_non_exist(github_api):
    r =github_api.get_user("butenkosergii")
    assert r["message"] =="Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r= github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r['items'][0]["name"]

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] !=0


@pytest.mark.emo
def test_get_emojis(github_api):
    r = github_api.get_emojis()
    assert "falafel" in r
    assert (len(r))>1934

@pytest.mark.emo
def test_repo_commit(github_api):
    r= github_api.get_repo_commit("octocat")
    assert "No commit found" in r["message"]
