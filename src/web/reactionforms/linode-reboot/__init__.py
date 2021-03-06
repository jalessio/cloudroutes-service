######################################################################
# Cloud Routes Web Application
# -------------------------------------------------------------------
# Reaction - Forms Class
######################################################################

from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, NumberRange
from ..base import BaseReactForm


class ReactForm(BaseReactForm):

    ''' Class that creates a Reaction form for the dashboard '''

    api_key = TextField(
        "API Key",
        validators=[DataRequired(message='API Key is a required field')])
    linode_id = TextField(
        "Linode ID#",
        validators=[
            DataRequired(message='Linode ID# is a required field'),
            NumberRange(
                min=1, max=None,
                message="Linode ID should be a numeric ID number")
        ]
    )
    call_on = SelectField(
        "Call On",
        choices=[('false', 'False Monitors'), ('true', 'True Monitors')],
        validators=[DataRequired(message='Call On is a required field')])


if __name__ == '__main__':
    pass
