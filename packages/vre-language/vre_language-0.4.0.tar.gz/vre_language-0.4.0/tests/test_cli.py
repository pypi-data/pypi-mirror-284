"""test the session class"""
import os
import subprocess as sp
import pytest
from fireworks import LaunchPad
from fireworks.fw_config import LAUNCHPAD_LOC


@pytest.fixture(name='model_file')
def model_file_fixture(tmp_path):
    """prepare a model file as a fixture"""
    path = os.path.join(tmp_path, 'model.vm')
    model = "a = 1; print(a)"
    with open(path, 'w', encoding='utf-8') as ifile:
        ifile.write(model)
    return path


@pytest.fixture(name='lpad_file')
def lpad_file_fixture(tmp_path):
    """launchpad file as fixture"""
    lpad = LaunchPad.from_file(LAUNCHPAD_LOC) if LAUNCHPAD_LOC else LaunchPad()
    path = os.path.join(tmp_path, 'launchpad.yaml')
    lpad.to_file(path)
    return path


def test_texts_script_instant(model_file):
    """test texts script cli tool in instant evaluation mode"""
    command = ['texts', 'script', '-f', model_file]
    with sp.Popen(command, stdout=sp.PIPE, shell=False) as proc:
        assert proc.stdout.read().decode() == "program output: >>>\n1\n<<<\n"


def test_texts_script_deferred(model_file):
    """test texts script cli tool in deferred evaluation mode"""
    command = ['texts', 'script', '-f', model_file, '-m', 'deferred']
    with sp.Popen(command, stdout=sp.PIPE, shell=False) as proc:
        assert proc.stdout.read().decode() == "program output: >>>\n1\n<<<\n"


def test_texts_script_workflow(model_file, lpad_file):
    """test texts script cli tool in workflow evaluation mode"""
    command = ['texts', 'script', '-f', model_file, '-m', 'workflow',
               '-l', lpad_file, '-r']
    with sp.Popen(command, stdout=sp.PIPE, shell=False) as proc:
        assert "program output: >>>\n1\n<<<\n" in proc.stdout.read().decode()


def test_texts_session(lpad_file, _res_config_loc):
    """test texts session cli tool"""
    model = "a = 1; print(a)\n%exit"
    command = ['texts', 'session', '-l', lpad_file, '-r']
    with sp.Popen(command, stdout=sp.PIPE, stdin=sp.PIPE, shell=False) as proc:
        stdout = proc.communicate(input=model.encode())[0]
        assert "Output > 1" in stdout.decode()


def test_texts_session_expression(lpad_file, _res_config_loc):
    """test texts session cli tool with expression"""
    model = "a = 1 \n a + 1 \n %exit"
    command = ['texts', 'session', '-l', lpad_file, '-r']
    with sp.Popen(command, stdout=sp.PIPE, stdin=sp.PIPE, shell=False) as proc:
        stdout = proc.communicate(input=model.encode())[0]
        assert "Output > 2" in stdout.decode()


def test_texts_session_magics(lpad_file, _res_config_loc):
    """test texts session cli tool with magics"""
    model = "%uuid \n %sleep \n %new \n %start \n %stop \n %hist \n %vary \n %exit"
    command = ['texts', 'session', '-l', lpad_file, '-r']
    with sp.Popen(command, stdin=sp.PIPE, shell=False) as proc:
        proc.communicate(input=model.encode())
