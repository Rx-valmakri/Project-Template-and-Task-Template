# -*- coding: utf-8 -*-
from odoo import models, fields


class ProjectTemplateTask(models.Model):
    _name = "project.template.task"

    name = fields.Char(string='Title', required=True)
    project_template_id = fields.Many2one("project.template")
    description = fields.Html(string='Description')
    user_ids = fields.Many2many('res.users', string="Assignees")
    date_deadline = fields.Datetime(string='Deadline')
    tag_ids = fields.Many2many('project.tags', string='Tags')