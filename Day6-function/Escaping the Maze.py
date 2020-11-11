def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not is_facing_north():
    turn_right()

while not at_goal():    
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
       turn_left()
    elif wall_in_front():
        turn_right()
    elif wall_on_right():
        move()
    else:
        move()