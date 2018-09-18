from flask import render_template, flash, redirect, url_for, session, request, g, abort
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .models import Name, Guild
from .functions import json_msg_to_text_array
import glob
import os.path
import os
import json

# TODO:
#maybe increase dimming on the white sections
#style the other pages
# maybe a static masthead of something

class User():
    def __init__(self, sid):
        self.id = sid

    #is the user allowed to authenticate?
    @property
    def is_authenticated(self):
        return True
    
    #is the user active and unbanned?
    @property
    def is_active(self):
        return True
    
    #for fake users that can't login
    @property
    def is_anonymous(self):
        return False
    
    #return an id
    def get_id(self):
        return str(self.id)

@app.before_request
def before_request():
    g.user = current_user

def int_404(p):
    try:
        return int(p)
    except:
        abort(404)

@app.route('/', methods=['GET','POST'])
def index():
    #form=ServerLoginForm()
    #if form.validate_on_submit():
    if 'pwd' in request.args:
        guild = Guild.query.filter_by(pwd=request.args['pwd']).first() #error: if two servers are assigned the same pwd app breaks, but that's unlikely
        if guild is not None:
            logout_user()
            login_user(User(guild.id))
            return redirect(url_for('pinfile_list'))
        else:
            flash("Invalid passcode!")
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/pinfile_list')
@login_required
def pinfile_list():
    pairs = []
    for fn in glob.glob(os.path.join(app.config['PINDIR'], g.user.id, "*.json")):
        channel_id = os.path.splitext(os.path.split(fn)[1])[0]
        name = Name.query.get(channel_id)
        if name is not None:
            pairs.append(("/pinfile/{}".format(channel_id), name.name)) #try dicts if fail
    return render_template('pinfile_list.html', pairs=pairs, guild_name=Guild.query.get(current_user.id))

@app.route('/pinfile/<pinfileid>')
@login_required
def pinfile(pinfileid):
    pinfileid = int_404(pinfileid)
    # don't worry, this doesn't leak
    fi = os.path.join(app.config['PINDIR'], str(current_user.id), str(pinfileid) + ".json")
    try:
        with open(fi) as f:
            j = json.load(f)
    except FileNotFoundError:
        abort(404)
    pins = []
    for o in j:
        if o['is_quote']:
            pins.append([json_msg_to_text_array(m) for m in o['messages']])
        else:
            pins.append([json_msg_to_text_array(o)])
    guild_name = Guild.query.get(current_user.id)
    channel_name = Name.query.get(pinfileid)
    return render_template('pinfile.html', guild_name=guild_name, channel_name=channel_name, pins=pins)

@app.route('/help')
def help():
    return render_template('help.html')

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500

# ADD A NO PERMISSIONS HANDLER FOR ACCESSING PINFILES OUT OF SCOPE
# NOT GONNA DO THIS ACTUALLY

#so this registers a user loader with flask-login
@lm.user_loader
def load_user(id):
    return User(id) #i can make a new user, right
