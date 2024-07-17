# -*- coding: utf-8 -*-
from odoo import models, fields


class TaskTemplate(models.Model):
    _name = "task.template"

    name = fields.Char(string='Title', required=True)
    project_id = fields.Many2one('project.project', string='Project')
    date_deadline = fields.Datetime(string='Deadline')
    partner_id = fields.Many2one(string="Customer", related="project_id.partner_id", readonly=False)
    company_id = fields.Many2one(string='Company', related="project_id.company_id")
    description = fields.Html(string='Description')
    task_count = fields.Integer(string="Tasks",
                                compute='compute_task_count')
    user_ids = fields.Many2many('res.users', string="Assignees")
    tag_ids = fields.Many2many('project.tags', string='Tags')

    def compute_task_count(self):
        for rec in self:
            rec.task_count = rec.env['project.task'].search_count(
                [('task_template_id', '=', rec.id)])

    def action_get_task_record(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'tree,form',
            'res_model': 'project.task',
            'domain': [('task_template_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def action_create_task(self):
        task = self.env['project.task'].create({
            'name': self.name,
            'state': '01_in_progress',
            'project_id': self.project_id.id,
            'date_deadline': self.date_deadline,
            'description': self.description,
            'user_ids': self.user_ids,
            'tag_ids': self.tag_ids,
            'task_template_id': self.id
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Task',
            'view_mode': 'form',
            'res_model': 'project.task',
            'res_id': task.id,
        }
