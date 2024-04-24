from odoo import fields,models,api
import logging

_logger = logging.getLogger(__name__)

class EnrollCourse(models.TransientModel):
    _name = "enroll.message.wizard"
    _description = "Enrollment Message Wizard"

    message_subject = fields.Char(default="Hi")
    message_body = fields.Html()
    enroll_course_ids = fields.Many2many("enroll.course", string="Enroll Course")

    def btn_message(self):
        ...

    def _action_open_wizard_model(self):
        '''
        Open Wizard
        '''
        return {
            'name': "Inform Message",
            'type': "ir.actions.act_window",
            'res_model': "enroll.message.wizard",
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }

    @api.model
    def get_default(self, field_names):
        default_dict = super().get_default(field_names)
        enroll_ids = self.env.context['active_ids']
        default_dict['enroll_course_ids'] = [(6, 0, enroll_ids)]

        return default_dict
