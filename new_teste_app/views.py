from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    flash,
    jsonify
)
from flask_login import (
    login_required,
    current_user
)
from . import db

from .main_ import (
    get_filmmaking_rotation,
    rotation_filmmaking_1,
    list_filmmaking
)

from .models import Rotation

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        reset()
        while True:
            if get_filmmaking_rotation(list_filmmaking):
                new_rotation = Rotation(
                    user_id = current_user.id,
                    tue_switch = rotation_filmmaking_1[0][0],
                    tue_joystick = rotation_filmmaking_1[1][0],
                    tue_notebook = rotation_filmmaking_1[2][0],
                    tue_camera = rotation_filmmaking_1[3][0],

                    wed_switch = rotation_filmmaking_1[0][1],
                    wed_joystick = rotation_filmmaking_1[1][1],
                    wed_notebook = rotation_filmmaking_1[2][1],
                    wed_camera = rotation_filmmaking_1[3][1],

                    thu_switch = rotation_filmmaking_1[0][2],
                    thu_joystick = rotation_filmmaking_1[1][2],
                    thu_notebook = rotation_filmmaking_1[2][2],
                    thu_camera = rotation_filmmaking_1[3][2],

                    fri_switch = rotation_filmmaking_1[0][3],
                    fri_joystick = rotation_filmmaking_1[1][3],
                    fri_notebook = rotation_filmmaking_1[2][3],
                    fri_camera = rotation_filmmaking_1[3][3],

                    sun_m_switch = rotation_filmmaking_1[0][4],
                    sun_m_joystick = rotation_filmmaking_1[1][4],
                    sun_m_notebook = rotation_filmmaking_1[2][4],
                    sun_m_camera = rotation_filmmaking_1[3][4],

                    sun_e_switch = rotation_filmmaking_1[0][5],
                    sun_e_joystick = rotation_filmmaking_1[1][5],
                    sun_e_notebook = rotation_filmmaking_1[2][5],
                    sun_e_camera = rotation_filmmaking_1[3][5],
                )
                db.session.add(new_rotation)
                db.session.commit()
                break

    return render_template('home.html', user=current_user, rotation=rotation_filmmaking_1)

@views.route('/reset', methods=['POST'])
@login_required
def reset():
    if request.method == 'POST':
        for rotation in current_user.rotation:
            db.session.delete(rotation)
            db.session.commit()
    
    return redirect(url_for('views.home'))

@views.route('/image', methods=['POST'])
@login_required
def image():
    if request.method == 'POST':
        import pandas as pd
        import dataframe_image as dfi
        import os
        os.chdir('C:/Users/jabri/Documents/flask/new_teste/new_teste_app/static/assets')
        df = pd.read_csv('rotation.csv', sep=';')
        df_styled = df.style.background_gradient()
        dfi.export(df_styled,"mytable.png")
        
