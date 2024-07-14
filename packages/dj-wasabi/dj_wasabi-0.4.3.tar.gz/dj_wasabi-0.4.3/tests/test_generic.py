"""File containing tests specific for the djWasabi/generic.py file."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_generic_debugLog(capsys):
    djWasabi.generic.debugLog(debug=True, message="We will create a release")
    captured = capsys.readouterr()
    assert captured.out == "We will create a release\n"


def test_generic_debugLog_no_debug(capsys):
    djWasabi.generic.debugLog(debug=False, message="We will create a release")
    captured = capsys.readouterr()
    assert not captured.out


def test_keysExitsInDict():
    """Test keysExistInDict with providing a dict and check them
    :return:
    """
    data = {
        "key1": {
            "key2": {
                "key3": "Not my problem",
                "key4": "This is some value we do not care about"
            }
        }
    }

    assert djWasabi.generic.keysExistInDict(data, "key1")
    assert not djWasabi.generic.keysExistInDict(data, "key1", "key3")
    assert djWasabi.generic.keysExistInDict(data, "key1", "key2")
    assert djWasabi.generic.keysExistInDict(data, "key1", "key2", "key4")
    assert not djWasabi.generic.keysExistInDict(data, "key1", "key2", "key3", "key4")


def test_keysExistInDict_with_string():
    """Test keysExistInDict with providing a string.
    :return:
    """
    data = "String"
    with pytest.raises(ValueError, match="We expects dict as first argument."):
        djWasabi.generic.keysExistInDict(data, "key1")


def test_keysExistInDict_with_list():
    """Test keysExistInDict with providing a list.
    :return:
    """
    data = ["String"]
    with pytest.raises(ValueError, match="We expects dict as first argument."):
        djWasabi.generic.keysExistInDict(data, "key1")


def test_keysExistInDict_with_empty_dict():
    """Test keysExistInDict without providing keys.
    :return:
    """
    data = {}
    with pytest.raises(ValueError, match="We expects at least two arguments, one given."):
        djWasabi.generic.keysExistInDict(data)


def test_generic_getRepoUrl():
    """Test the getRepoUrl function.
    """
    getRepoUrl = djWasabi.generic.getRepoUrl(owner="dj-wasabi", repository="dj-wasabi-release")
    assert getRepoUrl == "git@github.com:dj-wasabi/dj-wasabi-release.git"


def test_generic_getRepoUrl_no_owner():
    """Test the getRepoUrl function without providing owner.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the owner of the repository."):
        djWasabi.generic.getRepoUrl(repository="dj-wasabi-release")


def test_generic_getRepoUrl_no_repository():
    """Test the getRepoUrl function without providing repository.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the name of the repository."):
        djWasabi.generic.getRepoUrl(owner="dj-wasabi")


def test_generic_githubUrl():
    """Test the githubUrl function.
    """
    githubUrl = djWasabi.generic.getGithubUrl(owner="dj-wasabi", repository="dj-wasabi-release")
    assert githubUrl == "https://api.github.com/repos/dj-wasabi/dj-wasabi-release"


def test_generic_githubUrl_no_owner():
    """Test the githubUrl function without providing owner.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the owner of the repository."):
        djWasabi.generic.getGithubUrl(repository="dj-wasabi-release")


def test_generic_githubUrl_no_repository():
    """Test the githubUrl function without providing repository.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the name of the repository."):
        djWasabi.generic.getGithubUrl(owner="dj-wasabi")


def test_generic_getString():
    """Test the function to get a string from a string
    :return:
    """
    myString = "mystringhere"
    output = djWasabi.generic.getString(data=myString)
    assert output == "mystringhere"


def test_generic_getString_list():
    """Test the function to get a string from a list
    :return:
    """
    myList = ["my", "string", "here"]
    output = djWasabi.generic.getString(data=myList)
    assert output == "my string here"


def test_generic_getString_list_separator():
    """Test the function to get a string from a list
    :return:
    """
    myList = ["my", "string", "here"]
    output = djWasabi.generic.getString(data=myList, separater=",")
    assert output == "my,string,here"


def test_generic_executeCommand():
    """Test the to execute command to do an ls
    :return:
    """
    command = ["ls", "CHANGELOG.md"]
    output = djWasabi.generic.executeCommand(command=command)
    assert output == "CHANGELOG.md"


def test_generic_executeCommand_no_command():
    """Test the execute command without argument.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the command we want to execute."):
        djWasabi.generic.executeCommand()


def test_generic_compareDictsInLists():
    list1 = [
        {
            "key": "pizza",
            "name": "value"
        }
    ]
    list2 = [
        {
            "name": "value"
        }
    ]
    output = djWasabi.generic.compareDictsInLists(source1=list1, source2=list2)
    assert output == [{'key': 'pizza', 'name': 'value'}]
