# -*- coding: utf-8 -*-
from odoo import models, fields


class Task(models.Model):
    _inherit = 'project.task'

    task_template_id = fields.Many2one("task.template")

    def action_create_task_template(self):
        print("haiiii")
        task = self.env['task.template'].create({
            'name': self.name,
            'project_id': self.project_id.id,
            'date_deadline': self.date_deadline,
            'description': self.description,
            'user_ids': self.user_ids,
            'tag_ids': self.tag_ids,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Task Template',
            'view_mode': 'form',
            'res_model': 'task.template',
            'res_id': task.id,
        }
