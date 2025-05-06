def on_a_pressed():
    # Teleports player to x=100, y=50
    player2.set_position(100, 50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

player2: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
player2 = sprites.create(img("""
        . . . . . . b b b b . . . . . .
        . . . . . . b 4 4 4 b . . . . .
        . . . . . . b b 4 4 4 b . . . .
        . . . . . b 4 b b b 4 4 b . . .
        . . . . b d 5 5 5 4 b 4 4 b . .
        . . . . b 3 2 3 5 5 4 e 4 4 b .
        . . . b d 2 2 2 5 7 5 4 e 4 4 e
        . . . b 5 3 2 3 5 5 5 5 e e e e
        . . b d 7 5 5 5 3 2 3 5 5 e e e
        . . b 5 5 5 5 5 2 2 2 5 5 d e e
        . b 3 2 3 5 7 5 3 2 3 5 d d e 4
        . b 2 2 2 5 5 5 5 5 5 d d e 4 .
        b d 3 2 d 5 5 5 d d d 4 4 . . .
        b 5 5 5 5 d d 4 4 4 4 . . . . .
        4 d d d 4 4 4 . . . . . . . . .
        4 4 4 4 . . . . . . . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(player2)
player3 = sprites.create(img("""
        ........................
        ..........bbbb..........
        ........bbddddbb........
        .......bddbbbbddb.......
        ......bdbbddddbbdb......
        .....bdbbdbbbbdbbdb.....
        .....bdbdbddddbdbdb.....
        .....cdbbdbbbbdbbdc.....
        .....cbdbbddddbbdbc.....
        .....efbddbbbbddbce.....
        .....eeffbddddbccee.....
        .....eeeeffcccceee......
        .....ceeeeeeeeeeee......
        .....ceeeeeeeeeeee......
        .....feeeeeeeeeeee......
        .....cceeeeeeeeeee......
        ......feeeeeeeeeee......
        .....6fceeeeeeeeee6.....
        ....6776eeeeeeeee676....
        ...6777666eeee6666776...
        ..67768e67766777667776..
        ...668ee7768867788666...
        ......ee77eeee77ecee....
        ......ee6eeeeee6eef.....
        """),
    SpriteKind.player)
controller.move_sprite(player3)
scene.set_background_color(9)
enemy = sprites.create(img("""
        . . . . . . . . . b 5 b . . . .
        . . . . . . . . . b 5 b . . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 5 5 5 5 5 b . . .
        . . . . b b 5 b c 5 5 d 4 c . .
        . b b b b 5 5 5 b f d d 4 4 4 b
        . b d 5 b 5 5 b c b 4 4 4 4 b .
        . . b 5 5 b 5 5 5 4 4 4 4 b . .
        . . b d 5 5 b 5 5 5 5 5 5 b . .
        . b d b 5 5 5 d 5 5 5 5 5 5 b .
        b d d c d 5 5 b 5 5 5 5 5 5 b .
        c d d d c c b 5 5 5 5 5 5 5 b .
        c b d d d d d 5 5 5 5 5 5 5 b .
        . c d d d d d d 5 5 5 5 5 d b .
        . . c b d d d d d 5 5 5 b b . .
        . . . c c c c c c c c b b . . .
        """),
    SpriteKind.enemy)
enemy.set_position(100, 60)