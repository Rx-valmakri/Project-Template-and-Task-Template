# -*- coding: utf-8 -*-
from odoo import models, fields, Command


class Project(models.Model):
    _inherit = "project.project"

    project_template_id = fields.Many2one("project.template")

    def action_create_project_template(self):
        tasks = [Command.create({
            'name': rec.name,
            'user_ids': rec.user_ids,
            'description': rec.description,
            'date_deadline': rec.date_deadline,
            'tag_ids': rec.tag_ids,
        })for rec in self.task_ids]

        project_template = self.project_template_id.create({
            'name': self.name,
            'task_ids': tasks,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'date_start': self.date_start,
            'date': self.date,
            'label_tasks': self.label_tasks,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Project Template',
            'view_mode': 'form',
            'res_model': 'project.template',
            'res_id': project_template.id,
        }
