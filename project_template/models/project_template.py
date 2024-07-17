# -*- coding: utf-8 -*-
from odoo import models, fields, Command


class ProjectTemplate(models.Model):
    _name = "project.template"

    name = fields.Char(string="Name", required=True)
    label_tasks = fields.Char(string='Use Tasks as', default='Tasks')
    company_id = fields.Many2one('res.company', string='Company')
    partner_id = fields.Many2one('res.partner', string='Customer')
    user_id = fields.Many2one('res.users', string='Project Manager',
                              default=lambda self: self.env.user)
    date_start = fields.Date(string='Start Date')
    date = fields.Date(string='Expiration Date')

    task_ids = fields.One2many('project.template.task', "project_template_id", string='Tasks')

    project_count = fields.Integer(string="Projects",
                                          compute='compute_project_count')

    def compute_project_count(self):
        for rec in self:
            rec.project_count = rec.env['project.project'].search_count(
                [('project_template_id', '=', rec.id)])

    def action_get_project_record(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Projects',
            'view_mode': 'tree,form',
            'res_model': 'project.project',
            'domain': [('project_template_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def action_create_project(self):
        tasks = [Command.create({
            'name': rec.name,
            'user_ids': rec.user_ids,
            'description': rec.description,
            'date_deadline': rec.date_deadline,
            'tag_ids': rec.tag_ids
        })for rec in self.task_ids]

        project = self.env['project.project'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'label_tasks': self.label_tasks,
            'date_start': self.date_start,
            'date': self.date,
            'task_ids': tasks,
            'project_template_id': self.id
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Project',
            'view_mode': 'form',
            'res_model': 'project.project',
            'res_id': project.id,
        }

