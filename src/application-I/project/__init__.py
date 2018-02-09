
def main():
    #CWD = os.getcwd()
    #ROOT = PurePath(CWD).parents[0]
    CFG = 'conf/myapp.cfg'
    logging.config.fileConfig(CFG)

    app = Flask(__name__)
    LOGGER = logging.getLogger('myapplication')


    activate_schema = app.config.update(dict(
        message=str(),
    ))


