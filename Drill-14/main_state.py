import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from background import FixedBackground as Background
import ball
import collision_mgr


name = "MainState"

boy = None
background = None


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)

    background.set_center_object(boy)
    boy.set_background(background)

    for n in range(0, 100):
        game_world.add_object(ball.Ball(background), 2)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    collision_mgr.Collision_Boy_Ball(game_world.objects[2], game_world.objects[1])

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






