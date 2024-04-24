from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class EnrollCourse(models.TransientModel):
    _name = 'enroll.message.wizard'

    message_subject = fields.Char(default="Hi")
    message_body = fields.Html()
    enroll_course_ids = fields.Many2many('enroll.course', string="Enroll Course")

    def btn_message(self):
        ...

    def _action_open_wizard_modal(self):
        """
        Open Wizard
        :return:
        """
        return{
            'name': "Inform Message",
            'type': 'ir.actions.act_window',
            'res_model': 'enroll.message.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target_id': 'new',
        }

    @api.model
    def default_get(self, field_names):
        defaults_dict = super().default_get(field_names)
        enroll_ids = self.env.context["active_ids"]
        defaults_dict['enroll_course_ids'] = [(6, 0, enroll_ids)]
        print(defaults_dict)
        return defaults_dict