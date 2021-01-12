while True:
    if input.sound_level() > 150:
        light.set_all(color.rgb(0,255,0))
    else:
        light.clear